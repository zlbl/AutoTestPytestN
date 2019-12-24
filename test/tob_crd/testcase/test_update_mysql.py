# -*- coding:utf-8 -*-
import pymysql

global PAY_RECORD_ID
PAY_RECORD_ID = ''
global CONTRACT_NO
CONTRACT_NO = ''
global PAY_TRADE_ORDER_ID
PAY_TRADE_ORDER_ID = ''


def test_select_payRecord():
    """
    通过字段DEBT_INFO_ID
    在债权中心放款记录表b2b_loan_debtinfo.t_b2b_debt_pay_record
    查找线上放款字段PAY_TRADE_ORDER_ID
    """

    db = pymysql.connect(host='192.168.5.94', user='root', passwd='123456', db='b2b_loan_debtinfo', port=3306, charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 定义执行的查询sql
    sql = "SELECT *FROM b2b_loan_debtinfo.t_b2b_debt_pay_record WHERE DEBT_INFO_ID = '258269150705926144' "

    # 使用 execute()  方法执行SQL查询
    cursor.execute(sql)

    # 使用 fetchone() 方法获取单条数据
    results = cursor.fetchone()

    # 打印一条数据
    print('响应值 is ', results)
    global PAY_RECORD_ID
    global CONTRACT_NO
    global PAY_TRADE_ORDER_ID
    PAY_RECORD_ID = results[0]
    CONTRACT_NO = results[3]
    PAY_TRADE_ORDER_ID = results[12]
    # 打印结果
    print("PAY_RECORD_ID=%s,CONTRACT_NO=%s,PAY_TRADE_ORDER_ID=%s" % \
          (PAY_RECORD_ID, CONTRACT_NO, PAY_TRADE_ORDER_ID))

    # 定义执行的更新sql
    sql = """UPDATE `b2b_loan_paygateway`.`t_b2b_pay_trade_order` SET `TRADE_STATUS` = 3, `TRADE_MESSAGE` = '成功' WHERE `PAY_TRADE_ORDER_ID` = PAY_TRADE_ORDER_ID;"""
    # sql = "UPDATE b2b_loan_paygateway.t_b2b_pay_trade_order SET TRADE_STATUS = 3 WHERE PAY_TRADE_ORDER_ID = PAY_TRADE_ORDER_ID "

    # 使用 execute()  方法执行SQL
    results = cursor.execute(sql)

    # 对操作进行提交
    db.commit()

    # 打印一条数据
    print('响应值 is ', results)

    # 定义执行的更新sql
    sql = """UPDATE `b2b_loan_paygateway`.`t_b2b_pay_trade_task` SET `TASK_TYPE` = 1 WHERE `PAY_TRADE_ORDER_ID` = PAY_TRADE_ORDER_ID;"""

    # 使用 execute()  方法执行SQL
    results = cursor.execute(sql)

    # 对操作进行提交
    db.commit()

    # 打印一条数据
    print('响应值 is ', results)

    # 关闭数据库连接
    db.close()
    return results

