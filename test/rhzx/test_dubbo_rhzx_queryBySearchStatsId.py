#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util.common.dubbo.dubboclient import dubbo


global uid_dubbo_service_conn
import json

# 这里用到了fixture的知识，不懂？去看一下那部分的说明
def setup_module(module):
    """
    模块初始化，初始化dubbo客户端
    :param module:
    :return:
    """
    uid_dubbo_service_ip = '10.112.162.127'
    uid_dubbo_service_port = '20300'
    # 全局变量，用于后面测试用例使用
    global uid_dubbo_service_conn
    uid_dubbo_service_conn = \
        dubbo(uid_dubbo_service_ip, uid_dubbo_service_port)
    # 设定连接超时时间
    uid_dubbo_service_conn.set_connect_timeout(1000)  # 单位秒
    # 设定响应的编码
    uid_dubbo_service_conn.set_encoding('gbk')



def test_rhzx_queryBySearchStatsId():
    """
    测试invoke方法
    """
    # 定义dubbo接口叫什么
    interface = 'com.treefinance.risk.thirdparty2.CreditReportService'
    # 定义接口里的方法叫什么
    method = 'queryBySearchStatsId'
    # 如果有多个参数这样写
    # OperatorDTO createOperator(OperatorDTO operatorDTO);

    searchStatsId = 376422259214303232
    # 转成字符串，如果有多个对象，就像普通对象一样，添加多个，比如
    # json.dumps(operatorDTO) + ',' +
    # json.dumps(operatorDTO2) + ',12121212121212'

    res_data = uid_dubbo_service_conn.invoke(interface, method, searchStatsId)
    print('res_data is ', res_data)


def teardown_module(module):
    """
    这个模块的测试用例跑完之后，用这个方法把连接关掉
    """


if __name__ == "__main__":
    pass
