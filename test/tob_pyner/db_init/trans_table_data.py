"""
Created on 2019年1月10日
@author: bobo
@Description:该类负责调度各表传输数据的任务
"""
# 用户名 密码 host port sid
# oracle_auths = [('b2b_pyner_ucfloan', 'oracle', '192.168.5.164', '1521', 'db11g'),
#                 ('b2b_pyner_lanmaoloan', 'oracle', '192.168.5.164', '1521', 'db11g')]
import cx_Oracle

import time
import threadpool

from util.common.db.oracle_helper import OracleHelper

from util.common.db.MySqlHelper import insert_batch

oracle_auths = [('b2b_pyner_ucfloan', 'oracle', '192.168.5.164', '1521',
                 'db11g'),
                ('b2b_pyner_lanmaoloan', 'oracle', '192.168.5.164', '1521',
                 'db11g')]

# 用户名 密码 host port database
mysql_auths = [('root', '123456', '192.168.5.94', '3306',
                'b2b_pyner_original_ucf'),
               ('root', '123456', '192.168.5.94', '3306',
                'b2b_pyner_original_lanmao')]

# 定义存管数据库
oracle_dbs = []

# 定义目标库数据库
# mysql_dbs = []

table_pool = threadpool.ThreadPool(10)

table_batch_pool = threadpool.ThreadPool(20)

limit = 100000


def init():
    """
    初始化数据库连接池
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
    # for mysql_auth in mysql_auths:
    #     print('+++++++++ init mysql ', mysql_auth)
    #     # mysql_dbs.append(Mysql(mysql_auth[0], mysql_auth[1], mysql_auth[2], mysql_auth[3], mysql_auth[4]))
    #     mysql_dbs.append(
    #         MySQLHelper(mysql_auth[0], mysql_auth[1], mysql_auth[2],
    #                     mysql_auth[3], mysql_auth[4]))
    print('init mysql db finished!')


def multi_mig_oracle_table(index, table_list):
    func_var = []
    for table in table_list:
        func_var_per = (index, table)
        func_var.append((func_var_per, None))

    requests = threadpool.makeRequests(multi_mig_oracle_datas, func_var)
    [table_pool.putRequest(req) for req in requests]
    table_pool.wait()
    print("multi_mig_oracle_table finished")


def multi_mig_oracle_datas(index, table):
    print("multi_mig_oracle_datas start ", table)
    query_sql = "SELECT * FROM %s" % (table,)
    # total_datas = oracle_dbs[index].queryAll(query_sql)

    oracle_cursor = oracle_dbs[index].cursor
    oracle_cursor.execute(query_sql)
    table_metadata = oracle_dbs[index].get_table_metadata(table)

    func_var_batch = []
    print("单循环生成任务开始 ", table)
    while True:
        table_data_array = oracle_cursor.fetchmany(limit)
        print("fetch ", limit)
        if len(table_data_array) <= 0:
            break

        func_var_batch_per = (index, table, table_data_array, table_metadata)
        func_var_batch.append((func_var_batch_per, None))

    print("循环生成任务结束 ", table)
    requests = threadpool.makeRequests(mig_oracle_datas, func_var_batch)
    print("生成任务")
    [table_batch_pool.putRequest(req) for req in requests]
    print("等待执行完成")
    table_batch_pool.wait()
    print("multi_mig_oracle_datas finished")


def mig_oracle_datas(index, table, table_data_array, table_metadata):
    print("mig_oracle_datas start")
    # mysql_cursor = mysql_dbs[index].cursor
    # mysql_conn = mysql_dbs[index]._conn

    rows = []

    sql_insert_final = ''

    for table_data in table_data_array:
        # print("处理 ", table_data)
        sql_insert, column_values = get_mysql_insert_sql(table, table_data, table_metadata)
        sql_insert_final = sql_insert
        rows.append(column_values)

    # print("rows is ", len(rows))
    # print("rows is ", rows)
    # print("sql_insert_final is ", sql_insert_final)

    # mysql_cursor.executemany(sql_insert_final, rows)
    # mysql_conn.commit()

    insert_batch(sql_insert_final, rows)

    print("mig_oracle_datas end")


def get_mysql_insert_sql(table, table_data, table_metadata):
    """
    根据某一行数据获取插入语句
    :param table_data:
    :param table_metadata:
    :return:
    """
    column_names = []
    column_values = []
    index_tmp = 0
    for column in table_metadata:
        if column['name'] == 'LINES':
            column_names.append('NUM_LINES')
        else:
            column_names.append(column['name'])

        column_value = table_data[index_tmp]
        if column_value:
            if column['type'] == cx_Oracle.TIMESTAMP:
                column_value = str(column_value)
        # else:
        # column_value = ''

        if column_value is None:
            if column['type'] == cx_Oracle.TIMESTAMP:
                column_value = 0
            elif column['type'] == cx_Oracle.NUMBER:
                column_value = 0
            else:
                column_value = ''
        column_values.append(column_value)
        index_tmp += 1

    question_marks = ",".join(["%s" for i in range(len(column_names))])
    sql_insert = "INSERT INTO %s (%s) VALUES (%s)" % \
                 (table, ",".join(column_names), question_marks)

    # print("sql_insert is ", sql_insert)
    # print("column_values is ", column_values)
    # print("column_values len is ", len(column_values))

    return sql_insert, column_values


def test_do_trans():
    print('初始化开始')
    # 初始化数据库
    init()
    print('初始化结束')

    # 后面改成多线程
    print('查询UCF表')
    # mig_oracle_database(0)
    t1 = time.time()
    # mig_oracle_datas(0, "UCF_ACCOUNT_TEST")
    table_list = ["UCF_ACCOUNT_LOG"]
    multi_mig_oracle_table(0, table_list)
    t2 = time.time()
    print("UCF_ACCOUNT 表同步完成 用时", t2 - t1, " 秒")
    print('查询UCF表结束')

    # 后面改成多线程
    print('查询懒猫表')
    # mig_oracle_database(1)
    print('查询懒猫表结束')

    # 校验数据库完整性

    # 查询所有表

    # 查询mysql所有表
