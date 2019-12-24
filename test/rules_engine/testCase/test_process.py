import json
import allure
import requests

from config import config as C
from test.rules_engine.common.getToken import get_token

"""
获取共用的token
"""
tokenUrl = 'http://' + C.RULE_HOST + ':' + C.RULE_PORT + '/token/get'
token = get_token(tokenUrl)

"""
被测接口的url
"""
getInputParamsUrl = 'http://' + C.RULE_HOST + ':' + C.RULE_PORT + '/process/getInputParams'
runProcessUrl = 'http://' + C.RULE_HOST + ':' + C.RULE_PORT + '/process/run'


def common(method, url, params):
    headers = {
        'content-type': "application/json",
        'Authorization': token
    }
    payload = json.dumps(params, ensure_ascii=False)

    response = requests.request(method=method, url=url, data=payload, headers=headers)
    if response.status_code != 200:
        print("response.status_code is ", response.status_code)

    return response


def test_getInputParams_success():
    params = {
        "name": "loan_approve",
        "project": "CONSUMELOAN_CLOAN"
    }
    response = common("post", getInputParamsUrl, params)

    assert response.status_code == 200


def test_getInputParams_errorParamValue():
    params = {
        "name": "",
        "project": "CONSUMELOAN_CLOAN"
    }
    response = common("post", getInputParamsUrl, params)

    assert response.status_code == 500


def test_runProcess_success():
    params = {
        "name": "loan_approve",
        "session": {
            "approveResult": "Agree",
            "approveInput": "0"

        },
        "project": "CONSUMELOAN_CLOAN",
        "batchId": 123
    }
    response = common("post", runProcessUrl, params)

    assert response.status_code == 200


def test_runProcess_refuse():
    params = {
        "name": "loan_approve",
        "session": {
            "approveResult": "Refuse",
            "approveInput": "2"

        },
        "project": "CONSUMELOAN_CLOAN",
        "batchId": 123
    }
    response = common("post", runProcessUrl, params)
    result = json.loads(response.text, encoding='utf-8')

    assert result['otherResultMap']['approveResult'] == 'Refuse'


def test_runProcess_agree():
    params = {
        "name": "loan_approve",
        "session": {
            "approveResult": "Agree",
            "approveInput": "0"

        },
        "project": "CONSUMELOAN_CLOAN",
        "batchId": 123
    }
    response = common("post", runProcessUrl, params)
    result = json.loads(response.text, encoding='utf-8')

    assert result['otherResultMap']['approveResult'] == 'Agree'


def test_runProcess_artificial():
    params = {
        "name": "loan_approve",
        "session": {
            "approveResult": "Artificial",
            "approveInput": "1"

        },
        "project": "CONSUMELOAN_CLOAN",
        "batchId": 123
    }
    response = common("post", runProcessUrl, params)
    result = json.loads(response.text, encoding='utf-8')

    assert result['otherResultMap']['approveResult'] == 'Artificial'


def test_runProcess_errorName():
    params = {
        "name": "***",
        "session": {
            "approveResult": "Agree",
            "approveInput": "0"
        },
        "project": "CONSUMELOAN_CLOAN",
        "batchId": 123
    }
    response = common("post", runProcessUrl, params)

    assert response.status_code == 500
