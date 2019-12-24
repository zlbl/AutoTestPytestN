from faker import Faker

from test.tob_pyner.build_user.sqls.build_user_sql import *
from test.tob_pyner.fill_fields.bin.calculate.calc_bid import sync_obligatory_borrower_info
from test.tob_pyner.fill_fields.bin.fill.customer_bin import generate_customer_id
from test.tob_pyner.fill_fields.bin.fill.person_info_bin import person_info_transform, update_person_info
from test.tob_pyner.fill_fields.bin.fill.user_info_bin import user_area_transform
from test.tob_pyner.fill_fields.bin.fill.user_report_bin import generate_user_report
from test.tob_pyner.fill_fields.util.MySqlHelper import query, insert_batch, update

insertUserSQL = '''
INSERT IGNORE INTO pyner_user
    (bank_user_id, user_type, bank_platform_id, platform_name, business_type, user_status, customer_id, depository_id, 
    saas_id, create_time, last_update_time, creator, last_updater, state, real_name, cred_type, cred_no, 
    bank_create_time, bank_update_time) 
    VALUES (%s,'Person',%s,null,'Lender','Normal',null,%s,%s,now(),now(),1,1,'U',%s,'IDC',%s,now(),now())'''

insertPersonSQL = '''
INSERT IGNORE INTO pyner_user_person
    (bank_user_id, bank_platform_id, depository_id, saas_id, real_name, cred_type, cred_no,  create_time, last_update_time, creator, last_updater, state, bank_create_time, bank_update_time)
VALUES (%s,%s,%s,%s,%s,'IDC',%s,now(),now(), 1,1,'U',now(), now())
'''


def get_history_user():
    results = []
    """查询账户表中历史用户数据"""
    results.extend(query(queryHistoryAccountUserSQL))
    """查询标的表中历史用户数据"""
    results.extend(query(queryHistoryBidUserSQL))
    """查询债权表中历史用户数据"""
    results.extend(query(queryHistoryObligatoryUserSQL))
    """查询交易表中历史出款人用户数据"""
    results.extend(query(queryHistoryTradePayerSQL))
    """查询交易表中历史收款人人用户数据"""
    results.extend(query(queryHistoryTradeReceiverSQL))
    return results


def build_history_user():
    faker = Faker("zh_CN")
    params = []
    results = get_history_user()
    for result in results:
        param = [result[0], result[1], result[2], result[3], faker.name(), faker.ssn()]
        params.append(param)

    # 插入用户表
    insert_batch(insertUserSQL, params=params)
    print('insertUser Finish!')
    # 插入个人表
    insert_batch(insertPersonSQL, params=params)
    print('insertPerson Finish!')
    # 更新平台名
    update(updatePlatformNameSQL)


def update_other_info():
    user_area_transform()
    # # 个人信息 性别、出生日期转换
    person_info_transform()
    """
    注意!
    ALTER TABLE pyner_customer MODIFY customer_id bigint(20) NOT NULL auto_increment COMMENT '客户ID';
    ALTER TABLE pyner_customer AUTO_INCREMENT = 1000000001;
    """
    # 生成 customer_id 相关信息
    generate_customer_id()
    # 创建用户报表信息
    generate_user_report()
    # 更新个人信息的性别 出生日期
    update_person_info()
    # 更新债权借款人信息
    sync_obligatory_borrower_info()


if __name__ == '__main__':
    build_history_user()
    update_other_info()
