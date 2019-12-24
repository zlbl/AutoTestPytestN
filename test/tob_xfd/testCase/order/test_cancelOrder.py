# -*- coding:utf-8 -*-
from test.tob_xfd.common.getMergeParams import getMergeParams
from test.tob_xfd.data.cancelOrder_params import xfd_cancelOrder_params
from test.tob_xfd.data.consumeApply_Params import xfd_consumeApply_Params
from test.tob_xfd.enums.apiEnums import ApiEnums
from test.tob_xfd.enums.environmentEnums import EnvironmentEnums
import requests

from test.tob_xfd.testCase.order.test_consumeApply import consumeApply


def getCancelOrder(params):
    """
    取消订单，并返回结果
    """
    # 请求头
    headers = {
        'content-type': "application/json"
    }
    # 参数地址
    url = EnvironmentEnums.TEST_ZXXD_XFD_OPENAPI + ApiEnums.API_cancelOrder

    # 参数加签
    params = getMergeParams(params)

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code != 200:
        print("r.status_code is ", r.status_code)

    return r


def test_getCancelOrder():
    """
    取消订单：
    1.先创建订单
    2.取消上面新创建的订单
    """
    # 1.获取加签的参数（用款申请）
    consumeApply_Params = xfd_consumeApply_Params.params_success
    global APPLYNO
    APPLYNO = consumeApply_Params['applyNo']
    print("APPLYNO:"+APPLYNO)
    r_consumeApply = consumeApply(consumeApply_Params)
    print(r_consumeApply.json())

    # 2.获取加签的参数(取消订单参数)
    # applyNo = r_consumeApply.json()['data']['applyNo']
    xfd_cancelOrder_params.params_success['applyNo'] = APPLYNO
    r = getCancelOrder(xfd_cancelOrder_params.params_success)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('处理成功')
        else:
            raise Exception('后台处理异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])
    else:
        raise Exception('返回异常')


def test_getCancelOrder_Fail_repeat():
    """
    重复取消订单
    """
    r = getCancelOrder(xfd_cancelOrder_params.params_fail_repeat)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == -1:
            print('处理结果:'+res_json['errorMsg'])
        else:
            raise Exception('后台处理异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])
    else:
        raise Exception('返回异常')