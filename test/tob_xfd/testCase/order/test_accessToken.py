# -*- coding:utf-8 -*-
from test.tob_xfd.common.getSign import getSign
from test.tob_xfd.enums.environmentEnums import EnvironmentEnums
from test.tob_xfd.data.accessToken_params import xfd_accessToken_params
from test.tob_xfd.enums.apiEnums import ApiEnums
import requests

def accessToken(params):
    """
    TOB_消费贷获取令牌返回值
    """
    # 请求头
    headers = {
        'content-type': "application/json"
    }
    # 参数地址
    url = EnvironmentEnums.TEST_ZXXD_XFD_OPENAPI + ApiEnums.API_accessToken

    # 参数变量
    params = params

    merchantKey = params['merchantKey']
    del params['merchantKey']
    # 对参数进行加签
    sign = getSign(params, merchantKey)

    params['sign'] = sign

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    params['merchantKey'] = merchantKey
    del params['sign']

    if r.status_code != 200:
        print("r.status_code is ", r.status_code)

    return r


def test_accessToken():
    """
    TOB_消费贷获取令牌接口测试
    """
    r = accessToken(xfd_accessToken_params.params_ZXXD)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('处理成功')

        else:
            raise Exception('后台处理异常', res_json['code'], ' msg is ',
                            res_json['msg'])
    else:
        raise Exception('返回异常')

def test_getSign():
    params={
        "access_token": "0NrF9uUaACx8Yhv9oFpXZvgN27ud1BZ6ZkoBMtqEQW0=",
        "refresh_token": "084A004D4DF96A7498B92286D8E8F077",
        "openid": "06E6088FEF63B4928581BE296A3E560B",
        "apiVersion": "1.5",
        "applyNo": "DASHU_2018121110",
        "client_id": "HZS170921000015",
        "nonce_str": "123456",
        "recordContent": "{\"applyNo\":\"DASHU_2018121110\",\"applyPeopleRequest\":{\"applicantRelationship\":\"ZJ\",\"applyPepleTypeCode\":\"ZS\",\"customerName\":\"吴苗苗\",\"customerTypeCode\":\"YB\",\"isAllowCreditInquiries\":\"N\",\"mobileNo\":\"15222716837\",\"papersNo\":\"130984199007164224\",\"papersTypeCode\":\"SF\"},\"applyPeopleSubRequest\":{\"careerCode\":\"QT\",\"marryCode\":\"WH\",\"maxDegreeCode\":\"QT\"},\"applyRequest\":{\"loanTypeNo\":\"01\",\"loanUseCode\":\"XF\",\"loanUseExplain\":\"消费\"},\"applySubRequest\":{\"applayAmount\":0.01,\"applyPeriodLength\":6,\"firstPayAmount\":0.00,\"goodsBuyAmount\":0.01,\"yearRate\":0.13},\"extendParams\":{\"rate_type\":\"F\",\"repay_mode\":\"DEBX\",\"bank_code\":\"CNCB\",\"grace_day\":\"0\",\"int_cal_per\":\"GDTS\",\"per_pro_yn\":\"y\",\"currency\":\"RMB\",\"repay_grequency\":\"03\",\"loan_type\":\"XJ\",\"int_cal_ba_cd\":\"SY\"},\"imageRequest\":[{\"fileUrl\":\"http://jira.treefinance.com.cn/s/ksvhcn/712001/0671383139659647b34518c21f4bc41a/1.0/_/includes/jquery/plugins/fancybox/fancybox-x.png\",\"imageItemCode\":\"A1\"},{\"fileUrl\":\"https://www.91gfd.com.cn/loan-thirdparty/zxxd/download/DASHU_2018101809510449712519022/02\",\"imageItemCode\":\"A2\"},{\"fileUrl\":\"http://jira.treefinance.com.cn/s/ksvhcn/712001/0671383139659647b34518c21f4bc41a/_/jira-logo-scaled.png\",\"imageItemCode\":\"A3\"}],\"prodId\":\"01\",\"repaymentAccountRequest\":{\"acBankNa\":\"中信银行\",\"acCd\":\"JS\",\"acCuCd\":\"RMB\",\"acNa\":\"吴苗苗\",\"acNo\":\"6217710809498249\",\"acTyCd\":\"GR\",\"acUsCd\":\"FK\"}}"
    }
    merchantKey="DASHU_f53a9f4c-e708-4556-8979-da021090f0b5"

    sign=getSign(params, merchantKey)
    print("加签结果："+sign)