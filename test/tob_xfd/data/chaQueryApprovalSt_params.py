# -*- coding:utf-8 -*-

"""
TOB_订单状态查询数据
"""
class xfd_chaQueryApprovalSt_params:

    #存在的订单
    params_success = {
        "apiVersion": "1.1",
        "nonce_str": "123456",
        "productCode": "01",
        "applyNo": "XFD_applyNo_1543848196201"
    }

    #不存在的订单
    params_fail_repeat = {
        "apiVersion": "1.1",
        "nonce_str": "123456",
        "productCode": "01",
        "applyNo": "XFD_applyNo_no_1543832764152"
    }
