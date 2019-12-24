# -*- coding:utf-8 -*-
from test.tob_xfd.common.getMergeParams import getMergeParams
from test.tob_xfd.common.getSQLResult import getOrderInfoByApplyNo, getFlowInstanceByOrderId, \
    getFlowInstanceProcessByInstanceId, getOrderApprovalByOrderId
from test.tob_xfd.data.chaQueryApprovalSt_params import xfd_chaQueryApprovalSt_params
from test.tob_xfd.data.consumeApply_Params import xfd_consumeApply_Params
from test.tob_xfd.data.onlinePay_params import xfd_onlinePay_params
from test.tob_xfd.enums.environmentEnums import EnvironmentEnums
from test.tob_xfd.testCase.order.test_chaQueryApprovalSt import chaQueryApprovalSt
from test.tob_xfd.testCase.order.test_consumeApply import consumeApply
from test.tob_xfd.enums.apiEnums import ApiEnums
from test.tob_xfd.testCase.schedule.test_workflow import workflow
import time
import requests
#定义全局变量申请单号
APPLYNO = ''

def onlinePay(params):
    """
    放款，并返回结果
    """
    # 请求头
    headers = {
        'content-type': "application/json"
    }
    # 参数地址
    url = EnvironmentEnums.TEST_ZXXD_XFD_OPENAPI + ApiEnums.API_onlinePay

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code != 200:
        print("r.status_code is ", r.status_code)

    return r

def auditResult(params):

    # 请求头
    headers = {
        'content-type': "application/json"
    }
    # 参数地址
    url = EnvironmentEnums.TEST_ZXXD_XFD_INNERAPI + ApiEnums.API_auditOrderResult

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code != 200:
        print("r.status_code is ", r.status_code)

    return r

def test_onlinePay():
    """
    测试放款
    1.用款申请，获取到applyNo
    2.审批流2次，信审回调,继续审批,orderStatus=3,生成债权
    3.判断一下订单是否审批完成，调用如下方法chaQueryApprovalSt(),orderStatus=3,生成债权
    4.进行放款
    5.修改支付网关的数据b2b_loan_paygateway（t_b2b_pay_trade_order.trade_status=3、t_b2b_pay_trade_task.task_type=1&execute_status=3）
    6.调用网关的定时任务
    """
    # 1.用款申请，获取到applyNo
    r_consumeApply = consumeApply(xfd_consumeApply_Params.params_success)
    global APPLYNO, orderID
    APPLYNO = r_consumeApply.json()['data']['applyNo']
    print("APPLYNO:"+APPLYNO)

    # 2.1 执行审批流
    i = 1
    while i <= 4:
        workflow()
        i += 1
        time.sleep(1)
    # 2.2 查询订单ID
    results = getOrderInfoByApplyNo(APPLYNO)
    orderID = results[0]
    print("orderID:" + str(orderID))
    # 2.3 根据orderId查询工作流
    results = getFlowInstanceByOrderId(orderID)
    instanceId = results[0]
    print("instanceId:" + str(instanceId))
    # 2.4 查询工作流进程 和 订单审批信息
    results = getFlowInstanceProcessByInstanceId(instanceId)
    audResult = getOrderApprovalByOrderId(orderID)
    approvalId = audResult[0]
    print("approvalId:" + str(approvalId))
    if results is not None:
        # 2.5 回调信审接口
        auditResultParams = {
            "orderId": approvalId,
            "flag": "1",
            "remake": "测试通过"
        }
        auditResult(auditResultParams)
        # 2.6 继续审批
        j = 1
        while j <= 4:
            workflow()
            j += 1
            time.sleep(1)
        # 查询订单的状态
        # xfd_chaQueryApprovalSt_params.params_success['applyNo'] = APPLYNO
        # r = chaQueryApprovalSt(xfd_chaQueryApprovalSt_params.params_success)
        results = getOrderInfoByApplyNo(APPLYNO)
        orderStatus = results[4]
        # 判断订单状态，如果是3就可以放款
        if orderStatus == 3:
            xfd_onlinePay_params.params_success['applyNo'] = APPLYNO
            # 获取加签的参数
            params = getMergeParams(xfd_onlinePay_params.params_success)
            # 放款
            r = onlinePay(params)
            if r.status_code == 200:
                res_json = r.json()
                print('响应值 is ', res_json)
                if res_json['errorMsg'] == "":
                    code = res_json['code']

                    if code == 200:
                        print('处理成功')

                    else:
                        raise Exception('后台处理异常', res_json['code'], ' msg is ',
                                        res_json['msg'])
            else:
                raise Exception('返回异常')
        else:
            print("错误")
    else:
        print("错误")
