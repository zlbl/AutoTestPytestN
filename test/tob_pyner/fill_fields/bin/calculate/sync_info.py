from test.tob_pyner.fill_fields.bin.calculate.sqls.sync_sql import *
from test.tob_pyner.fill_fields.util.MySqlHelper import update

def update_trade_order_info():
    """更新交易订单表信息"""
    update(updateLanmaotradeOrderInfo)
    update(updateTradeOrderInfo)
    print('update_trade_order_info Finish!')

def sync_platform_name_info():
    """同步交易表 平台名称"""
    update(syncPlatformNameSQL)
    print('sync_platform_name_info Finish!')


def sync_trans_location_info():
    """同步 交易表-平台名称,出款方-归属地code(省市区)，出款方-归属地名称"""
    update(syncTransLocationInfoSQL)
    print('sync_trans_location_info Finish!')


def sync_trans_code_type_info():
    """同步 交易表-内部交易码类别"""
    update(syncTransCodeTypeInfoOfRechargeSQL)
    update(syncTransCodeTypeInfoOfWithdrawSQL)
    update(syncTransCodeTypeInfoOfTransferSQL)
    print('sync_trans_code_type_info Finish!')


def calc_last_trade_time():
    """设置最后交易时间"""
    update(calcLastTradeTimeSQL)
    update(calcReportLastTradeTimeSQL)
    print('calc_last_trade_time Finish!')


def calc_repayed_normal_amount():
    """设置正常还款金额"""
    update(calcRepayedNormalAmountSQL)
    print('calc_repayed_normal_amount Finish!')


def calc_repayed_normal_interest():
    """设置正常还款利息"""
    update(calcRepayedNormalInterestSQL)
    print('calc_repayed_normal_interest Finish!')


def calc_compensation_direct_amount():
    """设置直接代偿还款金额"""
    update(calcCompensationDirectAmountSQL)
    print('calc_compensation_direct_amount Finish!')


def calc_compensation_direct_interest():
    """设置直接代偿还款利息"""
    update(calcCompensationDirectInterestSQL)
    print('calc_compensation_direct_interest Finish!')


def calc_compensation_indirect_amount():
    """设置间接代偿还款金额"""
    update(calcCompensationIndirectAmountSQL)
    print('calc_compensation_indirect_amount Finish!')


def calc_compensation_indirect_interest():
    """设置直接代偿还款利息"""
    update(calcCompensationIndirectInterestSQL)
    print('calc_compensation_indirect_interest Finish!')


def calc_compensation_overdue_amount():
    """设置过还款日还代偿款金额"""
    update(calcCompensationOverdueAmountSQL)
    print('calc_compensation_overdue_amount Finish!')


def calc_compensation_overdue_interest():
    """设置过还款日还代偿款利息"""
    update(calcCompensationOverdueInterestSQL)
    print('calc_compensation_overdue_interest Finish!')


def calc_bid_service_amount():
    """设置标的服务费"""
    update(calcBidServiceAmountSQL)
    print('calc_bid_service_amount Finish!')


def calc_compensation_repayed_amount_interest():
    """设置还代偿还款额、利息"""
    update(calcCompensationRepayedAmountInterestSQL)
    print('calc_compensation_repayed_amount_interest Finish!')


def calc_overdue_time_and_amount():
    """设置逾期时间、逾期金额"""
    update(calcOverdueTimeAndAmount)
    print('calc_overdue_time_and_amount Finish!')


def calc_compensation_amount():
    """设置逾期还款余额"""
    update(calcCompensationAmountSQL)
    print('calc_compensation_amount Finish!')


def calc_repayed_interest():
    """设置先锋还款利息累加"""
    update(calcRepayedInterestSQL)
    print('calc_repayed_interest Finish!')


def calc_comprehensive_rate():
    """设置综合费率"""
    update(calcComprehensiveRateSQL)
    print('calc_comprehensive_rate Finish!')


def update_obligatory_bid_info():
    """更新债券标的信息"""
    update(updateObligatoryBidInfoSQL)
    print('update_obligatory_bid_info Finish!')


def sync_info():
    update_trade_order_info()
    sync_platform_name_info()
    sync_trans_location_info()
    sync_trans_code_type_info()
    calc_last_trade_time()
    calc_repayed_normal_amount()
    calc_repayed_normal_interest()
    calc_compensation_direct_amount()
    calc_compensation_direct_interest()
    calc_compensation_indirect_amount()
    calc_compensation_indirect_interest()
    calc_compensation_overdue_amount()
    calc_compensation_overdue_interest()
    calc_bid_service_amount()
    calc_compensation_repayed_amount_interest()
    calc_overdue_time_and_amount()
    calc_compensation_amount()
    calc_repayed_interest()
    calc_comprehensive_rate()
    update_obligatory_bid_info()


if __name__ == '__main__':
    sync_info()
