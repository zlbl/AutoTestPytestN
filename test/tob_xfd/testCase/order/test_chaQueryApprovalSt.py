# -*- coding:utf-8 -*-
from test.tob_xfd.common.getMergeParams import getMergeParams
from test.tob_xfd.data.chaQueryApprovalSt_params import xfd_chaQueryApprovalSt_params
from test.tob_xfd.enums.environmentEnums import EnvironmentEnums
from test.tob_xfd.data.consumeApply_Params import xfd_consumeApply_Params
from test.tob_xfd.enums.apiEnums import ApiEnums
import requests

from test.tob_xfd.testCase.order.test_consumeApply import consumeApply
global applyNo
applyNo = ''


def chaQueryApprovalSt(params):
    """
    取消订单，并返回结果
    """
    # 请求头
    headers = {
        'content-type': "application/json"
    }
    # 参数地址
    url = EnvironmentEnums.TEST_ZXXD_XFD_OPENAPI + ApiEnums.API_chaQueryApprovalSt

    #参数加签
    params = getMergeParams(params)

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code != 200:
        print("r.status_code is ", r.status_code)

    return r


def test_chaQueryApprovalSt():
    """
    查询订单状态（存在的订单）
    1.用款申请（新订单）
    2.查询上面申请订单状态
    """
    # 1.获取加签的参数（用款申请）
    r_consumeApply = consumeApply(xfd_consumeApply_Params.params_success)
    print(r_consumeApply.json())

    if r_consumeApply.json()['errorMsg'] == "":
        # 2.获取加签的参数(查询订单状态)
        applyNo = r_consumeApply.json()['data']['applyNo']
        xfd_chaQueryApprovalSt_params.params_success['applyNo'] = applyNo
        r = chaQueryApprovalSt(xfd_chaQueryApprovalSt_params.params_success)

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
    else:
        print(r_consumeApply.json()['errorMsg'])

"""
查询订单状态（不存在的订单）
"""
def test_chaQueryApprovalSt_Fail_repeat():
    """
    查询订单状态（不存在的订单）
    """

    # 获取不存在的订单参数，并加密
    # params = getMergeParams(xfd_chaQueryApprovalSt_params.params_fail_repeat)
    r = chaQueryApprovalSt(xfd_chaQueryApprovalSt_params.params_fail_repeat)

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
