# -*- coding:utf-8 -*-
# Power by godaipl 2018-11-26 17:28:15

import requests

import ssl

import time

import json

from test.ds_rhzx.MySqlHelper import insert_batch

url = 'https://db.99gfd.com/query/getresult/'


def test_get_latest1000_userids():
    """
            测试http get请求
            """
    headers = {}
    headers['Cookie'] = 'sessionid=awtop4tsbz6hzjctssbc3f81jrd2u2em'
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    headers[
        'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'  # 测试用
    headers['Host'] = 'db.99gfd.com'  # 测试用
    headers['Referer'] = 'https://db.99gfd.com/query/index/'  # 测试用
    headers['X-Requested-With'] = 'XMLHttpRequest'  # 测试用

    params = {}
    params[
        'sql'] = "select t_loan_order.UserId from t_loan_order where exists(select * from t_repayment_schedule where t_loan_order.Id = t_repayment_schedule.LoanOrderId) order by t_loan_order.CreateDate desc limit 1000;"
    params['db'] = "172.16.100.204"
    params['db_name'] = "loandb"

    ssl._create_default_https_context = ssl._create_unverified_context
    # params就是普通的url后加参数的方式
    r = requests.get(
        url=url, params=params, headers=headers, verify=ssl.CERT_NONE)
    print('r\'s json is ', r.json)
    print('r\'s json is ', r)
    userIdStr = ''
    for userIdTmp in r.json().get('results'):
        userIdStr += userIdTmp.get('UserId')
        userIdStr += ','

    print("userIdStr is ", userIdStr)


def test_get_non_userids():
    """
        测试http get请求
        """
    headers = {}
    headers['Cookie'] = 'sessionid=losb3rs5b4ucvlv4f0l0w8mj07uap2tt'
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    headers[
        'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'  # 测试用
    headers['Host'] = 'db.99gfd.com'  # 测试用
    headers['Referer'] = 'https://db.99gfd.com/query/index/'  # 测试用
    headers['X-Requested-With'] = 'XMLHttpRequest'  # 测试用

    params = {}
    params[
        'sql'] = "select distinct tu.user_id from loandb.tmp_userid tu where tu.user_id not in (select distinct UserId from loandb.t_fdd_contract tfc where tfc.ContractType = 'CREDIT_QUERY_AGE') and tu.user_id not in (select distinct UserId from loandb.t_loan_order tlo where tlo.GlobalPlatformId = 17 and Status = 4) limit 100000;"
    params['db'] = "172.16.100.204"
    params['db_name'] = "loandb"

    ssl._create_default_https_context = ssl._create_unverified_context
    # params就是普通的url后加参数的方式
    r = requests.get(
        url=url, params=params, headers=headers, verify=ssl.CERT_NONE)
    print('r\'s json is ', r.json)
    print('r\'s json is ', r)
    userIdStr = ''
    for userIdTmp in r.json().get('results'):
        userIdStr += userIdTmp.get('user_id')
        userIdStr += ','

    print("userIdStr is ", userIdStr)


def test_userIds_get():
    """
    测试http get请求
    """
    headers = {}
    headers['Cookie'] = 'sessionid=losb3rs5b4ucvlv4f0l0w8mj07uap2tt'
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    headers[
        'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'  # 测试用
    headers['Host'] = 'db.99gfd.com'  # 测试用
    headers['Referer'] = 'https://db.99gfd.com/query/index/'  # 测试用
    headers['X-Requested-With'] = 'XMLHttpRequest'  # 测试用

    params = {}
    params[
        'sql'] = "select user_id, create_time from credit_report_search_stats where task_id is not null and create_time < '2019-06-01' limit 10000000;"
    params['db'] = "172.16.100.203"
    params['db_name'] = "thirdparty2"

    ssl._create_default_https_context = ssl._create_unverified_context
    # params就是普通的url后加参数的方式
    r = requests.get(
        url=url, params=params, headers=headers, verify=ssl.CERT_NONE)
    print('r\'s json is ', r.json)
    print('r\'s json is ', r)
    userIdStr = ''
    array = []
    columns = ['user_id', 'create_time']
    for userIdJson in r.json().get('results'):
        array_per = []
        print(userIdJson)
        array_per.append(userIdJson.get('user_id'))
        dateStr = userIdJson.get('create_time')
        dateRight = dateStr.replace("\xa0", " ")
        array_per.append(dateRight)
        array.append(array_per)

    multi_mig_oracle_datas(array, 'tmp_userid', columns)


def multi_mig_oracle_datas(data_array, table_name, table_columns):
    """
    具体同步oralce数据库中的数据至Mysql中
    :param data_array: 从oracle数据库中查询出来的数据
    :param table_name: 最终需要生成的目标mysql数据库表
    :return:
    """
    question_marks = ",".join(["%s" for i in range(len(table_columns))])
    table_columns_marks = ",".join(table_columns)

    sql_insert = "INSERT IGNORE INTO %s (%s) VALUES (%s)" % \
                 (table_name, table_columns_marks, question_marks)

    t1 = time.time()
    insert_batch(sql_insert, data_array)
    t2 = time.time()
    print("insert_batch 单个批量插入耗时 ", t2 - t1, " s")
