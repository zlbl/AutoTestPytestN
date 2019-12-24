#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import html2text as ht
import tomd

base_url = 'https://tower.im/api/v1'

acces_token = '53c16b9eaedd36b7198dae0e28c1c5dfe4d4a2859ec55f028beece7117c3ab5b'
refresh_token = 'f17c10a965ca4cc8582236887216a650e6c7ba6d6ff58192732251807843386a'
client_id = '6ca63981bbcbce5142469c87d840b6ac31c3aee3c0ef397e9cb76ba4fcf06729'
client_secret = 'ca1307b08f0680237cb4c5118f7fb9db167afcb7169258d40d381dcab755f422'
redirect_uri = 'https://tower.datatrees.com.cn/callback'

token_type = 'Bearer'
authorization = token_type + acces_token


def test_get_tower_code():
    """
           授权码获取
           """
    headers = {}
    # headers['Auth'] = 'aaaaaaaaa'  # 测试用

    params = {}
    params['client_id'] = client_id  # 测试用参数
    params['client_secret'] = client_secret  # 测试用参数
    params['response_type'] = 'authorization_code'  # 测试用参数
    params['redirect_uri'] = 'https://tower.datatrees.com.cn/callback'  # 测试用参数

    # params就是普通的url后加参数的方式
    r = requests.get(
        url='https://tower.im/oauth/authorize', params=params, headers=headers)
    print('r\'s status code is ', r.status_code)
    print('r\'s text is ', r.text)
    print('r\'s json is ', r.json)


def test_get_tower_token():
    """
        获取tower token
        """
    headers = {}
    # headers['Auth'] = 'aaaaaaaaa'  # 测试用

    params = {}
    params['client_id'] = client_id  # 测试用参数
    params['client_secret'] = client_secret  # 测试用参数
    params['code'] = '219a2075a8a5a45c252a65c9b905287867c5a6b70f57849cfc882d01bb5431e5'  # 测试用参数
    params['grant_type'] = 'authorization_code'  # 测试用参数
    params['redirect_uri'] = redirect_uri

    # params就是普通的url后加参数的方式
    r = requests.post(
        url='https://tower.im/oauth/token', params=params, headers=headers)
    print('r\'s status code is ', r.status_code)
    print('r\'s text is ', r.text)
    print('r\'s json is ', r.json)


def test_refresh_tower_token():
    """
            刷新tower token
            """

    headers = {}
    headers['Authorization'] = token_type + acces_token  # 测试用

    params = {}
    params['client_id'] = client_id  # 测试用参数
    params['client_secret'] = client_secret  # 测试用参数
    params['grant_type'] = 'refresh_token'  # 测试用参数
    params['redirect_uri'] = redirect_uri  # 测试用参数
    params['refresh_token'] = refresh_token  # 测试用参数

    # params就是普通的url后加参数的方式
    r = requests.post(
        url='https://tower.im/oauth/token', params=params, headers=headers)
    print('r\'s status code is ', r.status_code)
    print('r\'s text is ', r.text)
    print('r\'s json is ', r.json)


def test_get_current_user_info():
    """
    获取当前账号信息
    :return:
    """
    headers = {}
    headers['Authorization'] = authorization  # 测试用

    params = {}
    # params['client_id'] = '6ca63981bbcbce5142469c87d840b6ac31c3aee3c0ef397e9cb76ba4fcf06729'  # 测试用参数

    url = base_url + '/user'
    print('url is ', url)

    # params就是普通的url后加参数的方式
    r = requests.get(
        url=url, params=params, headers=headers)
    print('r\'s status code is ', r.status_code)
    print('r\'s text is ', r.text)
    print('r\'s json is ', r.json)


def test_export_as_md():
    'https://tower.im/documents/3f67c8199276a22963a0fde8fc18c690/exports'
    """
        获取当前账号信息
        :return:
        """
    headers = {}
    # headers['Authorization'] = acces_token  # 测试用

    params = {}
    params['access_token'] = acces_token

    url = base_url + '/teams'
    print('url is ', url)

    # params就是普通的url后加参数的方式
    r = requests.get(
        url=url, params=params, headers=headers)
    print('r\'s status code is ', r.status_code)
    print('r\'s text is ', r.text)
    print('r\'s json is ', str(r.json))
    # team_id = 172bbd05ab0247b6b4f92158af3e522b


# --获取tower特定项目的todolist列表--
def test_get_tower_todo_list():
    # url = 'https://api.tower.im/v1/projects/' + '4076fe9fa73f41c4956d4eda5d4edd50' + '/todolists?access_token=' + acces_token
    params = {}
    params['access_token'] = acces_token

    url = base_url + '/projects/' + '4076fe9fa73f41c4956d4eda5d4edd50' + '/todolists'
    # print url
    r = requests.get(url=url, params=params)
    print('r\'s status code is ', r.status_code)
    print('r\'s text is ', r.text)
    print('r\'s json is ', r.json)


def test_get_project_docs():
    """
        获取团队项目列表
        :return:
        """
    headers = {}
    # headers['Authorization'] = acces_token  # 测试用

    params = {}
    params['access_token'] = acces_token

    # https://tower.im/api/v1/teams/{team_id}/projects
    url = base_url + '/projects/' + 'cf4df471677e4316b5cc9620f3f5a808' + '/docs'
    print('url is ', url)

    # params就是普通的url后加参数的方式
    r = requests.get(
        url=url, params=params, headers=headers)
    print('r\'s status code is ', r.status_code)
    print('r\'s text is ', r.text)
    print('r\'s json is ', str(r.json))


file_path = '/Users/yandongjun/Downloads/e9fb213a680cd6ee8cc788bbac8072be/projects/412732-大树金融文档共享/documents/3225e77c11e748219450bc5a69be9ab5_19.html'

def test_html_to_md():
    text_maker = ht.HTML2Text()
    # 读取html格式文件
    with open(file_path, 'r', encoding='UTF-8') as f:
        htmlpage = f.read()
    # 处理html格式文件中的内容
    text_maker.ignore_links = True
    text = text_maker.handle(htmlpage)
    # 写入处理后的内容
    with open('test.md', 'w') as f:
        f.write(text)


def test_html_to_md2():
    # 读取html格式文件
    with open(file_path, 'r', encoding='UTF-8') as f:
        htmlpage = f.read()
    # 处理html格式文件中的内容
    text = tomd.Tomd(htmlpage).markdown
    # 写入处理后的内容
    with open('test.md', 'w') as f:
        f.write(text)

def test_html_to_wiki():
    # 读取html格式文件
    with open(file_path, 'r', encoding='UTF-8') as f:
        htmlpage = f.read()
    # 处理html格式文件中的内容
    text = tomd.Tomd(htmlpage).markdown
    # 写入处理后的内容
    with open('test.md', 'w') as f:
        f.write(text)