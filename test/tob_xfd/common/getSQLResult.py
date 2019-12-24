# -*- coding:utf-8 -*-
import pymysql

from test.tob_xfd.data.dataSource_params import dataSource_params
from test.tob_xfd.util.DbUtil import DbUtil

hostname = dataSource_params.hostname
username = dataSource_params.username
passWord = dataSource_params.password
port = dataSource_params.port

def getOrderInfoByApplyNo(applyNo):
    """
    通过applyNo获取到订单信息
    :param applyNo:
    :return:
    """
    # 初始化连接参数
    xfd_db_b2b_loan_order = DbUtil(hostname,username,passWord,"b2b_loan_order",port)
    xfd_db_b2b_loan_order.open_connect()

    # 要执行的sql
    sql = "select * from b2b_loan_order.t_b2b_loan_order where apply_no =\'"+applyNo+"\'"

    results = xfd_db_b2b_loan_order.find_one(sql)
    xfd_db_b2b_loan_order.close_connect()
    return results

    """
    修改模版
    """
    # # 打开数据库连接
    # db = pymysql.connect(host='192.168.5.94', user='root', passwd='123456', db='b2b_loan_order', port=3306,charset='utf8')
    # # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    # # SQL 更新语句
    # sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
    # try:
    #     # 执行SQL语句
    #     cursor.execute(sql)
    #     # 提交到数据库执行
    #     db.commit()
    # except:
    #     # 发生错误时回滚
    #     db.rollback()
    #
    # # 关闭数据库连接
    # db.close()

    return results

def getFlowInstanceByOrderId(orderId):
    """
    通过orderId获取工作流信息
    :param orderId:
    :return:
    """
    # 打开数据库连接
    xfd_db_b2b_loan_workflow = DbUtil(hostname,username,passWord, 'b2b_loan_workflow', port)
    xfd_db_b2b_loan_workflow.open_connect()

    # 定义执行的sql
    sql = "select * from b2b_loan_workflow.t_b2b_flow_instance where BIZ_SOURCE_VALUE =" + str(orderId)

    results = xfd_db_b2b_loan_workflow.find_one(sql)
    xfd_db_b2b_loan_workflow.close_connect()
    return results

def getFlowInstanceProcessByInstanceId(instanceId):
    """
    通过instanceId获取工作流进程信息
    :param instanceId:
    :return:
    """
    # 初始化连接参数
    xfd_db_b2b_loan_workflow = DbUtil('192.168.5.94','root','123456',"b2b_loan_workflow",port)
    xfd_db_b2b_loan_workflow.open_connect()

    # 要执行的sql
    sql1 = "select * from b2b_loan_workflow.t_b2b_flow_instance_process where INSTANCE_ID =\'"+str(instanceId)+"\' and node_type=\'Task\'"

    results = xfd_db_b2b_loan_workflow.find_one(sql1)
    xfd_db_b2b_loan_workflow.close_connect()
    return results

def getOrderApprovalByOrderId(orderId):
    """
    通过订单id查询订单信审的审批信息
    :param orderId:
    :return:
    """
    # 初始化连接参数
    xfd_db_b2b_loan_order = DbUtil('192.168.5.94','root','123456',"b2b_loan_order",port)
    xfd_db_b2b_loan_order.open_connect()

    # 要执行的sql
    sql = "select * from b2b_loan_order.t_b2b_loan_order_approval where ORDER_ID=\'"+str(orderId)+"\'"

    results = xfd_db_b2b_loan_order.find_one(sql)
    xfd_db_b2b_loan_order.close_connect()
    return results

def test_sql():
    results1 = getOrderInfoByApplyNo("DASHU_XFD_applyNo_1544602374290")
    print("测试流程ID:"+str(results1[0]))
    results = getFlowInstanceByOrderId("257873024924303360")
    print("测试流程ID:"+str(results[0]))
    # orderId = 22222
    # sql = "select * from b2b_loan_workflow.t_b2b_flow_instance where BIZ_SOURCE_VALUE =" + str(orderId)
    # print("测试流程ID:"+sql)





