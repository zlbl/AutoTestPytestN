# -*- coding:utf-8 -*-
from test.tob_xfd.common.getMergeParams import getMergeParams
from test.tob_xfd.enums.environmentEnums import EnvironmentEnums
from test.tob_xfd.data.consumeApply_Params import xfd_consumeApply_Params
from test.tob_xfd.enums.apiEnums import ApiEnums
import requests


def consumeApply(params):
    """
    用款申请，并返回结果
    """
    # 请求头
    headers = {
        'content-type': "application/json"
    }
    # 参数地址
    url = EnvironmentEnums.TEST_ZXXD_XFD_OPENAPI + ApiEnums.API_consumeApply

    # 请求参数加签
    params = getMergeParams(params)

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code != 200:
        print("r.status_code is ", r.status_code)

    return r


def test_consumeApply():
    """
    用款接口测试
    """
    r = consumeApply(xfd_consumeApply_Params.params_success)

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
