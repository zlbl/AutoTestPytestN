# -*- coding:utf-8 -*-
import requests
import time
import datetime

sso_host = '192.168.5.158'
sso_port = '20187'
sso_login_uri = '/loan-sso/auth/ajaxLogin'
global token
token = ''
global enterpriseId
enterpriseId = ''
global orderId0
orderId0 = ''
global orderId1
orderId1 = ''
global orderId2
orderId2 = ''
global orderId3
orderId3 = ''
global debtInfoId
debtInfoId = ''
global repayPlanId
repayPlanId = ''
global approvalId0
approvalId0 = ''
global approvalId1
approvalId1 = ''
global approvalId2
approvalId2 = ''
global approvalId3
approvalId3 = ''
global approvalId4
approvalId4 = ''
global approvalId5
approvalId5 = ''
global approvalId6
approvalId6 = ''
global approvalId7
approvalId7 = ''
global approvalId8
approvalId8 = ''
global approvalId9
approvalId9 = ''
global approvalId10
approvalId10 = ''
global approvalId11
approvalId11 = ''
global approvalId12
approvalId12 = ''
global approvalId13
approvalId13 = ''
global approvalId14
approvalId14 = ''
global approvalId15
approvalId15 = ''
global approvalId16
approvalId16 = ''
global approvalId17
approvalId17 = ''
global approvalId18
approvalId18 = ''
global approvalId19
approvalId19 = ''


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
                "propertyValue": "接口:%s" % str(int(time.time())),
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
api_info = '/innerapi/enterprise/info'


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
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_info

    # 发起请求
    r = requests.get(url=url, params=params, headers=headers)

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

    else:
        raise Exception('返回异常')

# 请求api接口
api_appapplyAmount = '/innerapi/order/applyAmount'

def test_order_applyAmount():
    """
    TOB_产融贷创建额度申请订单
    """
    # 获取额度有效期
    f1 = datetime.date.today()
    f2 = f1 + datetime.timedelta(days=365)
    # 转换时间戳
    f3 = int(time.mktime(f1.timetuple()))
    f4 = int(time.mktime(f2.timetuple()))
    # 秒级毫秒级转换
    f5 = int(round(f3 * 1000))
    f6 = int(round(f4 * 1000))

    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = dict(creditAmount=100, temporaryAmount=100, cycleAmount=100, expireTime=f6, validTime=f5,
                  debtorId=enterpriseId, merchantType="LoanEnterprise")
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_appapplyAmount

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('创建额度申请订单成功')
            global orderId0
            orderId0 = res_json['data']
            print('orderId0 is ', orderId0)

        else:
            raise Exception('创建额度申请订单异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_workflow = '/schedule/workflow'


def test_schedule_workflow():
    """
    TOB_执行工作流（额度申请，用款申请，提前还款申请，展期申请）
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }

    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_workflow

    # for i in range(1, 2):
    i = 1
    while i <= 2:

        # 发起请求
        r = requests.post(url=url, headers=headers)

        if r.status_code == 200:
            res_json = r.json()
            print('响应值 is ', res_json)
            code = res_json['code']

            if code == 200:
                print('执行工作流成功')

            else:
                raise Exception('执行工作流异常', res_json['code'], ' msg is ',
                                res_json['errorMsg'])

        else:
            raise Exception('返回异常')
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        i += 1
        time.sleep(2)



# 请求api接口
api_listByOrderId= '/innerapi/approval/listByOrderId'

def test_approval_listByOrderId():
    """
    TOB_产融贷审核记录查询
    """

    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        'orderId': orderId0
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_listByOrderId

    # 发起请求
    r = requests.post(url=url, params=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('审核记录查询成功')
            global approvalId0
            global approvalId1
            global approvalId2
            global approvalId3
            global approvalId4

            approvalId0 = res_json['data'][0]['approvalId']
            approvalId1 = res_json['data'][1]['approvalId']
            approvalId2 = res_json['data'][2]['approvalId']
            approvalId3 = res_json['data'][3]['approvalId']
            approvalId4 = res_json['data'][4]['approvalId']
            print('approvalId0 is ', approvalId0)
            print('approvalId1 is ', approvalId1)
            print('approvalId2 is ', approvalId2)
            print('approvalId3 is ', approvalId3)
            print('approvalId4 is ', approvalId4)

        else:
            raise Exception('审核记录查询异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do1 = '/innerapi/approval/do'


def test_approval_do1():
    """
    TOB_产融贷任务审批1
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params_approval = {
      "approvalId": approvalId0,
      "approvalResult": "Agree",
      "approvalDesc": "",
      "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do1

    # 发起请求
    r = requests.post(url=url, json=params_approval, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('总经理(杨生胜)审批成功')


        else:
            raise Exception('总经理(杨生胜)审批异常', res_json['code'], ' msg is ',
                       res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do2 = '/innerapi/approval/do'


def test_approval_do2():
    """
    TOB_产融贷任务审批2
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId1,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do2

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('财务总监(张自谦)审批成功')


        else:
            raise Exception('财务总监(张自谦)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do3 = '/innerapi/approval/do'


def test_approval_do3():
    """
    TOB_产融贷任务审批3
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId2,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do3

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('法务总监(杜秀丽)审批成功')


        else:
            raise Exception('法务总监(杜秀丽)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do4 = '/innerapi/approval/do'


def test_approval_do4():
    """
    TOB_产融贷任务审批4
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId3,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do4

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('风险总监(潘德鹏)审批成功')


        else:
            raise Exception('风险总监(潘德鹏)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do5 = '/innerapi/approval/do'


def test_approval_do5():
    """
    TOB_产融贷任务审批5
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId4,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do5

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('业务总监(付强)审批成功')


        else:
            raise Exception('业务总监(付强)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_workflow2 = '/schedule/workflow'


def test_schedule_workflow2():
    """
    TOB_执行工作流（额度申请，用款申请，提前还款申请，展期申请）
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }

    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_workflow2

    # for i in range(1, 2):
    i = 1
    while i <= 4:

        # 发起请求
        r = requests.post(url=url, headers=headers)

        if r.status_code == 200:
            res_json = r.json()
            print('响应值 is ', res_json)
            code = res_json['code']

            if code == 200:
                print('执行工作流成功')

            else:
                raise Exception('执行工作流异常', res_json['code'], ' msg is ',
                                res_json['errorMsg'])

        else:
            raise Exception('返回异常')
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        i += 1
        time.sleep(2)


# 请求api接口
api_applyBorrow = '/innerapi/order/applyBorrow'


def test_order_applyBorrow():
    """
    TOB_产融贷创建用款申请订单
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
      "contractNo": "合同编号测试:%s" % str(int(time.time())),
      "borrowAmount": 10,
      "periodUnit": "DAY",
      "repaymentType": "MONTH_REPAY_DAILY_INTEREST",
      "startInterestOffset": "0",
      "rateValue": "12",
      "overdueRateValue": "12",
      "accountType": "1",
      "accountName": "账户名称测试-1",
      "accountNo": "账户号码测试-1",
      "bankNo": "CCCB",
      "bankOrgnizeName": "开户机构测试-1",
      "issuer": "联行号测试-1",
      "periodValue": "88",
      "debtorId": enterpriseId,
      # "attachmentUsedList": "",
      "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_applyBorrow

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('创建用款申请订单成功')
            global orderId1
            orderId1 = res_json['data']
            print('orderId1 is ', orderId1)
        else:
            raise Exception('创建用款申请订单异常', res_json['code'], ' msg is ',
                       res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_workflow3 = '/schedule/workflow'


def test_schedule_workflow3():
    """
    TOB_执行工作流（额度申请，用款申请，提前还款申请，展期申请）
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }

    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_workflow3

    # for i in range(1, 2):
    i = 1
    while i <= 2:

        # 发起请求
        r = requests.post(url=url, headers=headers)

        if r.status_code == 200:
            res_json = r.json()
            print('响应值 is ', res_json)
            code = res_json['code']

            if code == 200:
                print('执行工作流成功')

            else:
                raise Exception('执行工作流异常', res_json['code'], ' msg is ',
                                res_json['errorMsg'])

        else:
            raise Exception('返回异常')
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        i += 1
        time.sleep(2)



# 请求api接口
api_listByOrderId2= '/innerapi/approval/listByOrderId'

def test_approval_listByOrderId2():
    """
    TOB_产融贷审核记录查询
    """

    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        'orderId': orderId1
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_listByOrderId2

    # 发起请求
    r = requests.post(url=url, params=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('审核记录查询成功')
            global approvalId5
            global approvalId6
            global approvalId7
            global approvalId8
            global approvalId9

            approvalId5 = res_json['data'][0]['approvalId']
            approvalId6 = res_json['data'][1]['approvalId']
            approvalId7 = res_json['data'][2]['approvalId']
            approvalId8 = res_json['data'][3]['approvalId']
            approvalId9 = res_json['data'][4]['approvalId']
            print('approvalId5 is ', approvalId5)
            print('approvalId6 is ', approvalId6)
            print('approvalId7 is ', approvalId7)
            print('approvalId8 is ', approvalId8)
            print('approvalId9 is ', approvalId9)

        else:
            raise Exception('审核记录查询异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do6 = '/innerapi/approval/do'


def test_approval_do6():
    """
    TOB_产融贷任务审批1
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params_approval = {
      "approvalId": approvalId5,
      "approvalResult": "Agree",
      "approvalDesc": "",
      "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do6

    # 发起请求
    r = requests.post(url=url, json=params_approval, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('总经理(杨生胜)审批成功')


        else:
            raise Exception('总经理(杨生胜)审批异常', res_json['code'], ' msg is ',
                       res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do7 = '/innerapi/approval/do'


def test_approval_do7():
    """
    TOB_产融贷任务审批2
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId6,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do7

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('财务总监(张自谦)审批成功')


        else:
            raise Exception('财务总监(张自谦)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do8 = '/innerapi/approval/do'


def test_approval_do8():
    """
    TOB_产融贷任务审批3
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId7,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do8

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('法务总监(杜秀丽)审批成功')


        else:
            raise Exception('法务总监(杜秀丽)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do9 = '/innerapi/approval/do'


def test_approval_do9():
    """
    TOB_产融贷任务审批4
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId8,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do9

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('风险总监(潘德鹏)审批成功')


        else:
            raise Exception('风险总监(潘德鹏)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do10 = '/innerapi/approval/do'


def test_approval_do10():
    """
    TOB_产融贷任务审批5
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId9,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do10

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('业务总监(付强)审批成功')


        else:
            raise Exception('业务总监(付强)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_workflow4 = '/schedule/workflow'


def test_schedule_workflow4():
    """
    TOB_执行工作流（额度申请，用款申请，提前还款申请，展期申请）
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }

    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_workflow4

    # for i in range(1, 2):
    i = 1
    while i <= 4:

        # 发起请求
        r = requests.post(url=url, headers=headers)

        if r.status_code == 200:
            res_json = r.json()
            print('响应值 is ', res_json)
            code = res_json['code']

            if code == 200:
                print('执行工作流成功')

            else:
                raise Exception('执行工作流异常', res_json['code'], ' msg is ',
                                res_json['errorMsg'])

        else:
            raise Exception('返回异常')
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        i += 1
        time.sleep(2)


# 请求api接口
api_getByEnterpriseId = '/innerapi/debtinfo/getByEnterpriseId'


def test_debtinfo_getByEnterpriseId():
    """
    TOB_产融贷根据企业ID获得企业的债权列表
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        'debtorId': enterpriseId
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_getByEnterpriseId

    # 发起请求
    r = requests.post(url=url, params=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('获得企业债权列表成功')
            global debtInfoId
            debtInfoId = res_json['data'][0]['debtInfoId']
            print('debtInfoId is ', debtInfoId)

        else:
            raise Exception('获得企业债权列表异常', res_json['code'], ' msg is ',
                       res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_offlinePay = '/innerapi/debtinfo/offlinePay'


def test_debtinfo_offlinePay():
    """
    TOB_产融贷线下放款
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
      "debtInfoId": debtInfoId,
      "payFinishTime": "",
      "merchantId": "100000000001",
      "merchantCode": "HLJZXXD",
      "productId": "100000000001",
      "productCode": "ZXXD_CRD",
      "applyNo": "",
      "amount": "0.01",
      "startTime": "",
      "endTime": ""
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_offlinePay

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('线下放款补录成功')

        else:
            raise Exception('线下放款补录异常', res_json['code'], ' msg is ',
                       res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_listRepayPlan = '/innerapi/repay/listRepayPlan'


def test_repay_listRepayPlan():
    """
    TOB_产融贷查询还款计划列表
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        'debtInfoId': debtInfoId
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_listRepayPlan

    # 发起请求
    r = requests.post(url=url, params=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('查询还款计划列表成功')
            global repayPlanId
            repayPlanId = res_json['data'][0]['repayPlanId']
            print('repayPlanId is ', repayPlanId)

        else:
            raise Exception('查询还款计划列表异常', res_json['code'], ' msg is ',
                       res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_applyRepayPart = '/innerapi/order/applyRepayPart'


def test_order_applyRepayPart():
    """
    TOB_产融贷创建提前还部分申请订单
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
      "debtInfoId": debtInfoId,
      "debtorId": enterpriseId,
      "repayInterest": 0,
      "repayPrincipal": 0.01,
      "repayArrears": "",
      "repayTime": "",
      "repayAmount": 0.01,
      "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_applyRepayPart

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('创建提前还部分申请订单成功')
            global orderId2
            orderId2 = res_json['data']
            print('orderId2 is ', orderId2)

        else:
            raise Exception('创建提前还部分申请订单异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_workflow5 = '/schedule/workflow'

def test_schedule_workflow5():
    """
    TOB_执行工作流（额度申请，用款申请，提前还款申请，展期申请）
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }

    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_workflow5

    # for i in range(1, 2):
    i = 1
    while i <= 2:

        # 发起请求
        r = requests.post(url=url, headers=headers)

        if r.status_code == 200:
            res_json = r.json()
            print('响应值 is ', res_json)
            code = res_json['code']

            if code == 200:
                print('执行工作流成功')

            else:
                raise Exception('执行工作流异常', res_json['code'], ' msg is ',
                                res_json['errorMsg'])

        else:
            raise Exception('返回异常')
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        i += 1
        time.sleep(2)


# 请求api接口
api_listByOrderId3 = '/innerapi/approval/listByOrderId'


def test_approval_listByOrderId3():
    """
    TOB_产融贷审核记录查询
    """

    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        'orderId': orderId2
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_listByOrderId3

    # 发起请求
    r = requests.post(url=url, params=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('审核记录查询成功')
            global approvalId10
            global approvalId11
            global approvalId12
            global approvalId13
            global approvalId14

            approvalId10 = res_json['data'][0]['approvalId']
            approvalId11 = res_json['data'][1]['approvalId']
            approvalId12 = res_json['data'][2]['approvalId']
            approvalId13 = res_json['data'][3]['approvalId']
            approvalId14 = res_json['data'][4]['approvalId']
            print('approvalId10 is ', approvalId10)
            print('approvalId11 is ', approvalId11)
            print('approvalId12 is ', approvalId12)
            print('approvalId13 is ', approvalId13)
            print('approvalId14 is ', approvalId14)

        else:
            raise Exception('审核记录查询异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do11 = '/innerapi/approval/do'


def test_approval_do11():
    """
    TOB_产融贷任务审批1
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params_approval = {
        "approvalId": approvalId10,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do11

    # 发起请求
    r = requests.post(url=url, json=params_approval, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('总经理(杨生胜)审批成功')


        else:
            raise Exception('总经理(杨生胜)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do12 = '/innerapi/approval/do'


def test_approval_do12():
    """
    TOB_产融贷任务审批2
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId11,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do12

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('财务总监(张自谦)审批成功')


        else:
            raise Exception('财务总监(张自谦)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do13 = '/innerapi/approval/do'


def test_approval_do13():
    """
    TOB_产融贷任务审批3
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId12,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do13

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('法务总监(杜秀丽)审批成功')


        else:
            raise Exception('法务总监(杜秀丽)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do14 = '/innerapi/approval/do'


def test_approval_do14():
    """
    TOB_产融贷任务审批4
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId13,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do14

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('风险总监(潘德鹏)审批成功')


        else:
            raise Exception('风险总监(潘德鹏)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do15 = '/innerapi/approval/do'


def test_approval_do15():
    """
    TOB_产融贷任务审批5
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId14,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do15

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('业务总监(付强)审批成功')


        else:
            raise Exception('业务总监(付强)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_workflow6 = '/schedule/workflow'


def test_schedule_workflow6():
    """
    TOB_执行工作流（额度申请，用款申请，提前还款申请，展期申请）
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }

    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_workflow6

    # for i in range(1, 2):
    i = 1
    while i <= 4:

        # 发起请求
        r = requests.post(url=url, headers=headers)

        if r.status_code == 200:
            res_json = r.json()
            print('响应值 is ', res_json)
            code = res_json['code']

            if code == 200:
                print('执行工作流成功')

            else:
                raise Exception('执行工作流异常', res_json['code'], ' msg is ',
                                res_json['errorMsg'])

        else:
            raise Exception('返回异常')
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        i += 1
        time.sleep(2)


# 请求api接口
api_doAdvanceRepayment = '/innerapi/repay/doAdvanceRepayment'


def test_repay_doAdvanceRepayment():
    """
    TOB_产融贷提前部分还款登记
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
      "debtInfoId": debtInfoId,
      "accountName": "提前部分还款登记账户名称1",
      "accountNo": "提前部分还款登记账号1",
      "offlineRechargeType": "Manual",
      "offlineRepayTime": "",
      "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_doAdvanceRepayment

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('提前部分还款登记成功')

        else:
            raise Exception('提前部分还款登记异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_applyContinue = '/innerapi/order/applyContinue'


def test_order_applyContinue():
    """
    TOB_产融贷创建部分展期申请订单
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
      "debtorId": enterpriseId,
      "debtInfoId": debtInfoId,
      "periodUnit": "DAY",
      "periodValue": "88",
      "repaymentType": "MONTH_REPAY_DAILY_INTEREST",
      "startInterestOffset": "0",
      "rateValue": "12",
      "overdueRateValue": "12",
      "continueAmount": 0.01,
      "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_applyContinue

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('创建部分展期申请订单成功')
            global orderId3
            orderId3 = res_json['data']
            print('orderId3 is ', orderId3)

        else:
            raise Exception('创建部分展期申请订单异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_workflow7 = '/schedule/workflow'

def test_schedule_workflow7():
    """
    TOB_执行工作流（额度申请，用款申请，提前还款申请，展期申请）
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }

    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_workflow7

    # for i in range(1, 2):
    i = 1
    while i <= 2:

        # 发起请求
        r = requests.post(url=url, headers=headers)

        if r.status_code == 200:
            res_json = r.json()
            print('响应值 is ', res_json)
            code = res_json['code']

            if code == 200:
                print('执行工作流成功')

            else:
                raise Exception('执行工作流异常', res_json['code'], ' msg is ',
                                res_json['errorMsg'])

        else:
            raise Exception('返回异常')
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        i += 1
        time.sleep(2)


# 请求api接口
api_listByOrderId4 = '/innerapi/approval/listByOrderId'


def test_approval_listByOrderId4():
    """
    TOB_产融贷审核记录查询
    """

    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        'orderId': orderId3
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_listByOrderId4

    # 发起请求
    r = requests.post(url=url, params=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('审核记录查询成功')
            global approvalId15
            global approvalId16
            global approvalId17
            global approvalId18
            global approvalId19

            approvalId15 = res_json['data'][0]['approvalId']
            approvalId16 = res_json['data'][1]['approvalId']
            approvalId17 = res_json['data'][2]['approvalId']
            approvalId18 = res_json['data'][3]['approvalId']
            approvalId19 = res_json['data'][4]['approvalId']
            print('approvalId15 is ', approvalId15)
            print('approvalId16 is ', approvalId16)
            print('approvalId17 is ', approvalId17)
            print('approvalId18 is ', approvalId18)
            print('approvalId19 is ', approvalId19)

        else:
            raise Exception('审核记录查询异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do16 = '/innerapi/approval/do'


def test_approval_do16():
    """
    TOB_产融贷任务审批1
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params_approval = {
        "approvalId": approvalId15,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do16

    # 发起请求
    r = requests.post(url=url, json=params_approval, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('总经理(杨生胜)审批成功')


        else:
            raise Exception('总经理(杨生胜)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do17 = '/innerapi/approval/do'


def test_approval_do17():
    """
    TOB_产融贷任务审批2
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId16,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do17

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('财务总监(张自谦)审批成功')


        else:
            raise Exception('财务总监(张自谦)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do18 = '/innerapi/approval/do'


def test_approval_do18():
    """
    TOB_产融贷任务审批3
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId17,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do18

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('法务总监(杜秀丽)审批成功')


        else:
            raise Exception('法务总监(杜秀丽)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do19 = '/innerapi/approval/do'


def test_approval_do19():
    """
    TOB_产融贷任务审批4
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId18,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do19

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('风险总监(潘德鹏)审批成功')


        else:
            raise Exception('风险总监(潘德鹏)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_do20 = '/innerapi/approval/do'


def test_approval_do20():
    """
    TOB_产融贷任务审批5
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
        "approvalId": approvalId19,
        "approvalResult": "Agree",
        "approvalDesc": "",
        "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_do20

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('业务总监(付强)审批成功')


        else:
            raise Exception('业务总监(付强)审批异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_workflow8 = '/schedule/workflow'


def test_schedule_workflow8():
    """
    TOB_执行工作流（额度申请，用款申请，提前还款申请，展期申请）
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }

    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_workflow8

    # for i in range(1, 2):
    i = 1
    while i <= 4:

        # 发起请求
        r = requests.post(url=url, headers=headers)

        if r.status_code == 200:
            res_json = r.json()
            print('响应值 is ', res_json)
            code = res_json['code']

            if code == 200:
                print('执行工作流成功')

            else:
                raise Exception('执行工作流异常', res_json['code'], ' msg is ',
                                res_json['errorMsg'])

        else:
            raise Exception('返回异常')
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        i += 1
        time.sleep(2)


# 请求api接口
api_offlineRepay = '/innerapi/repay/offlineRepay'

def test_repay_offlineRepay():
    """
    TOB_产融贷还款登记（人工入账）
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
      "debtInfoId": debtInfoId,
      "repayPlanId": repayPlanId,
      "periodIndex": 1,
      "accountNo": "还款登记账号-1",
      "accountName": "还款登记账户名称-1",
      "repayAmount": 0.01,
      "offlineRechargeType": "Manual",
      "transaction": "",
      "offlineRepayTime": "",
      "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_offlineRepay

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('线下还款登记人工入账成功')

        else:
            raise Exception('线下还款登记人工入账异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


# 请求api接口
api_applyRepayAll = '/innerapi/order/applyRepayAll'

def test_order_applyRepayAll():
    """
    TOB_产融贷创建提前结清申请订单
    """
    # 请求头
    headers = {
        'content-type': "application/json",
        'Authorization': token

    }
    # 参数变量
    params = {
      "debtInfoId": debtInfoId,
      "debtorId": enterpriseId,
      "repayTime": "",
      "repayAmount": "",
      "repayArrears": "",
      "repayInterest": 0,
      "repayPrincipal": "",
      "merchantType": "LoanEnterprise"
    }
    # 参数地址
    url = "http://api.loan.test.hljzxxd.com/gateway" + api_applyRepayAll

    # 发起请求
    r = requests.post(url=url, json=params, headers=headers)

    if r.status_code == 200:
        res_json = r.json()
        print('响应值 is ', res_json)
        code = res_json['code']

        if code == 200:
            print('创建提前结清申请订单成功')

        else:
            raise Exception('创建提前结清申请订单异常', res_json['code'], ' msg is ',
                            res_json['errorMsg'])

    elif r.status_code == 400:
        res_json = r.json()
        print(res_json['errorMsg'])

    else:
        raise Exception('返回异常')


