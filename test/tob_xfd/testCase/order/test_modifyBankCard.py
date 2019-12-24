# -*- coding:utf-8 -*-
from test.tob_xfd.common.getMergeParams import getMergeParams
from test.tob_xfd.data.modifyBankCard_params import xfd_modifyBankCard_params
from test.tob_xfd.enums.apiEnums import ApiEnums
from test.tob_xfd.enums.environmentEnums import EnvironmentEnums
import requests


def modifyBankCard(params):
    """
    修改银行卡，并返回结果
    """
    # 请求头
    headers = {
        'content-type': "application/json"
    }
    # 参数地址
    url = EnvironmentEnums.TEST_ZXXD_XFD_OPENAPI + ApiEnums.API_modifyBankCard

    # 参数加签
    params = getMergeParams(params)

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code != 200:
        print("r.status_code is ", r.status_code)

    return r

def test_modifyBankCard():
    """
    测试「修改银行卡」修改银行卡接口
    """
    # 获取加签的参数，并请求
    r = modifyBankCard(xfd_modifyBankCard_params.params_success)

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