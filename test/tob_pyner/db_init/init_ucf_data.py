'''
Created on 2019年1月9日
@author: bobo
'''

import time

import cx_Oracle


def test_oracle_select():
    # conn = cx_Oracle.connect('用户名/密码@主机ip地址/orcl')  # 用自己的实际数据库用户名、密码、主机ip地址 替换即可
    conn = cx_Oracle.connect('b2b_pyner_ucfloan/oracle@192.168.5.164/db11g')  # 用自己的实际数据库用户名、密码、主机ip地址 替换即可
    curs = conn.cursor()
    sql = 'select * from UCF_ACCOUNT order by account_no desc'  # sql语句
    rr = curs.execute(sql)
    row = curs.fetchone()
    print(row)
    curs.close()
    conn.close()


class Oracle(object):
    """  oracle db operator  """

    def __init__(self, userName, password, host, instance):
        self._conn = cx_Oracle.connect("%s/%s@%s/%s" % (userName, password, host, instance))
        self.cursor = self._conn.cursor()

    def queryTitle(self, sql, nameParams={}):
        if len(nameParams) > 0:
            self.cursor.execute(sql, nameParams)
        else:
            self.cursor.execute(sql)

        colNames = []
        for i in range(0, len(self.cursor.description)):
            colNames.append(self.cursor.description[i][0])

        return colNames

    # query methods
    def queryAll(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def queryOne(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def queryBy(self, sql, nameParams={}):
        if len(nameParams) > 0:
            self.cursor.execute(sql, nameParams)
        else:
            self.cursor.execute(sql)

        return self.cursor.fetchall()

    def insertBatch(self, sql, nameParams=[]):
        """batch insert much rows one time,use location parameter"""
        self.cursor.prepare(sql)
        self.cursor.executemany(None, nameParams)
        self.commit()

    def commit(self):
        self._conn.commit()

    def __del__(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()

        if hasattr(self, '_conn'):
            self._conn.close()


oraDb = Oracle('b2b_pyner_ucfloan', 'oracle', '192.168.5.164', 'db11g')
cursor = oraDb.cursor


def init_table():
    create_table = """
        create table UCF_ACCOUNT_TEST
    (
      ACCOUNT_NO       VARCHAR2(32)           not null,
      ACCOUNT_TYPE     VARCHAR2(10)           not null,
      CURRENCY         VARCHAR2(6)            not null,
      AMOUNT           NUMBER(15)             not null,
      FREEZE_AMOUNT    NUMBER(15)             not null,
      UNCLEARED_AMOUNT NUMBER(15)   default 0 not null,
      STATUS           VARCHAR2(2)            not null,
      REF_MERCHANT     VARCHAR2(32)           not null,
      USER_ID          VARCHAR2(32)           not null,
      TEMP_CREATE      VARCHAR2(100),
      TEMP_MODIFIED    VARCHAR2(100),
      REMARK           VARCHAR2(255),
      LOAN_AMOUNT      NUMBER(15),
      ADVANCE_AMOUNT   NUMBER(15),
      LAST_ERASE_DATE  NUMBER(8),
      GMT_CREATE       TIMESTAMP(6) default NULL,
      GMT_MODIFIED     TIMESTAMP(6)
    )
        """
    cursor.execute(create_table)


def drop_tabe():
    cursor.execute("DROP TABLE UCF_ACCOUNT_TEST PURGE")


def truncate_table():
    cursor.execute("TRUNCATE TABLE UCF_ACCOUNT_TEST")


# def test2():
#     id = 1
#     # 更新存管ID
#     # update UCF_ACCOUNT_1 set REF_MERCHANT = 'M200027136632'
#     for i in range(100):
#         ref_index = id + i
#         print("开始更新表 ref_index ", ref_index)
#         sql_temp = "update UCF_ACCOUNT_1 set REF_MERCHANT = " + str(ref_index)
#         print("执行sql", sql_temp)
#         cursor.execute(sql_temp)
#         oraDb.commit()
#         print("执行完成", time.asctime())
#         sql = "INSERT INTO B2B_PYNER_UCFLOAN_TEST.UCF_ACCOUNT SELECT * FROM UCF_ACCOUNT_1"
#         print("开始插入")
#         cursor.execute(sql)
#         oraDb.commit()
#         print("插入执行完成", time.asctime())


# test3()


def do_batch(original_table,
             target_table, other_column, times=100, original_db='B2B_PYNER_UCFLOAN',
             target_db='B2B_PYNER_UCFLOAN_TEST'):
    id = 1
    for i in range(101, 1001):
        ref_index = id + i
        print("开始更新表 ref_index ", ref_index)
        sql_temp = "update " + str(original_db) + "." + str(original_table) + " set " + str(other_column) + " = " + str(
            ref_index)
        print("执行sql", sql_temp)
        cursor.execute(sql_temp)
        oraDb.commit()
        print("执行完成", time.asctime())
        sql = "INSERT INTO " + str(target_db) + "." + str(target_table) + " SELECT * FROM " + str(
            original_db) + "." + str(original_table)
        print("开始插入")
        cursor.execute(sql)
        oraDb.commit()
        print("插入执行完成", time.asctime())


def test_ucf():
    do_batch(original_table='UCF_TRADE_BID_INFO_EXTRA_1', target_table='UCF_TRADE_BID_INFO_EXTRA_1',
             other_column='MERCHANT_ID')
