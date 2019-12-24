from datetime import datetime

from test.tob_pyner.fill_fields.bin.fill.update_cust_info_sql import updateBidPersonInfoSQL, \
    updateObligatoryPersonInfoSQL, \
    updateReportPersonInfoSQL
from test.tob_pyner.fill_fields.util.MySqlHelper import execute, query, insert_batch, update, get_cursor
from test.tob_pyner.fill_fields.util.transform_util import trans_sex, trans_birthday

DropPersonTemporarySQL = 'DROP TABLE IF EXISTS person_temporary'

CreatePersonTemporarySQL = 'CREATE TABLE person_temporary(' \
                           'user_id varchar(50),' \
                           'platform_id varchar(50),' \
                           'depository_id bigint,' \
                           'cred_no varchar(50),' \
                           'gender varchar(20),' \
                           'birthday date)'

InsertPersonTemporarySQL = 'INSERT INTO person_temporary VALUES (%s,%s,%s,%s,%s,%s)'
UpdatePersonInfoSQL = 'update pyner_user_person u, person_temporary t ' \
                      'set u.gender = t.gender, u.birthday = t.birthday ' \
                      'where u.bank_user_id = t.user_id  ' \
                      'and u.bank_platform_id = t.platform_id ' \
                      'and u.depository_id = t.depository_id'


def person_info_transform():
    # 删临时表
    execute(DropPersonTemporarySQL)
    # 建临时表
    execute(CreatePersonTemporarySQL)

    params = []
    cursor = get_cursor("select bank_user_id, bank_platform_id, depository_id, cred_no "
                        "from pyner_user_person "
                        "where cred_type = 'IDC'")
    print('fetch 个人信息结束 {}'.format(datetime.now()))

    while True:
        params.clear()
        results = cursor.fetchmany(10000)
        print('已经获取个人数据 {}条 时间:{}'.format(len(results), datetime.now()))

        if len(results) == 0:
            break
        for result in results:
            sex = trans_sex(result[3])
            birthday = trans_birthday(result[3])
            params.append([result[0], result[1], result[2], result[3], sex, birthday])

        # 在临时表中插入转换后的数据
        insert_batch(InsertPersonTemporarySQL, params=params)

    # 更新存管表用户信息
    update(UpdatePersonInfoSQL)

    print('person_info_transform Finish', datetime.now())


def update_bid_person_info():
    update(updateBidPersonInfoSQL)
    print('update_bid_person_info Finish', datetime.now())


def update_obligatory_person_info():
    update(updateObligatoryPersonInfoSQL)
    print('update_obligatory_person_info Finish', datetime.now())


def update_report_person_info():
    update(updateReportPersonInfoSQL)
    print('update_report_person_info Finish', datetime.now())


def update_person_info():
    update_bid_person_info()
    update_obligatory_person_info()
    update_report_person_info()


if __name__ == '__main__':
    print('开始时间:', datetime.now())
    person_info_transform()
    print('结束时间:', datetime.now())
