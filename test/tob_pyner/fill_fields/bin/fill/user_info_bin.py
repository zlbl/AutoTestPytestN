from datetime import datetime

from test.tob_pyner.fill_fields.util.MySqlHelper import query, execute, insert_batch, update, get_cursor
from test.tob_pyner.fill_fields.util.transform_util import get_area_dict, trans_idc_area, trans_uscc_area

DropUserTemporarySQL = 'DROP TABLE IF EXISTS user_temporary'

CreateUserTemporarySQL = 'CREATE TABLE user_temporary(' \
                         'user_id varchar(50),' \
                         'platform_id varchar(50),' \
                         'depository_id bigint,' \
                         'cred_no varchar(50),' \
                         'province_code varchar(20),' \
                         'province_name varchar(20),' \
                         'city_code varchar(20),' \
                         'city_name varchar(20),' \
                         'area_code varchar(20),' \
                         'area_name varchar(20),' \
                         'longitude varchar(20),' \
                         'latitude varchar(20))'

InsertUserTemporarySQL = 'INSERT INTO user_temporary VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

UpdateUserInfoSQL = 'UPDATE pyner_user u, user_temporary t ' \
                    'SET u.province_code = t.province_code, u.province_name = t.province_name,' \
                    'u.city_code = t.city_code, u.city_name = t.city_name,' \
                    'u.area_code = t.area_code, u.area_name = t.area_name,' \
                    'u.latitude = t.latitude, u.longitude = t.longitude ' \
                    'where u.bank_user_id = t.user_id  ' \
                    'and u.bank_platform_id = t.platform_id  ' \
                    'and u.depository_id = t.depository_id'


def user_area_transform():
    # 删临时表
    execute(DropUserTemporarySQL)
    # 建临时表
    execute(CreateUserTemporarySQL)

    params = []
    area_dict = get_area_dict()
    cursor = get_cursor("select bank_user_id, bank_platform_id, depository_id, cred_no "
                        "from pyner_user "
                        "where user_type = 'Person' and cred_type = 'IDC'")
    print('fetch 个人信息结束 {}'.format(datetime.now()))
    while True:
        params.clear()
        results = cursor.fetchmany(10000)
        print('已经获取个人数据 {}条 时间:{}'.format(len(results), datetime.now()))
        if len(results) == 0:
            break
        for result in results:
            area = trans_idc_area(result[3], area_dict)
            params.append([result[0], result[1], result[2], result[3], area.province_code, area.province_name,
                           area.city_code, area.city_name, area.area_code, area.area_name, area.longitude,
                           area.latitude])
            # 在临时表中插入转换后的数据
        insert_batch(InsertUserTemporarySQL, params=params)

    cursor = get_cursor("select bank_user_id, bank_platform_id, depository_id, cred_no "
                        "from pyner_user "
                        "where user_type != 'Person' and cred_type = 'USCC'")
    print('fetch 企业信息结束 {}', datetime.now())

    while True:
        params.clear()
        results = cursor.fetchmany(1000)
        print('已经获取企业数据 {}条 时间:{}'.format(len(results), datetime.now()))
        if len(results) == 0:
            break
        for result in results:
            area = trans_uscc_area(result[3], area_dict)
            params.append([result[0], result[1], result[2], result[3], area.province_code, area.province_name,
                           area.city_code, area.city_name, area.area_code, area.area_name, area.longitude,
                           area.latitude])
            # 在临时表中插入转换后的数据
        insert_batch(InsertUserTemporarySQL, params=params)

    # 更新存管表用户信息
    update(UpdateUserInfoSQL)

    print('user_area_transform Finish!', datetime.now())


if __name__ == '__main__':
    user_area_transform()
    # cursor = get_cursor("select * from pyner_platform")
    # while True:
    #     results = cursor.fetchmany(10)
    #     print(results)
    #     if len(results) == 0:
    #         break
