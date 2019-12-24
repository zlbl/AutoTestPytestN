#!/usr/bin/python3
# -*- coding:utf-8 -*-

# pip3 install pyexcel-xls
from util.common.db.MySqlHelper import MysqlHelper
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple

mysql = MysqlHelper(user_name='root', password='Vx8kpx7Ylg', database='tfams', host='192.168.5.109')

xlsx_file_path = r'/Users/yandongjun/Documents/workspace/test/tob-auto-test-pytest/test/ds_tcms/files/资产盘点信息.xlsx'


def test_init_amsinfos():
    """
    初始化资产信息
    :return:
    """
    # 1. 从本地文件中读取数据
    xls_data = file_load(xlsx_file_path)
    if xls_data:
        print(xls_data)
        target_data = trans_original_data(xls_data)

        # AssetsType = 3 通讯设备
        # AssetsSecType = 8 服务器
        # AssetsStatus = 1 使用中
        table_column = ['AssetsNo', 'AssetsType', 'AssetsSecType', 'SerialNo', 'BuyAt',
                        'Price', 'AssetsStatus', 'UseAt', 'Memo']
        sql_insert = get_sql_insert('ams_assets_info', table_column)
        mysql.insert_batch(sql_insert, target_data)
    else:
        print('no data')


# 读文件
def file_load(filename='待读取.xlsx'):
    dataset = []
    workbook = xlrd.open_workbook(filename)
    table = workbook.sheets()[0]
    for row in range(table.nrows):
        dataset.append(table.row_values(row))
    return dataset


def trans_original_data(original_data):
    target_data = list()
    i = 0
    for data in original_data:
        target_item = list()
        if i == 0:
            print('i is 0 ignore')
        else:
            j = 0
            for element in data:
                element_tmp = str(element)
                if j == 1:
                    element_tmp = str(3)

                if j == 2:
                    if element_tmp == '网络设备':
                        element_tmp = str(9)
                    # elif element_tmp == '服务器':
                    #     element_tmp = str(8)
                    else:
                        element_tmp = str(8)

                if j == 3:
                    element_tmp = element_tmp.replace(' ', '')

                if j == 6:
                    element_tmp = str(1)

                if j == 4 or j == 7:
                    date = datetime(*xldate_as_tuple(element, 0))
                    element_tmp = date.strftime('%Y-%m-%d %H:%M:%S')

                if j == 8:
                    element_tmp = element_tmp.replace(' ', '')

                target_item.append(element_tmp)
                j = j + 1
            target_data.append(target_item)
        i = i + 1

    print(target_data)
    return target_data


def get_sql_insert(table_name, table_column, ):
    question_marks = ",".join(["%s" for i in range(len(table_column))])
    table_column_marks = ",".join(table_column[i] for i in range(len(table_column)))
    sql_insert = "INSERT INTO %s (%s) VALUES (%s)" % \
                 (table_name, table_column_marks, question_marks)

    return sql_insert
