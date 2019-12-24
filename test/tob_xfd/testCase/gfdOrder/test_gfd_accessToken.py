# -*- coding:utf-8 -*-
import urllib
from test.tob_xfd.enums.environmentEnums import EnvironmentEnums
from test.tob_xfd.data.accessToken_params import gfd_accessToken_params
from test.tob_xfd.enums.apiEnums import ApiEnums
import requests

def gfd_accessToken(params):
    """
    TOB_功夫贷获取令牌返回值
    """
    # 请求头
    headers = {
        'content-type': "application/x-www-form-urlencoded"
    }
    # 参数地址
    url = EnvironmentEnums.TEST_ZXXD_XFD_OPENAPI + ApiEnums.API_access_token

    # 参数变量
    params = params
    params = urllib.parse.urlencode(params)

    # 发起请求
    r = requests.post(url=url, data=params, headers=headers)

    if r.status_code != 200:
        print("r.status_code is ", r.status_code)

    return r


def test_gfd_accessToken():
    """
    TOB_功夫贷获取令牌接口测试
    """
    r = gfd_accessToken(gfd_accessToken_params.params_ZXXD)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['username']

        if code == gfd_accessToken_params.params_ZXXD['client_id']:
            print('处理成功')

        else:
            raise Exception('后台处理异常', res_json['code'], ' msg is ',
                            res_json['msg'])
    else:
        raise Exception('返回异常')