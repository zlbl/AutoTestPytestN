'''
Created on 2019年1月9日
@author: bobo
'''

import time
import threadpool

from test.tob_pyner.db_init_mysql.ETLSqlHelper import insert_batch
from faker import Faker, Factory

sql_pools = threadpool.ThreadPool(50)


def get_sql_insert(table_name, table_column_count, ):
    question_marks = ",".join(["%s" for i in range(table_column_count)])
    sql_insert = "INSERT INTO %s VALUES (%s)" % \
                 (table_name, question_marks)

    return sql_insert


def get_itf_account():
    # sql_itf_account
    table_name = 'itf_account'
    table_column_count = 17

    func_var = []
    t3 = time.time()
    sql_insert = get_sql_insert(table_name, table_column_count)

    for j in range(100):
        print("循环第", j, "次")
        M = []
        for i in range(100000):
            index = j * 10000000000 + i
            M.append(
                (index, index, index, 'M20003428034', '01', '2000000000.11000', '1.02000', '1000000001', '1',
                 '2019-01-18 15:17:00', '2019-01-18 15:17:00', 0, 0, 'U', '0.00000',
                 '2019-01-18 15:17:00', '2019-01-18 15:17:00'))
        func_var_per = (j, sql_insert, M)
        func_var.append((func_var_per, None))
            # print('生成第', i, '条数据')
    t4 = time.time()
    print("初始化完成 ", t4 - t3)

    return func_var


def get_itf_bid():
    # sql_itf_account
    table_name = 'itf_bid'
    table_column_count = 33

    func_var = []
    t3 = time.time()

    sql_insert = get_sql_insert(table_name, table_column_count)

    print('sql_insert is ', sql_insert)
    for j in range(100):
        print("循环第", j, "次")
        M = []
        for i in range(100000):
            index = j * 10000000000 + i
            M.append(
                (index, index, index, index, 'M20003428034', 'BID' + str(index), '101.11000',
                 index, '8', '0.08',
                 'Lended', 'Mortgage', '1000.00000', '1.0000', '2019-01-01 12:00:00', '2019-01-01 13:00:00',
                 '2019-01-01 14:00:00', 1,
                 0,
                 'FirstInterestLastPrincipal',
                 '05', '用途', '1000000001', '1', '2019-01-21 12:00:00', '2019-01-21 12:00:00', 0, 0, 'U',
                 '2019-01-21 12:00:00', '2019-01-21 12:00:00', '100', '2019-01-21 12:00:00')
            )
        func_var_per = (j, sql_insert, M)
        func_var.append((func_var_per, None))
            # print('生成第', i, '条数据')
    t4 = time.time()
    print("初始化完成 ", t4 - t3)

    return func_var


def get_itf_obligatory():
    # sql_itf_account
    table_name = 'itf_obligatory'
    table_column_count = 27
    faker1 = Faker("zh_CN")

    func_var = []
    t3 = time.time()

    sql_insert = get_sql_insert(table_name, table_column_count)

    print('sql_insert is ', sql_insert)
    for j in range(1):
        print("循环第", j, "次")
        M = []
        for i in range(1):
            index = j * 10000000000 + i
            M.append(
                (index, index, index, index, index, 'M20003428034', '10000.00001', '0.0000', '1.00000', '1000000001',
                 '1',
                 '2019-01-21 12:00:00', '2019-01-21 12:00:00', 0, 0, 'U', '2019-01-21 12:00:00', '2019-01-21 12:00:00',
                 index, index, '10000.00000', 'Lended', 'Mortgage', 'Person', '严波波', 'IDC', '330226198612253672')
            )
        func_var_per = (j, sql_insert, M)
        func_var.append((func_var_per, None))
            # print('生成第', i, '条数据')
    t4 = time.time()
    print("初始化完成 ", t4 - t3)

    return func_var


def get_itf_user():
    # sql_itf_account
    faker1 = Faker("zh_CN")
    table_name = 'itf_user'
    table_column_count = 21

    func_var = []
    t3 = time.time()

    sql_insert = get_sql_insert(table_name, table_column_count)

    print('sql_insert is ', sql_insert)
    for j in range(100):
        print("循环第", j, "次")
        M = []
        for i in range(100000):
            index = j * 10000000000 + i
            M.append(
                (index, index, index, 'Person', 'M20003428034', 'Borrower', '杭州', '15158881253', 'T', '1000000001', '1',
                 '2019-01-21 12:00:00', '2019-01-21 12:00:00', 0, 0, 'U', '2019-01-21 12:00:00', '2019-01-21 12:00:00',
                 '严波波', 'IDC', faker1.ssn())
            )
        func_var_per = (j, sql_insert, M)
        func_var.append((func_var_per, None))
            # print('生成第', i, '条数据')
    t4 = time.time()
    print("初始化完成 ", t4 - t3)

    return func_var


def get_itf_user_person():
    # sql_itf_account
    faker1 = Faker("zh_CN")
    table_name = 'itf_user_person'
    table_column_count = 14

    func_var = []
    t3 = time.time()

    sql_insert = get_sql_insert(table_name, table_column_count)

    print('sql_insert is ', sql_insert)
    for j in range(100):
        print("循环第", j, "次")
        M = []
        for i in range(100000):
            index = j * 10000000000 + i
            M.append(
                (
                    index, 'M20003428034', '严' + str(index), 'IDC', faker1.ssn(), '1000000001',
                    '1',
                    '2019-01-21 12:00:00',
                    '2019-01-21 12:00:00', 0, 0, 'U', '2019-01-21 12:00:00', '2019-01-21 12:00:00')
            )
        func_var_per = (j, sql_insert, M)
        func_var.append((func_var_per, None))
            # print('生成第', i, '条数据')
    t4 = time.time()
    print("初始化完成 ", t4 - t3)

    return func_var


def get_itf_trade():
    # sql_itf_account
    table_name = 'itf_trade'
    table_column_count = 43

    func_var = []
    t3 = time.time()

    sql_insert = get_sql_insert(table_name, table_column_count)

    print('sql_insert is ', sql_insert)
    for j in range(1000):
        print("循环第", j, "次")
        M = []
        for i in range(100000):
            index = j * 10000000000 + i
            M.append(
                (
                index, index, index, 'M20003428034', '压力测试用', index, index, index, index, index, '100.00000', '1.00000',
                '1.00000', '1', 'Recharge',
                '1013', 'Success', '2019-01-21 12:00:00', '测试用', '来源', '2019-01-21 13:00:00', '2019-01-21', '1', index,
                index,
                index, '1', '1.00000', '2019-02-27 12:00:00', '0', 'B2C', '1000000001', '1', '2019-01-21 12:00:00',
                '2019-01-21 12:00:00', 0, 0, 'U', '1013', '', '2019-01-21 12:00:00', '2019-01-21 12:00:00', 0)
            )
        func_var_per = (j, sql_insert, M)
        func_var.append((func_var_per, None))
            # print('生成第', i, '条数据')
    t4 = time.time()
    print("初始化完成 ", t4 - t3)

    return func_var


def test2():
    # func_var = get_itf_account()
    func_var = get_itf_bid()
    # func_var = get_itf_obligatory()
    # func_var = get_itf_user()
    # func_var = get_itf_user_person()
    # func_var = get_itf_trade()
    t1 = time.time()
    requests = threadpool.makeRequests(execute_sql, func_var)
    [sql_pools.putRequest(req) for req in requests]
    sql_pools.wait()

    t2 = time.time()
    print('total it last ', t2 - t1, ' s')
    print('insert batch ok.')


def execute_sql(i, sql, M):
    t1 = time.time()
    print('execute_sql start.', i)
    insert_batch(sql, M)
    t2 = time.time()
    print('execute_sql ok.', i, ' last ', (t2 - t1))
