import requests
import json


def get_token(url):
    params = {
        "projectCode": "CONSUMELOAN_CLOAN",
        "projectSecret": "6b579baf610bbcba4dec0c1f224ca42922c1346d43da78f9b71b7b702b141cdb"
    }

    headers = {
        'content-type': "application/json"
    }

    payload = json.dumps(params, ensure_ascii=False)
    response = requests.request("POST", url, data=payload, headers=headers)
    content = json.loads(response.text, encoding='utf-8')

    print(content['token'])
    return content['token']
