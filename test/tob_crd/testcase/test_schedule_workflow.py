# -*- coding:utf-8 -*-
import requests
import time

sso_host = '192.168.5.158'
sso_port = '20187'
sso_login_uri = '/loan-sso/auth/ajaxLogin'
global token
token = ''

tob_audit_host = '192.168.5.156'
tob_audit_port = '8190'


def init_authoration():
    """
        TOB_产融贷获取token
    """
    params = {}
    params['username'] = 'loanAdmin'
    params['password'] = 'dashu0701'
    params['cne'] = \
        'vNQm0Ih-9hdLoHSYzeT2qQNKWY2rRw-LeTAKd9vZS68_VUtfLqyQeaRlilVerWmw'

    sso_api = 'http://' + sso_host + ':' + sso_port + sso_login_uri

    r = requests.post(sso_api, json=params)

    if r.status_code == 200:
        res_json = r.json()
        print('res_json is ', res_json)
        code = res_json['code']
        print('code is ', code)

        if code == '0':
            global token
            token = res_json['result']['token']
            print('token is ', token)
        else:
            raise Exception('sso login error authoration is none')


def setup_class():  # 这个类加载的时候会跑
    print('setup_class start')
    # 这里可以写一点初始化代码
    print('setup_class end')


def setup_module():  # pytest 自动会跑的方法
    print('setup_module start')
    init_authoration()
    print('setup_module end')

# 请求api接口
api = '/schedule/workflow'


def test_schedule_workflow():
    """
    TOB_执行工作流（额度申请，用款申请，提前还款申请，展期申请）
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }

    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api

    # for i in range(1, 2):
    i = 1
    while i <= 3:

        # 发起请求
        r = requests.post(url=url, headers=headers)

        if r.status_code == 200:
            res_json = r.json()
            print('响应值 is ', res_json)
            code = res_json['code']

            if code == 200:
                print('执行工作流成功')

            else:
                raise Exception('执行工作流异常', res_json['code'], ' msg is ',
                                res_json['errorMsg'])

        else:
            raise Exception('返回异常')
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        i += 1
        time.sleep(3)
