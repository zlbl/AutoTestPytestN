"""
Created on 2019年1月15日
@author: bobo
@Description:将sql脚本进行分组添加至接口表中
"""
import sys
import threadpool
import time

from test.tob_pyner.db_init import trans_sql_data_conf
from test.tob_pyner.db_init.MySqlHelper import list_col, insert_batch
from test.tob_pyner.db_init.oracle_helper import OracleHelper

oracle_auths = [('b2b_pyner_ucfloan', 'oracle', '192.168.5.164', '1521',
                 'db11g'),
                ('b2b_pyner_lanmaoloan', 'oracle', '192.168.5.164', '1521',
                 'db11g')]

oracle_dbs = []

# 后面配置到配置文件中
# 先锋
# sql_pools = [threadpool.ThreadPool(10), threadpool.ThreadPool(10)]

# sql_batch_pools = [threadpool.ThreadPool(20), threadpool.ThreadPool(20)]

# 每次批量处理多少条数据
batch_num = 50000


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
    func_var = []
    for sql in sqls:
        func_var_per = (index, sql)
        func_var.append((func_var_per, None))

    sql_pools = threadpool.ThreadPool(10)
    requests = threadpool.makeRequests(multi_migrate_sql, func_var)
    # [sql_pools[index].putRequest(req) for req in requests]
    # sql_pools[index].wait()
    [sql_pools.putRequest(req) for req in requests]
    sql_pools.wait()
    print("multi_migrate_tasks end index is ", index)


def multi_migrate_sql(index, sql):
    """
    批量更新数据并插入
    :param index: 数据库下标 0 UCF_ORACLE 1 LANMAO_ORACLE
    :param sql: 数据结构如配置中一样(query_sql, table_name)
    :return:
    """
    table_name = sql[1]
    query_sql = sql[0]

    # 后面搞成oracle数据库连接池的形式
    oracle_cursor = oracle_dbs[index].cursor

    query_count_sql = "select count(*) from (%s)" % (query_sql, )
    print("查询语句是 ", query_count_sql)
    # 查询表行数
    rows_count = oracle_dbs[index].queryOne(query_count_sql)
    print(table_name, "表共有", rows_count, "条数据")

    # 计算需要执行多少次
    run_times = int(rows_count[0] / batch_num)
    print("run times is ", run_times)

    # 执行查询语句
    oracle_cursor.execute(query_sql)

    table_columns = list_col(table_name)

    

    func_var_batch = []
    print("单循环生成任务开始 ", table_name)

    # fetch_pools = threadpool.ThreadPool(10)

    # while True:
    #     t5 = time.time()
    #     data_array = oracle_cursor.fetchmany(batch_num)
    #     t6 = time.time()
    #     print("fetchmany ", batch_num, "需要耗时 ", t6 - t5, " s")
    #     if len(data_array) <= 0:
    #         break

    #     print("fetch ", batch_num)

    #     func_var_batch_per = (data_array, table_name, table_columns)
    #     func_var_batch.append((func_var_batch_per, None))


def test_trans_test():
    try:
        init_dbs()

        multi_migrate_tasks
    except ImportError as e1:
        print(e1)
        sys.exit(1)

    try:
        sqls_ucf = trans_sql_data_conf.sqls_ucf
        print("sqls ucf ", trans_sql_data_conf.sqls_ucf)
        # sqls_lanmao = conf_module.lanmao
        # print("sqls lanmao ", sqls_lanmao)
    except AttributeError as e2:
        print(e2)
        sys.exit(1)
    """
    0 先锋 1 懒猫
    """
    t1 = time.time()
    multi_migrate_tasks(0, sqls_ucf)
    t2 = time.time()

    print("总共耗时，", t2 - t1, " s")
