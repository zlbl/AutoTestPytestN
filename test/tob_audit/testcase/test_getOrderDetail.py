#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import time
#导入pymysql模块，要先安装pip3 install PyMySQL
import pymysql

#登录地址
sso_host = '192.168.5.158'
sso_port = '20187'
sso_login_uri = '/loan-sso/auth/ajaxLogin'
global token
token = ''

#信审地址
tob_audit_host = '192.168.5.159'
tob_audit_port = '8082'
tob_audit_uri = '/audit/getOrderDetail'

#登录
def init_authoration():
    #请求参数
    params = {}
    params['username'] = '曹燕'
    params['password'] = 'caoyan1'
    params['cne'] = \
        "BnOfFHDqWVz4x98zY3twmeFTAs18ILt7a51CDgLYhJFNmMqq3XcTr4J9KYeVBVQZ"

    #请求地址
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
            raise Exception('sso login error Authorization is none')

def setup_class():  # 这个类加载的时候会跑
    print('setup_class start')
    # 这里可以写一点初始化代码
    print('setup_class end')


def setup_module():  # pytest 自动会跑的方法
    print('setup_module start')
    init_authoration()   #执行登录
    time.sleep(10)         #等待时间
    print('setup_module end')

#获取订单详情
def test_getOrderDetail():
    #请求头
    headers = {}
    headers['Authorization'] = token
    headers['Content-Type'] = "application/x-www-form-urlencoded"
    print('headers is ', headers)

    #数据库连接
    #打开数据库
    db = pymysql.connect(host='121.43.177.8', user='dingzhaoyun', passwd='0EERv9DVpS', db='tob_audit', port=3344, charset='utf8')
    #使用cursor()方法创建一个游标对象
    cursor = db.cursor()
    #定义查询
    sql_select = "select * from audit_job where user_name='吴苗苗' and contract_amount='1.00' order by create_time desc limit 0,1"
    #使用execute()方法执行查询
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for row in results:
        order_id = row[1]
    #打印查询结果
    print("user_id=%s" %order_id)

    #请求参数
    params = {
        "orderId":order_id
    }

    #请求地址
    getOrderDetail_api = 'http://' + tob_audit_host + ':' + tob_audit_port + tob_audit_uri

    r = requests.post(getOrderDetail_api, params=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('res_json is ', res_json)
        code = res_json['code']

        if code == 0:
            print('处理成功')

        else:
            raise Exception('后台处理异常', res_json['code'], ' msg is ',
                            res_json['msg'])
    else:
        raise Exception('返回异常')

#main函数
    if __name__ == '__main__':
        test_getOrderDetail()


