from datetime import datetime

from test.tob_pyner.fill_fields.bin.fill.update_cust_info_sql import *
from test.tob_pyner.fill_fields.util.MySqlHelper import select_insert, update


def generate_customer():
    """生成客户id"""
    # ALTER TABLE pyner_customer AUTO_INCREMENT = 1000000001;
    select_insert(generateSQL)
    """生成平台客户ID"""
    update(updatePlatformCredInfoUSCCSQL)
    update(updatePlatformCredInfoBLCSQL)
    select_insert(generatePlatformSQL)
    print('generate_customer Finish', datetime.now())


def update_user_customer_id():
    """更新用户表客户Id"""
    update(updateUserCustomerIdSQL)
    print('update_user_customer_id Finish', datetime.now())


def update_person_customer_id():
    update(updatePersonCustomerIdSQL)
    print('update_person_customer_id Finish', datetime.now())


def update_enterprise_customer_id():
    update(updateEnterpriseCustomerIdSQL)
    print('update_enterprise_customer_id Finish', datetime.now())


def update_platform_customer_id():
    update(updatePlatformCustomerIdSQL)
    print('update_platform_customer_id Finish', datetime.now())


def update_account_customer_id():
    # 更新用户账户表
    update(updateAccountCustomerIdSQL1)
    # 更新平台账户表
    update(updateAccountCustomerIdSQL2)
    print('update_account_customer_id Finish', datetime.now())


def update_bid_customer_id():
    update(updateBidCustomerIdSQL)
    print('update_bid_customer_id Finish', datetime.now())


def update_obligatory_customer_id():
    update(updateObligatoryCustomerIdSQL)
    print('update_obligatory_customer_id Finish', datetime.now())


def update_trade_pay_customer_id():
    update(updateTradePayCustomerIdSQL)
    print('update_trade_pay_customer_id Finish', datetime.now())


def update_trade_receive_customer_id():
    update(updateTradeReceiveCustomerIdSQL)
    print('update_trade_receive_customer_id Finish', datetime.now())


if __name__ == '__main__':
    print('开始时间:', datetime.now())
    # generate_customer()
    update_user_customer_id()
    update_person_customer_id()
    update_enterprise_customer_id()
    update_platform_customer_id()
    update_account_customer_id()
    update_bid_customer_id()
    update_obligatory_customer_id()
    update_trade_pay_customer_id()
    update_trade_receive_customer_id()
    print('结束时间:', datetime.now())


def generate_customer_id():
    # 生成customerId
    generate_customer()

    # 更新customerId到User表
    update_user_customer_id()

    # 更新customerId到Person表
    update_person_customer_id()

    # 更新customerId到Enterprise表
    update_enterprise_customer_id()

    # 更新customerId到Platform表
    update_platform_customer_id()

    # 更新customerId到Account表
    update_account_customer_id()

    # 更新customerId到Bid表
    update_bid_customer_id()

    # 更新customerId到Obligatory表
    update_obligatory_customer_id()

    # 更新付款方customerId到Trade表
    update_trade_pay_customer_id()

    # 更新收款方customerId到Trade表
    update_trade_receive_customer_id()
