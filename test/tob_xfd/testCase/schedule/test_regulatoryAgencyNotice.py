# -*- coding:utf-8 -*-
from test.tob_xfd.enums.apiEnums import ApiEnums
from test.tob_xfd.enums.environmentEnums import EnvironmentEnums
import requests


def regulatoryAgencyNotice():
    """
    执行「监管查账数据」定时任屋
    """
    # 请求头
    headers = {
        'content-type': "application/json"
    }
    # 参数地址
    url = EnvironmentEnums.TEST_ZXXD_XFD_INNERAPI + ApiEnums.API_workflow

    # 发起请求
    r = requests.get(url=url, headers=headers)

    if r.status_code != 200:
        print("r.status_code is ", r.status_code)

    return r


def test_regulatoryAgencyNotice():
    """
    测试「监管查账数据」定时任屋
    """
    r = regulatoryAgencyNotice()

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