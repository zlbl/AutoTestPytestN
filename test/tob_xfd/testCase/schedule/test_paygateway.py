# -*- coding:utf-8 -*-
from test.tob_xfd.enums.apiEnums import ApiEnums
from test.tob_xfd.enums.environmentEnums import EnvironmentEnums
import requests

def paygateway():
    """
    执行支付网关（支付/放款「功夫贷」）
    """
    # 请求头
    headers = {
        'content-type': "application/json"
    }
    # 参数地址
    url = EnvironmentEnums.TEST_ZXXD_XFD_INNERAPI + ApiEnums.API_paygateway

    # 发起请求
    r = requests.get(url=url, headers=headers)

    if r.status_code != 200:
        print("r.status_code is ", r.status_code)

    return r

def test_paygateway():
    """
    测试支付定时任务
    """

    r = paygateway()

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