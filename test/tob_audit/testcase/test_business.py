#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-

from test.tob_audit.data.auditParams import business_params
import requests
import time

sso_host = '192.168.5.158'
sso_port = '20187'
sso_login_uri = '/loan-sso/auth/ajaxLogin'
global token
token = ''

tob_audit_host = '192.168.5.159'
tob_audit_port = '8082'
tob_audit_interface = '/audit/business'


def init_authoration():
    params = {}
    params['username'] = '丁昭云'
    params['password'] = 'Dashu0701'
    params[
        'cne'] = 'BnOfFHDqWVz4x98zY3twmeFTAs18ILt7a51CDgLYhJHvG4gteAK6MivNos4RNrtx'

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
    time.sleep(1)
    print('setup_module end')

def test_business():
    """
    个人业务统计
    """
    #请求头
    headers = {}
    headers["Authorization"] = token

    #参数变量
    params = {
        'pageSize': business_params.pageSize,
        'pageNumber' : business_params.pageNumber,
        'total' : business_params.total
    }

    audit_business_api = 'http://' + tob_audit_host + ':' + tob_audit_port + tob_audit_interface

    #发起请求
    r = requests.post(url=audit_business_api,json=params,headers = headers)

    if r.status_code == 200:
        res_json = r.json()
        code = res_json['code']

        if code == 0:
            print('处理成功')

        else:
            raise Exception('后台处理异常',res_json['code'],'msg is',res_json['msg'])
    else:
        raise Exception('返回异常')






