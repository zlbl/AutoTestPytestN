#!/usr/bin/python3

import pymysql
# 读写2007 excel
import openpyxl

import time

import requests


def get_report_data():
    # 打开数据库连接
    db = pymysql.connect(
        "192.168.5.94", "root", "123456", "b2b_bi_report", charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sql = """
    select d.report_id,
           d.report_name,
           d.database_code,
           d.database_name,
           d.max_limit,
           rh.report_result_handle_id,
           rh.execute_sql
    from b2b_bi_report.report_define d,
         b2b_bi_report.report_result_handle rh
    where d.report_id = rh.report_id
      and d.database_code = 14
      and d.state = 'U' order by rh.execute_sql;
    """

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)

    # 获取所有查询报表，及最终需要更新的报表表信息
    data = cursor.fetchall()

    # for tmp in data:
    #     print(tmp)

    # print("Database version : ", data)

    # 关闭数据库连接
    db.close()

    return data


def init_excel_data(data):
    excel_row_infos = [[
        "reportId", "报表名称", "数据库ID", "数据获取原数据库", "数据库limit", "result表id",
        "报表插入语句", "报表查询语句", "报表查询条件", "报表名"
    ]]
    for data_one in data:
        table_name = get_table_name(data_one)
        # data_one = data_one + table_name
        select_infos = get_select_infos(data_one[0])
        tuple_tmp = data_one + select_infos + (table_name, '')
        excel_row_infos.append(tuple_tmp)
    return excel_row_infos


def get_select_infos(report_id):
    # params就是普通的url后加参数的方式
    # r = requests.post(
    # url='http://www.baidu.com', params=params, headers=headers)

    url = 'http://192.168.5.93:8666/report/opera/getReportExecuteSql?reportId=' + str(
        report_id)

    r = requests.get(url=url)
    ret_json = r.json()
    select_sql = ret_json['data']['selectSql']
    condition_value_list = ret_json['data']['coditionValueList']
    print('select sql is ', select_sql)
    print('condition_value_list is ', condition_value_list)

    return select_sql, condition_value_list


def get_table_name(data_one):
    """
    获取某一行数据的报表表名
    :param data_one:
    :return:
    """
    sql = data_one[6]

    table_name = ''

    if (sql.__contains__('insert')
            or sql.__contains__('INSERT')) and sql.__contains__('('):
        print('1 deal sql is ', sql)
        index_spot = sql.index('.', 0)
        print('1 index_spot is ', sql.index('.', 0))
        index_quoat = sql.index('(', 0)
        print('1 index_quoat is ', sql.index('(', 0))
        table_name = sql[index_spot + 1:index_quoat].strip()
    elif sql.__contains__('TRUNCATE TABLE'):
        print('2 deal sql is ', sql)
        index_spot = sql.index('.', 0)
        print('2 index_spot is ', index_spot)
        table_name = sql[index_spot + 1:].strip()
        if table_name.endswith(';'):
            table_name = table_name[:-1]
    elif (sql.__contains__('update')
          or sql.__contains__('UPDATE')) and (sql.__contains__('set')
                                              or sql.__contains__('/tset')):
        print('3 deal sql is ', sql)
        index_spot = sql.index('.', 0)
        print('3 index_spot is ', index_spot)
        index_set = sql.index('set', 0)
        print('3 index_set is ', index_set)
        table_name = sql[index_spot + 1:index_set]
    else:
        print('do not deal sql is ', sql)

    table_name = table_name.replace('`', '')
    return table_name


def write_report_data(file_path, data):
    """
    写报表excel
    :param file_path: 
    :param data:
    :return:
    """
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '报表列表'

    excel_row_infos = init_excel_data(data)

    for i in range(len(excel_row_infos)):
        for j in range(len(excel_row_infos[i])):
            sheet.cell(
                row=i + 1, column=j + 1, value=str(excel_row_infos[i][j]))

    wb.save(file_path)

    print("写数据成功")
    wb.close()


def test_1():
    file_path = 'reportInfo' + str(time.time()) + '.xlsx'
    data = get_report_data()
    write_report_data(file_path, data)


def test_2():
    data = get_report_data()
    for data_one in data:
        print('table_name is ', get_table_name(data_one))


# test_1()
