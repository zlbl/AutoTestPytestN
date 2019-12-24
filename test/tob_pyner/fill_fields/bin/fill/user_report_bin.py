from test.tob_pyner.fill_fields.util.MySqlHelper import select_insert

createUserReportSQL = '''
                        insert into pyner_user_report
                            (bank_user_id, bank_platform_id, user_type, customer_id, depository_id, saas_id, 
                            create_time, last_update_time, creator, last_updater, state, business_type, real_name, 
                            cred_type, cred_no, bank_create_time, bank_update_time, province_code, province_name, 
                            city_code, city_name, longitude, latitude)
                        select bank_user_id, bank_platform_id, user_type, customer_id, depository_id, saas_id, now(), 
                        now(), 0, 0, 'U',business_type, real_name, cred_type, cred_no, bank_create_time, 
                        bank_update_time, province_code, province_name, city_code, city_name, longitude, latitude 
                        from pyner_user'''


def generate_user_report():
    """生成用户报表基础信息"""
    select_insert(createUserReportSQL)
    print('create_user_report Finish')


if __name__ == '__main__':
    generate_user_report()
