"""
Created on 2019年1月15日
@author: bobo
@Description:将sql脚本进行分组添加至接口表中
"""
import logging
import time
from datetime import datetime

import threadpool

from test.tob_pyner.db_init import trans_sql_data_conf
from test.tob_pyner.db_init.MySqlHelper import list_col, insert_batch
from test.tob_pyner.db_init.oracle_helper import OracleHelper
from test.tob_pyner.db_init.trans_sql_data_conf import oracle_auths, batch_num, db_select

oracle_dbs = []


def init_dbs():
    """
    初始化数据库
    :return:
    """
    print('init oracle db start!')
    for oracle_auth in oracle_auths:
        print('+++++++++ init oracle ', oracle_auth)
        oracle_db = OracleHelper(oracle_auth[0], oracle_auth[1],
                                 oracle_auth[2], oracle_auth[3],
                                 oracle_auth[4])
        oracle_dbs.append(oracle_db)

    print('init oracle db finished!')

    print('init mysql db start!')
    print('mysql db init ignore!')
    print('init mysql db finished!')


def multi_migrate_tasks(index, sqls):
    """
    mysql数据已经在mysql_helper.py中配置
    :param index: 数据库实例 序号
    :param sqls:需要执行的sql语句
    :return:
    """
    # 第一步，多线程处理不同sql
    # func_var = []
    for sql in sqls:
        start_date = datetime.now()
        multi_migrate_sql(index, sql)
        end_date = datetime.now()
        print('插入的数据库', sql[1])
        print('开始时间: ', start_date)
        print('结束时间: ', end_date)

    #     func_var_per = (index, sql)
    #     func_var.append((func_var_per, None))
    #
    # requests = threadpool.makeRequests(multi_migrate_sql, func_var)
    # # [sql_pools[index].putRequest(req) for req in requests]
    # # sql_pools[index].wait()
    # [sql_pools.putRequest(req) for req in requests]
    # sql_pools.wait()
    print("multi_migrate_tasks end index is ", index)


def multi_migrate_sql(index, sql):
    """
    批量更新数据并插入
    :param index: 数据库下标 0 UCF_ORACLE 1 LANMAO_ORACLE
    :param sql: 数据结构如配置中一样(query_sql, table_name)
    :return:
    """
    insert_pool = threadpool.ThreadPool(5)
    query_sql = sql[0]
    table_name = sql[1]

    # 后面搞成oracle数据库连接池的形式
    oracle_cursor = oracle_dbs[index].cursor
    # 执行查询语句
    oracle_cursor.execute(query_sql)

    table_columns = list_col(table_name)

    print("单循环生成任务开始 ", table_name)

    # 五个线程同时插入
    insert_index = 0
    while True:
        insert_index += 1
        data_array = oracle_cursor.fetchmany(batch_num)

        if len(data_array) == 0:
            insert_pool.wait()
            break
        # 放入插入数据的线程池中
        func_var_batchs = []
        func_var_batch_per = (data_array, table_name, table_columns)
        func_var_batchs.append((func_var_batch_per, None))
        requests = threadpool.makeRequests(multi_mig_oracle_datas, func_var_batchs)
        [insert_pool.putRequest(req) for req in requests]

        if insert_index % 5 == 0:
            batch_start_time = time.time()

            # 等待线程插入结束
            insert_pool.wait()
            # 清空参数
            func_var_batchs.clear()
            batch_end_time = time.time()
            print('多线程批量插入耗时 {} s'.format(batch_end_time - batch_start_time))
    print('批量插入结束')


def multi_mig_oracle_datas(data_array, table_name, table_columns):
    """
    具体同步oralce数据库中的数据至Mysql中
    :param data_array: 从oracle数据库中查询出来的数据
    :param table_name: 最终需要生成的目标mysql数据库表
    :return:
    """
    question_marks = ",".join(["%s" for i in range(len(table_columns))])
    table_columns_marks = ",".join(table_columns)

    sql_insert = "INSERT IGNORE INTO %s (%s) VALUES (%s)" % \
                 (table_name, table_columns_marks, question_marks)

    # print("sql_insert is ", sql_insert)
    # t1 = time.time()
    insert_batch(sql_insert, data_array)
    # t2 = time.time()
    # print("insert_batch 单个批量插入耗时 ", t2 - t1, " s")
    # return t2 - t1


if __name__ == "__main__":
    # def test_trans():
    start_date_time = datetime.now()
    print('开始时间:', start_date_time)

    init_dbs()
    if db_select == 0:
        sqls = trans_sql_data_conf.sqls_ucf
        print("sqls ucf ", sqls)
    else:
        sqls = trans_sql_data_conf.sqls_lanmao
        print("sqls lanmao ", sqls)

    """
    0 先锋 1 懒猫
    """
    logging.info("开始 multi_migrate_tasks")
    t1 = time.time()
    multi_migrate_tasks(db_select, sqls)
    t2 = time.time()
    print('总开始时间:', start_date_time)
    print('总结束时间:', datetime.now())

    print("总共耗时，", t2 - t1, " s")
