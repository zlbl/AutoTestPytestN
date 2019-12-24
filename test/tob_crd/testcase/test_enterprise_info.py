# -*- coding:utf-8 -*-
import requests
import time

sso_host = '192.168.5.158'
sso_port = '20187'
sso_login_uri = '/loan-sso/auth/ajaxLogin'
global token
token = ''
global enterpriseId
enterpriseId = ''

tob_audit_host = '192.168.5.156'
tob_audit_port = '8190'


def init_authoration():
    """
        TOB_产融贷获取token
    """
    params = {}
    params['username'] = 'loanAdmin'
    params['password'] = 'dashu0701'
    params['cne'] = \
        'vNQm0Ih-9hdLoHSYzeT2qQNKWY2rRw-LeTAKd9vZS68_VUtfLqyQeaRlilVerWmw'

    sso_api = 'http://' + sso_host + ':' + sso_port + sso_login_uri

    r = requests.post(sso_api, json=params)

    if r.status_code == 200:
        res_json = r.json()
        print('res_json is ', res_json)
        code = res_json['code']
        print('code is ', code)

        if code == '0':
            global token
            token = res_json['result']['token']
            print('token is ', token)
        else:
            raise Exception('sso login error authoration is none')


def setup_class():  # 这个类加载的时候会跑
    print('setup_class start')
    # 这里可以写一点初始化代码
    print('setup_class end')


def setup_module():  # pytest 自动会跑的方法
    print('setup_module start')
    init_authoration()
    print('setup_module end')

# 请求api接口
api_create = '/innerapi/enterprise/create'


def test_enterprise_create():
    """
    TOB_产融贷创建企业信息
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }

    # 参数变量
    params = {
        "enterpriseId": "",
        "enterpriseName": "接口测试:%s" % str(int(time.time())),
        "enterpriseCode": "接口测试:%s" % str(int(time.time())),
        "contactName": "接口:%s" % str(int(time.time())),
        "contactMobile": "18212342222",
        "groupNumber": "",
        "propertyValueList": [
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "1",
                "propertyName": "",
                "propertyType": "java.lang.String",
                "propertyCode": "merchantId",
                "propertyValue": "100000000001",
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            },
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "1",
                "propertyName": "",
                "propertyType": "java.lang.String",
                "propertyCode": "productId",
                "propertyValue": "100000000001",
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            },
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "1",
                "propertyName": "企业编号",
                "propertyType": "java.lang.String",
                "propertyCode": "enterpriseCode",
                "propertyValue": "接口测试:%s" % str(int(time.time())),
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            },
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "1",
                "propertyName": "企业名称",
                "propertyType": "java.lang.String",
                "propertyCode": "enterpriseName",
                "propertyValue": "接口测试:%s" % str(int(time.time())),
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            },
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "1",
                "propertyName": "法人代表姓名",
                "propertyType": "java.lang.String",
                "propertyCode": "representativeName",
                "propertyValue": "接口:%s" % str(int(time.time())),
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            },
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "1",
                "propertyName": "证件类型",
                "propertyType": "java.lang.String",
                "propertyCode": "representativeIdType",
                "propertyValue": "idCard",
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            },
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "1",
                "propertyName": "证件号码",
                "propertyType": "java.lang.String",
                "propertyCode": "representativeIdNumber",
                "propertyValue": "356712190210231457",
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            },
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "1",
                "propertyName": "证件有效期",
                "propertyType": "java.lang.String",
                "propertyCode": "personValidTime",
                "propertyValue": "349804800000",
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            },
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "1",
                "propertyName": "证件有效期",
                "propertyType": "java.lang.String",
                "propertyCode": "personExpireTime",
                "propertyValue": "长期",
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            },
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "3",
                "propertyName": "证件形式",
                "propertyType": "java.lang.String",
                "propertyCode": "paperType",
                "propertyValue": "ThreeCertificatesInOne",
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            },
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "3",
                "propertyName": "营业执照号码",
                "propertyType": "java.lang.String",
                "propertyCode": "paperCode",
                "propertyValue": "1234567890",
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            },
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "3",
                "propertyName": "证件有效期",
                "propertyType": "java.lang.String",
                "propertyCode": "paperValidTime",
                "propertyValue": "665856000000",
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            },
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "3",
                "propertyName": "证件有效期",
                "propertyType": "java.lang.String",
                "propertyCode": "paperExpireTime",
                "propertyValue": "长期",
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            },
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "2",
                "propertyName": "联系人姓名",
                "propertyType": "java.lang.String",
                "propertyCode": "contactName",
                "propertyValue": "接口",
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            },
            {
                "propertyValueId": "",
                "debtorId": "",
                "groupNumber": "2",
                "propertyName": "手机号码",
                "propertyType": "java.lang.String",
                "propertyCode": "contactMobile",
                "propertyValue": "16712340987",
                "propertyDesc": "",
                "status": "",
                "extend": "false"
            }
        ],
        "attachmentUsedList": [
            {
                "attachUsedId": "",
                "attachmentId": "",
                "attachmentCode": "licenceFile",
                "attachmentName": "营业执照",
                "originalFileName": "清分记录清分服务费显示异常.png",
                "businessType": "Enterprise",
                "businessValue": "",
                "createTime": ""
            }
        ],
        "merchantId": "100000000001",
        "merchantName": "中新小贷",
        "merchantType": "LoanEnterprise",
        "productId": "100000000001",
        "productName": "产融贷"
    }


    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_create

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('企业创建成功')
            global enterpriseId
            enterpriseId = res_json['data']
            print('enterpriseId is ', enterpriseId)

        else:
            raise Exception('企业创建异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])
    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])
    else:
        raise Exception('返回异常')


# 请求api接口
api = '/innerapi/enterprise/info'


def test_enterprise_info():
    """
    TOB_产融贷查询企业信息
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        'enterpriseId': enterpriseId
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api

    # 发起请求
    r = requests.get(url=url, params=params, headers=headers)

    try:
        if r.status_code == 200:
            res_json = r.json()
            print('响应值 is ', res_json)
            code = res_json['code']

            if code == 200:
                print('查询企业信息成功')

            else:
                raise Exception('查询企业信息异常', res_json['code'], ' msg is ',
                           res_json['errorMsg'])

        elif r.status_code == 400:
            res_json = r.json()
            print(res_json['errorMsg'])

    except Exception as e:
        print(e)
