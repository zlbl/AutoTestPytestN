# -*- coding:utf-8 -*-
from test.tob_xfd.enums.apiEnums import ApiEnums
from test.tob_xfd.enums.environmentEnums import EnvironmentEnums
import requests


def executeNoticeRecord():
    """
    2.执行「定时通知记录(上传也需执行)」
    上传对账文件（如果有需要下载的文件会一起下载，下载完成➡️Transferred） 上传成功➡️success
    """
    # 请求头
    headers = {
        'content-type': "application/json"
    }
    # 参数地址
    url = EnvironmentEnums.TEST_ZXXD_XFD_INNERAPI + ApiEnums.API_executeNoticeRecord

    # 发起请求
    r = requests.get(url=url, headers=headers)

    if r.status_code != 200:
        print("r.status_code is ", r.status_code)

    return r


def test_executeNoticeRecord():
    """
    测试「定时通知记录(上传也需执行)」
    """
    r = executeNoticeRecord()

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