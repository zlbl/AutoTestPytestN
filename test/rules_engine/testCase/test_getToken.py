import requests
import json
import allure
from config import config as C

"""
被测接口的url
"""
url = 'http://' + C.RULE_HOST + ':' + C.RULE_PORT + '/token/get'


def common(method, params):
    headers = {
        'content-type': "application/json"
    }
    payload = json.dumps(params, ensure_ascii=False)

    response = requests.request(method=method, url=url, data=payload, headers=headers)
    if response.status_code != 200:
        print("response.status_code is ", response.status_code)

    return response


def test_success():
    params = {
        "projectCode": "CONSUMELOAN_CLOAN",
        "projectSecret": "6b579baf610bbcba4dec0c1f224ca42922c1346d43da78f9b71b7b702b141cdb"
    }
    response = common("post", params)

    assert response.status_code == 200


def test_tokenIsNone():
    params = {
        "projectCode": "CONSUMELOAN_CLOAN",
        "projectSecret": ""
    }
    response = common("post", params)
    result = json.loads(response.text, encoding='utf-8')

    assert result["token"] == None


def test_notExistValue():
    params = {
        "projectCode": "CONSUMELOAN",
        "projectSecret": ""
    }
    response = common("post", params)
    result = json.loads(response.text, encoding='utf-8')

    assert result["token"] == None
