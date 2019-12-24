# -*- coding:utf-8 -*-
from test.tob_xfd.common.getMergeParams import getMergeParams
from test.tob_xfd.data.getMerchantBalance_params import xfd_getMerchantBalance_params
from test.tob_xfd.enums.apiEnums import ApiEnums
from test.tob_xfd.enums.environmentEnums import EnvironmentEnums
import requests


def getMerchantBalance(params):
    """
    查询余额，并返回结果
    """
    # 请求头
    headers = {
        'content-type': "application/json"
    }
    # 参数地址
    url = EnvironmentEnums.TEST_ZXXD_XFD_OPENAPI + ApiEnums.API_getMerchantBalance

    # 参数加签
    params = getMergeParams(params)

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code != 200:
        print("r.status_code is ", r.status_code)

    return r


def test_getMerchantBalance():
    """
    测试查询余额接口
    """
    # 获取加签的参数，并请求
    r = getMerchantBalance(xfd_getMerchantBalance_params.params_success)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('处理成功')
        elif code == -1:
            print(' code is ',res_json['code'], ' msg is ', res_json['errorMsg'])
        else:
            raise Exception('后台处理异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])
    else:
        raise Exception('返回异常')
