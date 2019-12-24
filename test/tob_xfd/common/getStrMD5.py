# -*- coding:utf-8 -*-
import hashlib

"""
TOB_对字符串进行加密
"""
def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    print(m.hexdigest())
    return m.hexdigest()


def md5GBK(str1):
    m = hashlib.md5(str1.encode(encoding='gb2312'))
    print(m.hexdigest())
    return m.hexdigest()


