# -*- coding:utf-8 -*-
import time

t = time.time()
curTimeStamp = int(round(t * 1000))

class xfd_consumeApply_Params:
    """
    TOB_消费贷用款申请参数
    """
    params_success ={
        #"accessToken": "vJg4p7K22yEq/BZbHEMtdJDMzxQK/kuD6p8ObDj13VM=",
        #"openid": "71C019B632CB53F7149975C370205ED3",
        #"merchantCode": "HZS170921000015",
        "version": "1.5",
        "applyNo": "DASHU_XFD_applyNo_"+str(curTimeStamp),
        "nonceStr": "123456",
        #"sign": "{{sign}}",
        "productCode": "02",  # 02  test_saasId_02
        "contractNo": "contractNo_XFD_"+str(curTimeStamp),
        "recordDesc": "",
        "careerCode": "JS",
        "maxDegreeCode": "BK",
        "marryCode": "YW",
        "applyPeopleRequest": {
            "customerName": "吴苗苗",
            "customerTypeCode": "YB",
            "mobile": "15222716837",
            "papersNo": "130984199007164224",
            "papersTypeCode": "SF",
            "isAllowCredit": "N",
            "merchantProductUserId": "130984199007164224",
            "applicantRelationship": "ZJ",
            "applyPepleTypeCode": "ZS",
            "careerCode": "JS",
            "maxDegreeCode": "BK",
            "marryCode": "YW",
            "propertyValueList": [
                {
                    "groupNumber": "1",
                    "propertyName": "结婚",
                    "propertyCode": "careerCode",
                    "propertyValue": "QT",
                    "propertyDesc": "1"
                }, {
                    "groupNumber": "2",
                    "propertyName": "结婚2",
                    "propertyCode": "marryCode",
                    "propertyValue": "WH",
                    "propertyDesc": "2"
                }
            ]
        },
        "applyAccountRequest": {
            "accountType": "1",
            "accountNo": "6217710809498249",
            "accountName": "吴苗苗",
            "bankNo": "CNCB",
            "acUsCd": "FK",
            "acBankNa": "中信银行",
            "acCd": "JS",
            "acCuCd": "RMB",
            "papersNo": "130984199007164224",
            "papersTypeCode": "SF"
        },
        "applyAmountRequest": {
            "applyNo": "DASHU_XFD_applyNo_"+str(curTimeStamp),
            "productCode": "02",  # 02  test_saasId_02
            "borrowAmount": 1,
            "periodValue": "6",
            "rateUnit": "MONTH",
            "repaymentType": "EmptyEqualPI",
            "computeInterestUnit": "MONTH",
            "currency": "RMB",
            "orderType": "PersonalBorrow",
            "firstPayAmount": "0.01",
            "goodsBuyAmount": "0.01",
            "rateValue": 0.13,
            "loanUseCode": "XF",
            "loanUseExplain": "消费",
            "extendParams": {
                "rateType": "F",
                "repayMode": "DEBX",
                "bankNo": "CNCB",
                "overdueGraceOffset": "0",
                "intCalPer": "GDTS",
                "perProYn": "y",
                "currency": "RMB",
                "repayQrequency": "03",
                "loanType": "XJ",
                "intCalBaCd": "SY"
            }
        }
    }

class gfd_consumeApply_Params:
    """
    TOB_功夫贷用款申请参数
    """
    params_success = {
        "apiVersion": "1.5",
        "applyNo": "DASHU_GFD_applyNo_"+str(curTimeStamp),
        "client_id": "HZS170921000015",
        "nonce_str": "123456",
        "recordContent": "{\"applyNo\":\"DASHU_GFD_applyNo_"+str(curTimeStamp)+"\",\"applyPeopleRequest\":{\"applicantRelationship\":\"ZJ\",\"applyPepleTypeCode\":\"ZS\",\"customerName\":\"吴苗苗\",\"customerTypeCode\":\"YB\",\"isAllowCreditInquiries\":\"N\",\"mobileNo\":\"15222716837\",\"papersNo\":\"130984199007164224\",\"papersTypeCode\":\"SF\"},\"applyPeopleSubRequest\":{\"careerCode\":\"QT\",\"marryCode\":\"WH\",\"maxDegreeCode\":\"QT\"},\"applyRequest\":{\"loanTypeNo\":\"01\",\"loanUseCode\":\"XF\",\"loanUseExplain\":\"消费\"},\"applySubRequest\":{\"applayAmount\":0.01,\"applyPeriodLength\":6,\"firstPayAmount\":0.00,\"goodsBuyAmount\":0.01,\"yearRate\":0.13},\"extendParams\":{\"rate_type\":\"F\",\"repay_mode\":\"DEBX\",\"bank_code\":\"CNCB\",\"grace_day\":\"0\",\"int_cal_per\":\"GDTS\",\"per_pro_yn\":\"y\",\"currency\":\"RMB\",\"repay_grequency\":\"03\",\"loan_type\":\"XJ\",\"int_cal_ba_cd\":\"SY\"},\"imageRequest\":[{\"fileUrl\":\"http://jira.treefinance.com.cn/s/ksvhcn/712001/0671383139659647b34518c21f4bc41a/1.0/_/includes/jquery/plugins/fancybox/fancybox-x.png\",\"imageItemCode\":\"A1\"},{\"fileUrl\":\"https://www.91gfd.com.cn/loan-thirdparty/zxxd/download/DASHU_2018101809510449712519022/02\",\"imageItemCode\":\"A2\"},{\"fileUrl\":\"http://jira.treefinance.com.cn/s/ksvhcn/712001/0671383139659647b34518c21f4bc41a/_/jira-logo-scaled.png\",\"imageItemCode\":\"A3\"}],\"prodId\":\"01\",\"repaymentAccountRequest\":{\"acBankNa\":\"中信银行\",\"acCd\":\"JS\",\"acCuCd\":\"RMB\",\"acNa\":\"吴苗苗\",\"acNo\":\"6217710809498249\",\"acTyCd\":\"GR\",\"acUsCd\":\"FK\"}}"
    }