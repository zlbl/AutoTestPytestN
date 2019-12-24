#!/usr/bin/python3
# -*- coding:utf-8 -*-
import datetime

import requests
import hashlib
import time

token_url = 'https://open.sobot.com/open/platform/getAccessToken.json'
zhichi_appId = '4a64916122d44eb6987e13e3266fd103'
zhichi_appKey = 'sY72221LE50q'
zhichi_createTime = '1569571051'
zhichi_sign = zhichi_appId + zhichi_appKey + zhichi_createTime
zhichi_sign_md5 = '68108c0a993ae813ffdfffc258da89f3'

customer_message_url = 'https://open.sobot.com/open/platform/api.json'


def get_md5(str):
    b = str.encode('utf')
    m = hashlib.md5()
    str_md5 = m.hexdigest()
    print()
    print('MD5加密前为 ：' + str)
    print()
    print('MD5加密后为 ：' + str_md5)

    return str_md5


def http_get_gettoken():
    """
    测试http get请求
    """
    headers = {}
    # headers['Auth'] = 'aaaaaaaaa'  # 测试用

    ticks = time.time()
    int_ticks = int(round(ticks * 1000))
    print('当前时间戳： ', int_ticks)

    params = {}
    params['appId'] = zhichi_appId  # 测试用参数
    params['appKey'] = zhichi_appKey  # 测试用参数
    params['createTime'] = zhichi_createTime  # 自1970年1月1日0时起至今的毫秒数
    # params['sign'] = get_md5(zhichi_sign)  # 签名（appId,appKey,createTime以字符串方式拼接后经过MD5加密）
    params['sign'] = zhichi_sign_md5  # 签名（appId,appKey,createTime以字符串方式拼接后经过MD5加密）

    print('访问的地址是：', token_url)
    print('传递参数为：', params)

    # params就是普通的url后加参数的方式
    r = requests.get(
        url=token_url, params=params, headers=headers)
    print('返回状态status code：', r.status_code)
    print('返回结果：', r.text)
    # print('r\'s json is ', r.json)
    return ''


def http_get_offline_data():
    # {
    #     "action": "wb_export_open_data",
    #     "access_token": "b075eb5b33cf4a8ca29816eaf3e456b7",
    #     "data": {
    #         "companyId": "d44257ee428448e3bfc147fa0ca82bab",
    #         "taskType": 2,
    #         "date": "2018-02-03"
    #     }
    # }
    headers = {}
    # headers['Auth'] = 'aaaaaaaaa'  # 测试用

    params_data = {}
    params_data['companyId'] = 'd44257ee428448e3bfc147fa0ca82bab'
    params_data['taskType'] = 2
    params_data['date'] = '2018-02-03'

    params = {}
    params['action'] = 'wb_export_open_data'  # 测试用参数
    params['access_token'] = 'b075eb5b33cf4a8ca29816eaf3e456b7'  # 测试用参数
    params['data'] = params_data  # 测试用参数

    print('params is :', params)
    r = requests.post('https://open.sobot.com/open/platform/api.json', json=params, headers=headers)
    print('返回的结果是: ', r.json)
    print('返回的结果是: ', r.text)
    return r.text


def http_post_():
    """
    测试http post请求
    """
    headers = {}
    # headers['access_token'] = 'aaaaaaaaa'  # 测试用

    params = {}
    params['action'] = 'wb_session_customer'  # 传值为"wb_session_customer"
    params['access_token'] = 'wb_session_customer'  # 调用接口凭据

    # params就是普通的url后加参数的方式
    # r = requests.post(
    # url='http://www.baidu.com', params=params, headers=headers)

    r = requests.post(
        url=customer_message_url, json=params, headers=headers)
    print('r\'s status code is ', r.status_code)
    print('r\'s text is ', r.text)
    print('r\'s json is ', r.json)


def test_http_get_gettoken():
    print(http_get_gettoken())


def test_http_get_offline_data():
    day = -603
    days = 90
    # 现在的时间
    now = datetime.datetime.now()
    # 100天前的时间
    endnow = now + datetime.timedelta(days=-603)
    # 六天后的时间转换成字符串
    endnow = str(endnow.strftime('%Y-%m-%d'))

    print(endnow)
    # ret_text = http_get_offline_data()

def test_main():
    print('1')
