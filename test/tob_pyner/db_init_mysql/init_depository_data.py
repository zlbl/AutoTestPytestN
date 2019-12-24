'''
Created on 2019年1月9日
@author: bobo
'''

import time
import threadpool

from test.tob_pyner.db_init_mysql.ETLSqlHelper import insert_batch

sql_pools = threadpool.ThreadPool(50)


def get_sql_insert(
        table_name,
        table_column_count,
):
    question_marks = ",".join(["%s" for i in range(table_column_count)])
    sql_insert = "INSERT INTO %s VALUES (%s)" % \
                 (table_name, question_marks)

    return sql_insert


def get_itf_account():
    table_name = 'pyner_account'
    table_column_count = 18

    func_var = []
    t3 = time.time()
    sql_insert = get_sql_insert(table_name, table_column_count)

    for j in range(100):
        print("循环第", j, "次")
        M = []
        for i in range(100000):
            index = j * 10000000000 + i
            M.append((index, index, index, 'M20003428034', '01',
                      '2000000000.11000', '1.02000', 0, '1000000001', '1',
                      '2019-01-18 15:17:00', '2019-01-18 15:17:00', 0, 0, 'U',
                      '0.00000', '2019-01-18 15:17:00', '2019-01-18 15:17:00'))
        func_var_per = (j, sql_insert, M)
        func_var.append((func_var_per, None))
        # print('生成第', i, '条数据')
    t4 = time.time()
    print("初始化完成 ", t4 - t3)

    return func_var


def get_itf_bid():
    # sql_itf_account
    table_name = 'pyner_bid'
    table_column_count = 63

    func_var = []
    t3 = time.time()

    sql_insert = get_sql_insert(table_name, table_column_count)

    print('sql_insert is ', sql_insert)
    for j in range(100):
        print("循环第", j, "次")
        M = []
        for i in range(100000):
            index = j * 10000000000 + i
            M.append((index, index, index, index, 'M20003428034', 'BID1',
                      '101.11000', '101.11000', 8, 0.08, '1.00001', '2.00002',
                      'Lended', 'Mortgage', '10000.00000', '1000.00001', '1.00001',
                      '9999.00000', '1000', '9000.00001', '1.00000', '2.00000',
                      '3.00000', '4.00000', '5.00000', '2019-01-10 12:00:00',
                      '2019-01-10 12:00:40', '2019-01-31 12:00:00',
                      '2019-01-31 12:00:00', '2019-01-31 11:00:00', '1', '0',
                      10, '0.08', '0.07', 'FixedBasisMortgage', '05', '0.05',
                      '测试用途', 0, '1000000001', '1', '2019-01-21 11:00:00',
                      '2019-01-21 11:00:00', 0, 0, 'U', '0.00008', '0.22222',
                      '0.22222', '0.22222', '0.22222', '0.22222', '0.22222',
                      'Person', '严东军', 'IDC', '330226198612253672', 1,
                      '2019-01-21 11:00:00', '2019-01-21 11:00:00',
                      '2019-01-21 11:00:00', '2019-01-22 11:00:00'))
        func_var_per = (j, sql_insert, M)
        func_var.append((func_var_per, None))
        # print('生成第', i, '条数据')
    t4 = time.time()
    print("初始化完成 ", t4 - t3)

    return func_var


def get_itf_obligatory():
    # sql_itf_account
    table_name = 'pyner_obligatory'
    table_column_count = 45

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
                (index, index, index, index, 0, index, index, 'M20002661169',
                 300.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000,
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 1, 1,
                 '2017-06-19 16:43:00', '2017-06-30 09:43:14', 0, 0, 'U',
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000,
                 1000.00000, 'Lended', 'Mortgage', 'Person', '严东军', 'IDC',
                 '330226198612253672', 8, '2017-06-19 16:43:00',
                 '2017-06-19 16:43:00', index, index))
        func_var_per = (j, sql_insert, M)
        func_var.append((func_var_per, None))
        # print('生成第', i, '条数据')
    t4 = time.time()
    print("初始化完成 ", t4 - t3)

    return func_var


def get_itf_user():
    # sql_itf_account
    table_name = 'pyner_user'
    table_column_count = 42

    func_var = []
    t3 = time.time()

    sql_insert = get_sql_insert(table_name, table_column_count)

    print('sql_insert is ', sql_insert)
    for j in range(100):
        print("循环第", j, "次")
        M = []
        for i in range(100000):
            index = j * 10000000000 + i
            M.append((index, index, index, 'Person', 'M20003428034', '彩麒麟',
                      'Lender', '2018-01-09 08:00:10', '中国', '01', '浙江省', '01',
                      '杭州', '100000', '西湖区', '西湖区外婆家', '15158881253', 'T', 0,
                      '100000000001', 1, '2018-12-26 12:35:55',
                      '2017-11-23 12:49:48', 0, 0, 'U', '罗淑敏', 'IDC',
                      '330226198612253672', 'Y', 'Y', '错误', 3,
                      '2015-01-09 08:00:10', '2016-01-09 08:00:10',
                      '2019-01-21 08:00:10', 1, '2019-01-21 08:00:10',
                      '2019-01-08 16:00:00', '2019-01-08 16:00:00', '1', '1'))
        func_var_per = (j, sql_insert, M)
        func_var.append((func_var_per, None))
        # print('生成第', i, '条数据')
    t4 = time.time()
    print("初始化完成 ", t4 - t3)

    return func_var


def get_itf_user_person():
    # sql_itf_account
    table_name = 'pyner_user_person'
    table_column_count = 17

    func_var = []
    t3 = time.time()

    sql_insert = get_sql_insert(table_name, table_column_count)

    print('sql_insert is ', sql_insert)
    for j in range(100):
        print("循环第", j, "次")
        M = []
        for i in range(100000):
            index = j * 10000000000 + i
            M.append((index, 'M20003428034', '严东军', 'IDC',
                      '330226198612253672', '1', '1986-12-25', 0, 100000000001,
                      1, '2019-01-08 16:00:00', '2019-01-08 16:00:00', 0, 0,
                      'U', '2019-01-08 16:00:00', '2019-01-08 16:00:00'))
        func_var_per = (j, sql_insert, M)
        func_var.append((func_var_per, None))
        # print('生成第', i, '条数据')
    t4 = time.time()
    print("初始化完成 ", t4 - t3)

    return func_var


def get_itf_user_report():
    # sql_itf_account
    table_name = 'pyner_user_report'
    table_column_count = 40

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
                (index, 'M20004665224', 'Person', 180, 1, 2572803.00000, 2612100, 12330.00000, 4,
                 4567780.00000, 5, 0.00000, 6, 43240.00000, 7, 23420.00000, 8, 272385447936798720, 1000000001,
                 100000000001, '2019-01-22 15:22:30', '2019-01-22 15:22:30', 0, 0, 'U', 'Lender',
                 '周露', 'IDC', '610724198710070070', '2018-01-21 01:00:00', '2018-01-21 01:00:00',
                 'M', '1987-10-07', '2019-01-13 09:19:34', '61', '陕西省', '07', '汉中市', '108.95', '34.27'))
        func_var_per = (j, sql_insert, M)
        func_var.append((func_var_per, None))
        # print('生成第', i, '条数据')
    t4 = time.time()
    print("初始化完成 ", t4 - t3)

    return func_var


def get_itf_trade():
    # sql_itf_account
    table_name = 'pyner_trade'
    table_column_count = 51

    func_var = []
    t3 = time.time()

    sql_insert = get_sql_insert(table_name, table_column_count)

    print('sql_insert is ', sql_insert)
    for j in range(501, 600):
        print("循环第", j, "次")
        M = []
        for i in range(100000):
            index = j * 10000000000 + i
            M.append(
                (index, index, index, 'M20004665224', '海享贷', '1068', '20005747132',
                 '6536', 123, '20007306302', '6960', 123, 1500000.00000, 1500000.00000,
                 1500000.00000, 'CNY', '3100', '3014', 'Success', '2018-05-14 08:58:46',
                 321, '2', '2019-01-21 10:20:01', '2019-01-21 01:00:00', '2019-01-21',
                 123, 333, 234, 543, 'N', 453, '2019-01-22 16:08:27', 1, 423, 1000000001,
                 100000000001, '2019-01-22 16:08:25', '2019-01-22 16:08:27', 888, 1,
                 'U', 'Person', '张可恒', 'IDC', '350425198501030925', '350425',
                 '湖北省武汉市乔口区', '3014', '1000', '2019-01-21 01:00:00', 23.5))
        func_var_per = (j, sql_insert, M)
        func_var.append((func_var_per, None))
        # print('生成第', i, '条数据')
    t4 = time.time()
    print("初始化完成 ", t4 - t3)

    return func_var


def test2():
    # func_var = get_itf_account()
    # func_var = get_itf_bid()
    # func_var = get_itf_obligatory()
    # func_var = get_itf_user()
    # func_var = get_itf_user_person()
    # func_var = get_itf_user_report()
    func_var = get_itf_trade()
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
