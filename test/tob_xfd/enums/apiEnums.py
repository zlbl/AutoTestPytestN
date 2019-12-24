# -*- coding:utf-8 -*-

class ApiEnums:
    # 订单相关API
    API_accessToken = "/openapi/accessToken"
    API_consumeApply = "/openapi/consume/apply"
    API_getMerchantBalance = "/openapi/consume/getMerchantBalance"
    API_cancelOrder = "/openapi/consume/cancelOrder"
    API_chaQueryApprovalSt = "/openapi/consume/chaQueryApprovalSt"
    API_modifyBankCard = "/openapi/consume/modifyBankCard"

    # 功夫贷的接口地址
    API_access_token = "/openapi/access_token"
    API_chaApply = "/openapi/message/chaApply"

    # 支付放款 定时任务相关API
    API_workflow = "/schedule/workflow"
    API_paygateway = "/schedule/paygateway"
    API_createClarifyRecord = "/schedule/createClarifyRecord"
    API_autoExecuteClarifyRecord = "/schedule/autoExecuteClarifyRecord"
    API_regulatoryAgencyNotice = "/schedule/regulatoryAgencyNotice"

    # 文件上传下载、通知执行定时任务
    API_createFtpNoticeRecordTask = "/schedule/createFtpNoticeRecordTask"
    API_executeNoticeRecord = "/schedule/executeNoticeRecord"
    API_processTransferredNoticeRecord = "/schedule/processTransferredNoticeRecord"
    API_processTransferringNoticeRecord = "/schedule/processTransferringNoticeRecord"

    # 债权相关接口
    API_onlinePay = "/openapi/consume/debtinfo/onlinePay"

    # 信审回调接口
    API_auditOrderResult = "/audit/order/result"