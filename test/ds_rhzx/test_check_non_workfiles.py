# -*- coding:utf-8 -*-
# Power by godaipl 2019-07-09 15:40:15
import datetime
import time

import xlrd
from xlrd import xldate_as_tuple
import xlwt as ExcelWrite

from util.common.db.MySqlHelper import MysqlHelper

xls_file_path = r'/Users/yandongjun/Downloads/test/original_file.xls'

xls_target_file = r'/Users/yandongjun/Downloads/test/table_import_tidb4.xlsx'

xls_write_path = r'/Users/yandongjun/Downloads/test/final.xls'

final_path = r'/Users/yandongjun/Downloads/test/table_import2019-07-09-2132.xls'
# file_path_final = r'/Users/yandongjun/Downloads/异常查询查得用户信息.xlsx'
file_path_final = r'/Users/yandongjun/Downloads/test/2019-07-23-6-1703-2.xlsx'


# mysql = MysqlHelper(user_name='root', password='', database='test', host='localhost')

# select * from table_import_month into outfile '/tmp/2019-07-22-6.xls'
# echo "select usercode, queryorgno, querydate, NAME, CERTTYPE, CERTNO, flag, concat(repno, '\t'), concat(report_id, '\t'), username, search_type, registe_time, loan_time, credit_time, latest_sign_time, search_time, querydate2, concat(userid, '\t') from mtest.table_import_month where 1 " | mysql -h10.110.0.83 -P54000 -uyandongjun -p > /tmp/2019-07-23-6-1226.xls

def test_init_searchinfos():
    """
    初始化资产信息
    :return:
    """
    # 1. 从本地文件中读取数据
    xls_data = file_load(xls_file_path)
    xls_tartget = file_load(xls_target_file)
    # xls_target = xls_data
    if xls_data:
        # print(xls_data)
        final_data = trans_data(xls_data, xls_tartget)
        # init_table(final_data)
        writeXLS(final_data)
    else:
        print('no data')


def trans_data(xls_data, xls_tartget):
    dataset = list()
    for data in xls_data:
        userCode = data[0]
        queryOrgno = data[1]
        queryDate = data[2]
        name = data[3]
        certType = data[4]
        certNo = data[5]
        flag = data[6]
        repno = data[7]
        print('userCode is ', userCode, ' queryOrgno is ', queryOrgno, 'queryDate is ', queryDate, 'name is ', name,
              'certType is ', certType,
              'certNo is ', certNo, 'flag is ', flag, 'repno is ', repno)
        # 循环获取线上数据中的值
        target_element = list()
        target_element.append(userCode)
        target_element.append(queryOrgno)
        target_element.append(queryDate)
        target_element.append(name)
        target_element.append(certType)
        target_element.append(certNo)
        target_element.append(flag)
        target_element.append(repno)
        for data2 in xls_tartget:
            id = data2[0]
            user_id = data2[1]
            report_id = data2[2]
            name2 = data2[3]
            search_reason = data2[4]
            if search_reason == '01':
                search_reason = '贷后管理'
            if search_reason == '02':
                search_reason = '贷款申请'
            zhuce_time = data2[5]
            shenqing_daikulan_time = data2[6]
            credit_time = data2[7]
            # if (repno and report_id and repno == report_id) or (name and name2 and name == name2):
            if repno and report_id and repno == report_id:
                target_element.append(name2)
                target_element.append(search_reason)
                target_element.append(zhuce_time)
                target_element.append(shenqing_daikulan_time)
                target_element.append(credit_time)
                queryDate2 = datetime.datetime.strptime(queryDate, '%Y%m%d %H:%M:%S')
                target_element.append(str(queryDate2))
                target_element.append(user_id)
                target_element.append(report_id)

                if repno != report_id:
                    target_element.append('报告ID不一致')
                break
            # else:
            #     # target_element.append("")
            #     # target_element.append("")
            #     # target_element.append("")
            #     # target_element.append("")
        dataset.append(target_element)

    return dataset


# 读文件
def file_load(filename='待读取.xlsx'):
    dataset = []
    workbook = xlrd.open_workbook(filename)
    table = workbook.sheets()[0]
    for row in range(table.nrows):
        dataset.append(table.row_values(row))
    return dataset


def writeXLS(datas):
    xls = ExcelWrite.Workbook()
    sheet = xls.add_sheet("Sheet1")

    i = 0
    for tmp in datas:
        print(tmp)
        j = 0
        for tmp2 in tmp:
            sheet.write(i, j, tmp2)
            j = j + 1
        i = i + 1
    xls.save(xls_write_path)
    # for i in range(0, 4):
    #     for j in range(0, len(datas)):
    #         sheet.write(j, i, datas[i][j])
    #
    # xls.save(xls_write_path)


def init_table(final_data):
    if final_data:
        print(final_data)
        target_data = trans_original_data(final_data)

        table_column = ['search_time', 'user_id']
        sql_insert = get_sql_insert('rhzx_tmp', table_column)
        # mysql.insert_batch(sql_insert, target_data)
    else:
        print('no data')


def trans_original_data(original_data):
    target_data = list()
    i = 0
    for data in original_data:
        target_item = list()
        if i == 0:
            print('i is 0 ignore')
        else:
            j = 0
            # for element in data:
            #     element_tmp = str(element)
            #     target_item.append(element_tmp)
            #     j = j + 1
            if len(data) >= 7:
                report_id = data[7]
                if report_id:
                    search_time = data[2]
                    search_time = time.strptime(search_time, fmt='%yyyy%m%d %H:%M:%S')
                    user_id = data[13]
                    # target_item.append(report_id)
                    target_item.append(search_time)
                    target_item.append(user_id)
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


def test_time_tras():
    str_p = '20190511 16:29:27'
    dateTime_p = datetime.datetime.strptime(str_p, '%Y%m%d %H:%M:%S')
    print(dateTime_p)  # 2019-01-30 15:29:08


def test_check_xls():
    datas = file_load(final_path)
    for data in datas:
        type = data[10]
        if type != 'type':
            loan_date = data[12]
            loan_time = None
            if loan_date != '0000-00-00 00:00:00':
                loan_time = datetime.datetime.strptime(loan_date, '%Y-%m-%d %H:%M:%S')
            credit_date2 = data[13]
            credit_time2 = None
            if credit_date2 != '0000-00-00 00:00:00':
                credit_time2 = datetime.datetime.strptime(credit_date2, '%Y-%m-%d %H:%M:%S')
            search_date = data[15]
            search_time = None
            if search_date != '0000-00-00 00:00:00':
                search_time = datetime.datetime.strptime(search_date, '%Y%m%d %H:%M:%S')

            # if credit_time2 is not None and loan_time is not None:
            #     if credit_time2 < loan_time:
            #         print('credit_time < loan_time', data)
            if credit_time2 is not None and search_time is not None:
                if search_time < credit_time2:
                    print('search_time < credit_time', data)


def test_check_final():
    datas = file_load(file_path_final)

    i = 0
    j = 0
    z = 0
    z1 = 0
    k = 0
    h = 0
    l = 0

    xyz = 0
    for data in datas:
        if xyz == 0:
            print("xyz is ", xyz)
        else:
            rh_name = data[4]
            type_loan = data[10]
            registe_time = data[11]
            loan_apply_time = data[12]
            credit_time = data[13]
            last_sign_time = data[14]
            rh_query_time = data[15]

            if type_loan != '贷后管理' and type_loan != '查询类型' and type_loan != 'search_type':
                try:
                    # registe_time_final = xldate_as_tuple(registe_time, 0)
                    if rh_query_time == '':
                        rh_query_time_final = None
                    else:
                        rh_query_time_final = xldate_as_tuple(rh_query_time, 0)

                    if loan_apply_time == '':
                        loan_apply_time_final = None
                    else:
                        loan_apply_time_final = xldate_as_tuple(loan_apply_time, 0)

                    if credit_time == '':
                        credit_time_final = None
                    else:
                        credit_time_final = xldate_as_tuple(credit_time, 0)

                except Exception as e:
                    print("error", e)

                if loan_apply_time_final is None:
                    print('申请贷款时间为空 ', data)
                    z = z + 1

                if credit_time_final is None:
                    print('初次授信时间为空 ', data)
                    z1 = z1 + 1

                # else:
                # print('OK')

                # loan_apply_time_final_datetime = datetime.datetime(loan_apply_time_final[0], loan_apply_time_final[1], loan_apply_time_final[2], loan_apply_time_final[3], loan_apply_time_final[4], loan_apply_time_final[5])
                if rh_query_time_final and loan_apply_time_final and rh_query_time_final < loan_apply_time_final:
                    print('query_time_final < loan_apply_time_final ', data)
                    l = l + 1
                # credit_time_final_datetime = datetime.datetime(credit_time_final[0], credit_time_final[1], credit_time_final[2], credit_time_final[3], credit_time_final[4], credit_time_final[5])
                if rh_query_time_final and credit_time_final and rh_query_time_final < credit_time_final:
                    print('query_time_final < credit_time_final ', data)
                    k = k + 1
            else:
                j = j + 1
            i = i + 1
        xyz += 1

    print('total 总数 is ', i - 1)
    print('total 授信时间为空的数据有 ', z1, '条')
    print('total 授信时间在查询时间之后 ', k, '条')
    print('total 申请贷款时间为空的数据有 ', z, '条')
    print('total 授信时间在申请贷款时间之后 ', h, '条')
    print('total 查询时间在申请贷款时间之前 ', l, '条')
    print("total 贷后 is ", j - 1)
