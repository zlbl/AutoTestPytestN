from datetime import datetime

from test.tob_pyner.fill_fields.bin.calculate.sqls.bid_sql import *
from test.tob_pyner.fill_fields.util.MySqlHelper import update


def update_bid_platform_name():
    """设置标的平台名称"""
    update(updateBidPlatformNameSQL)
    print('update_bid_platform_name Finish!', datetime.now())


def calc_flowed_bid_time():
    """设置流标标的时间"""
    update(calcFlowBidTimeSQL)
    print('calc_flowed_bid_time Finish!', datetime.now())


def calc_request_time():
    """请求时间为空"""
    update(calcRequestTimeSQL)
    print('calc_request_time Finish!', datetime.now())


def calc_granted_time():
    """放款时间为空且已放款"""
    update(calcGrantedTimeSQL)
    print('calc_granted_time Finish!', datetime.now())


def calc_lended_bid_time():
    """设置放款标的时间"""
    update(calcLendedBidTimeSQL)
    print('calc_lended_bid_time Finish!', datetime.now())


def calc_raise_duration():
    """设置募集期"""
    update(calcRaiseDurationSQL)
    update(calcRaiseDurationSQL1)
    print('calc_raise_duration Finish!', datetime.now())


def calc_should_repay_time():
    """设置应还时间"""
    update(calcShowRepayTimeSQL)
    print('calc_should_repay_time Finish!', datetime.now())


def calc_granted_amount():
    """放款金额"""
    update(calcGrantedAmountSQL)
    print('calc_granted_amount Finish!', datetime.now())


def calc_repayed_amount():
    """还款金额"""
    update(calcRepayedAmountSQL)
    print('calc_repayed_amount Finish!', datetime.now())


def calc_balance_amount():
    """设置借款余额"""
    update(calcBalanceAmountSQL)
    update(calcBalanceAmountSQL1)
    print('calc_balance_amount Finish!', datetime.now())


def calc_close_bid_status():
    """设置结清标的时间、状态、综合费率"""
    update(calcCloseBidStatusSQL)
    print('calc_close_bid_status Finish!', datetime.now())


def sync_obligatory_borrower_info():
    """同步 债权表借款人用户ID，客户ID"""
    update(syncObligatoryBorrowerInfoSQL)
    print('sync_obligatory_borrower_info Finish!', datetime.now())


def calc_bid():
    print('开始时间:', datetime.now())
    update_bid_platform_name()
    calc_flowed_bid_time()
    calc_request_time()
    calc_granted_time()
    calc_lended_bid_time()
    calc_raise_duration()
    calc_should_repay_time()
    calc_granted_amount()
    calc_repayed_amount()
    calc_balance_amount()
    calc_close_bid_status()
    sync_obligatory_borrower_info()
    print('结束时间:', datetime.now())


if __name__ == '__main__':
    calc_bid()
