#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import pymysql

# 信审地址
tob_audit_host = '192.168.5.159'
tob_audit_port = '8082'
tob_audit_uri = '/audit/add'


def setup_class():  # 这个类加载的时候会跑
    print('setup_class start')
    # 这里可以写一点初始化代码
    print('setup_class end')


def setup_module():  # pytest 自动会跑的方法
    print('setup_module start')
    print('setup_module end')


# 增加订单
def test_add():

    # 请求参数
    params = {
        "orderId": "3308211011",
        "userId": "0",
        "userName": "大树",
        "contractAmount": "6000.00",
        "period": "6",
        "orderCreateTime": "2018-12-07T10:30:17+0800",
        "merchantType": "fe5d90f57c768f47da80c15ef497a5d7",
        "jobFrom": "f1915ea2184c606e335ea030fccceb6b",
        "saasId": "300000000001"
    }

    # 请求地址
    add_api = 'http://' + tob_audit_host + ':' + tob_audit_port + tob_audit_uri

    r = requests.post(add_api, json=params)

    if r.status_code == 200:
        res_json = r.json()
        print('res_json is ', res_json)
        status = res_json['status']

        if status == True:
            print('处理成功')

        else:
            raise Exception('后台处理异常', res_json['code'], ' msg is ',
                            res_json['msg'])
    else:
        raise Exception('返回异常')

    # 数据库连接
    # 打开数据库
    db = pymysql.connect(
        host='121.43.177.8',
        user='dingzhaoyun',
        passwd='0EERv9DVpS',
        db='tob_audit',
        port=3344,
        charset='utf8')
    # 使用cursor()方法创建一个游标对象
    cursor = db.cursor()
    # 定义查询
    sql_select = "delete from audit_job where order_id=" + params['orderId']
    # 使用execute()方法执行查询
    cursor.execute(sql_select)
    db.commit()

    # main函数
    if __name__ == '__main__':
        test_add()
