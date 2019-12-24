# -*- coding:utf-8 -*-

"""
TOB_取消订单接口
"""
class xfd_cancelOrder_params:

    #成功取消数据
    params_success = {
        "apiVersion": "1.1",
        "nonce_str": "123456",
        "productCode": "02"
        #"applyNo": "XFD_applyNo_1543848196201"
    }

    #重复取消数据
    params_fail_repeat = {
        "apiVersion": "1.1",
        "nonce_str": "123456",
        "productCode": "01",
        "applyNo": "XFD_applyNo_1543832764152"
    }

def get_params_success(params,applyNo):
    params['applyNo'] = applyNo