#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util.common.dubbo.dubboclient2 import dubbo

global dubbo_client2




# 这里用到了fixture的知识，不懂？去看一下那部分的说明
def setup_module(module):
    """
    模块初始化，初始化dubbo客户端
    :param module:
    :return:
    """
    zk_ip = '192.168.5.241'
    zk_port = '2181'
    # 全局变量，用于后面测试用例使用
    global dubbo_client2
    dubbo_client2 = dubbo(zk_ip, zk_port)
    # 设定连接超时时间
    dubbo_client2.set_connect_timeout(1000)  # 单位秒
    # 设定响应的编码
    dubbo_client2.set_encoding('gbk')


def test_invoke_get_all_ding_department():
    """
    测试invoke方法
    """
    # 定义dubbo接口叫什么
    interface = 'com.treefinance.loan.gateway.dingtalk.facade'
    # 定义接口里的方法叫什么
    method = 'getAllDingDepartments'
    # 如果没有参数就写空字符串
    param = ''
    global dubbo_client2
    print('result', dubbo_client2.invoke(interface, method, param))


def teardown_module(module):
    """
    这个模块的测试用例跑完之后，用这个方法把连接关掉
    """