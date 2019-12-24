#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests

#信审-回调任务地址
tob_audit_host = '192.168.5.159'
tob_audit_port = '8082'
tob_audit_uri = '/audit/task/callBackJob'

def setup_class():  # 这个类加载的时候会跑
    print('setup_class start')
    # 这里可以写一点初始化代码
    print('setup_class end')

#回调任务-消费贷审核完成通知接口
def test_callBackJob():

    #请求地址
    test_callBackJob_api = 'http://' + tob_audit_host + ':' + tob_audit_port + tob_audit_uri

    r = requests.get(test_callBackJob_api)

    if r.status_code == 200:
        print('处理成功')
    else:
        raise Exception('返回异常')

#main函数
if __name__ == '__main__':
    test_callBackJob()

