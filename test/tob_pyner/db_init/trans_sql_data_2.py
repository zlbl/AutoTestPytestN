"""
Created on 2019年1月15日
@author: bobo
@Description:将sql脚本进行分组添加至接口表中
"""
import sys
import threadpool
import logging
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
    query_sql = sql[0]
    table_name = sql[1]

    query_count_sql = "select count(*) from (%s)" % (query_sql,)
    print("查询语句是 ", query_count_sql)
    # 查询表行数
    rows_count = oracle_dbs[index].queryOne(query_count_sql)
    print(table_name, "表共有", rows_count, "条数据")

    # 计算需要执行多少次
    run_times = int(rows_count[0] / batch_num)
    print("run times is ", run_times)

    # 后面搞成oracle数据库连接池的形式
    oracle_cursor = oracle_dbs[index].cursor
    # 执行查询语句
    oracle_cursor.execute(query_sql)

    table_columns = list_col(table_name)

    func_var_batch = []
    print("单循环生成任务开始 ", table_name)

    for i in range(run_times):
        func_var_batch_per = ([], table_name, table_columns)
        func_var_batch.append((func_var_batch_per))

    t3 = time.time()
    print("循环生成任务结束 ", table_name)

    sql_batch_pools = threadpool.ThreadPool(1)

    requests = threadpool.makeRequests(multi_mig_oracle_datas, func_var_batch)
    # requests = threadpool.makeRequests(multi_mig_oracle_datas_test, func_var_batch)
    print("生成任务")
    # [sql_batch_pools[index].putRequest(req) for req in requests]
    [sql_batch_pools.putRequest(req) for req in requests]
    print("等待执行完成")
    sql_batch_pools.wait()

    t4 = time.time()
    print("全部批量操作完成耗时 ", t4 - t3, " s")
    print("multi_migrate_sqls finished")


def multi_mig_oracle_datas_test(table_name, table_columns):
    """
    具体同步oralce数据库中的数据至Mysql中
    :param table_name:
    :param table_columns:
    :return:
    """
    # 第一步先fetch数据
    # data_array = oracle_cursor.fetchmany(batch_num)
    data_array = []

    question_marks = ",".join(["%s" for i in range(len(table_columns))])
    table_columns_marks = ",".join(table_columns)

    # print("question_marks is ", question_marks)
    # print("table_columns_marks is ", table_columns_marks)
    sql_insert = "INSERT INTO %s (%s) VALUES (%s)" % \
                 (table_name, table_columns_marks, question_marks)

    # print("sql_insert is ", sql_insert)
    t1 = time.time()
    insert_batch(sql_insert, data_array)
    t2 = time.time()
    print("insert_batch 单个批量插入耗时 ", t2 - t1, " s")


def multi_mig_oracle_datas(data_array, table_name, table_columns):
    """
    具体同步oralce数据库中的数据至Mysql中
    :param data_array: 从oracle数据库中查询出来的数据
    :param table_name: 最终需要生成的目标mysql数据库表
    :return:
    """
    question_marks = ",".join(["%s" for i in range(len(table_columns))])
    table_columns_marks = ",".join(table_columns)

    # print("question_marks is ", question_marks)
    # print("table_columns_marks is ", table_columns_marks)
    sql_insert = "INSERT INTO %s (%s) VALUES (%s)" % \
                 (table_name, table_columns_marks, question_marks)

    # print("sql_insert is ", sql_insert)
    t1 = time.time()
    insert_batch(sql_insert, data_array)
    t2 = time.time()
    print("insert_batch 单个批量插入耗时 ", t2 - t1, " s")


# if __name__ == "__main__":
def test_trans():
    # if len(sys.argv) < 3:
    #     print("""Usage: oracle2mysql.py CONF_MODULE_NAME
    #     where CONFIG_MODULE is the name of a python module
    #     that defines 3 variables:
    #     oracle = a cx_Oracle connection object instance, to use for source
    #     mysql  = a MySQLdb connection object instance, to use for target
    #     tables = an iterable of string table names to migrate
    #
    #     Example:
    #
    #     # python trans_sql_data.py trans_sql_data_conf 0""")
    #     sys.exit(0)

    # conf_module_name = sys.argv[1]
    conf_module_name = "trans_sql_data_conf"
    # db_select = sys.argv[2]
    db_select = 0
    try:
        # conf_module = __import__(conf_module_name)

        init_dbs()
    except ImportError as e1:
        print(e1)
        print("ERROR: Could not find config module: %s" % (conf_module_name,))
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
    logging.info("开始 multi_migrate_tasks")
    t1 = time.time()
    multi_migrate_tasks(db_select, sqls_ucf)
    t2 = time.time()

    print("总共耗时，", t2 - t1, " s")
