# -*- coding:utf-8 -*-

class getAuditJob_params :
    """
    audit 信审队列参数
    """
    orderId = ""
    sysUserId = ""
    auditStatus = ""
    jobFrom = "消费贷"
    pageNumber = "10"
    pageSize = "20"

class business_params:
    """
    个人业务统计参数
    """

    pageSize = "1"
    pageNumber = "1"
    total = "1"

class listPersonalHistory_params :
    """
    当前信审员历史完成订单参数
    """
    pageNumber = "10"
    pageSize = "10"

class handleOrderResult_params :
    """
    订单处理参数
    """
    orderId = "251736201944678400"
    flag = "1"
    remark = "备注订单"