from test.tob_pyner.fill_fields.bin.init.sqls.assert_quality_sql import *
from test.tob_pyner.fill_fields.util.MySqlHelper import select_insert


def init_should_repay_assert_period_range_report():
    """资产质量-已到期资产期限分布报表"""
    # 1天-30天
    select_insert(initShouldRepayAssertPeriodRangeSQL1.format(1, 30))
    # 30天-90天
    select_insert(initShouldRepayAssertPeriodRangeSQL1.format(30, 90))
    # 90天-180天
    select_insert(initShouldRepayAssertPeriodRangeSQL1.format(90, 180))
    # 180天-
    select_insert(initShouldRepayAssertPeriodRangeSQL2.format(180))
    print('init_assert_period_range_report Finish!')


def init_should_repay_assert_rate_range_report():
    """资产质量-已到期资产期限分布报表"""
    # 0%-6%
    select_insert(initShouldRepayAssertRateRangeSQL1.format(0, 0.06))
    # 6%-10%
    select_insert(initShouldRepayAssertRateRangeSQL1.format(0.06, 0.1))
    # 10%-15%
    select_insert(initShouldRepayAssertRateRangeSQL1.format(0.1, 0.15))
    # 15%以上
    select_insert(initShouldRepayAssertRateRangeSQL2.format(0.15))
    print('init_assert_rate_range_report Finish!')


def init_should_repay_assert_amount_range_report():
    """资产质量-已到期标的金额分布报表"""
    # 小于100元
    select_insert(initShouldRepayAssertAmountRangeSQL0.format(100))
    # 100-500元
    select_insert(initShouldRepayAssertAmountRangeSQL1.format(100, 500))
    # 500-1000元
    select_insert(initShouldRepayAssertAmountRangeSQL1.format(500, 1000))
    # 大于1000元
    select_insert(initShouldRepayAssertAmountRangeSQL2.format(1000))
    print('init_should_repay_assert_amount_range_report Finish!')


def init_should_repay_compensation_report():
    # TODO 未测试
    """逾期表现-代偿金额"""
    select_insert(initShouldRepayCompensationSQL)
    print('init_should_repay_compensation_report Finish!')


def init_should_repay_compensation_repayed_report():
    # TODO 未测试
    """逾期表现-还代偿金额"""
    select_insert(initShouldRepayCompensationRepayedSQL)
    print('init_should_repay_compensation_repayed_report Finish!')


def init_overdue_repayed_report():
    # TODO 未测试
    """逾期表现-逾期还款金额"""
    select_insert(initOverdueRepayedSQL)
    print('init_overdue_repayed_report Finish!')


def init_overdue_bid_amount_report():
    # TODO 未测试
    """逾期表现-所有标的金额"""
    select_insert(initOverdueBidAmountSQL)
    print('init_overdue_bid_amount_report Finish!')


def init_normal_repay_assert_period_range_report():
    # TODO 未测试
    """资产质量-正常还款资产期限分布报表"""
    # 1天-30天
    select_insert(initNormalRepayAssertPeriodRangeSQL1.format(1, 30))
    # 30天-90天
    select_insert(initNormalRepayAssertPeriodRangeSQL1.format(30, 90))
    # 90天-180天
    select_insert(initNormalRepayAssertPeriodRangeSQL1.format(90, 180))
    # 180天-
    select_insert(initNormalRepayAssertPeriodRangeSQL2.format(180))
    print('init_normal_repay_assert_period_range_report Finish!')


def init_normal_repay_assert_rate_range_report():
    # TODO 未测试
    """资产质量-正常还款资产期限分布报表"""
    # 0%-6%
    select_insert(initNormalRepayAssertRateRangeSQL1.format(0, 0.06))
    # 6%-10%
    select_insert(initNormalRepayAssertRateRangeSQL1.format(0.06, 0.1))
    # 10%-15%
    select_insert(initNormalRepayAssertRateRangeSQL1.format(0.1, 0.15))
    # 15%以上
    select_insert(initNormalRepayAssertRateRangeSQL2.format(0.15))
    print('init_normal_repay_assert_rate_range_report Finish!')


def init_normal_repay_assert_amount_range_report():
    # TODO 未测试
    """资产质量-正常还款标的金额分布报表"""
    # 小于100元
    select_insert(initNormalRepayAssertAmountRangeSQL0.format(100))
    # 100-500元
    select_insert(initNormalRepayAssertAmountRangeSQL1.format(100, 500))
    # 500-1000元
    select_insert(initNormalRepayAssertAmountRangeSQL1.format(500, 1000))
    # 大于1000元
    select_insert(initNormalRepayAssertAmountRangeSQL2.format(1000))
    print('init_normal_repay_assert_amount_range_report Finish!')


def init_overdue_repay_assert_period_range_report():
    # TODO 未测试
    """资产质量-逾期还款资产期限分布报表"""
    # 1天-30天
    select_insert(initOverdueRepayAssertPeriodRangeSQL1.format(1, 30))
    # 30天-90天
    select_insert(initOverdueRepayAssertPeriodRangeSQL1.format(30, 90))
    # 90天-180天
    select_insert(initOverdueRepayAssertPeriodRangeSQL1.format(90, 180))
    # 180天-
    select_insert(initOverdueRepayAssertPeriodRangeSQL2.format(180))
    print('init_overdue_repay_assert_period_range_report Finish!')


def init_overdue_repay_assert_rate_range_report():
    # TODO 未测试
    """资产质量-逾期还款资产期限分布报表"""
    # 0%-6%
    select_insert(initOverdueRepayAssertRateRangeSQL1.format(0, 0.06))
    # 6%-10%
    select_insert(initOverdueRepayAssertRateRangeSQL1.format(0.06, 0.1))
    # 10%-15%
    select_insert(initOverdueRepayAssertRateRangeSQL1.format(0.1, 0.15))
    # 15%以上
    select_insert(initOverdueRepayAssertRateRangeSQL2.format(0.15))
    print('init_overdue_repay_assert_rate_range_report Finish!')


def init_overdue_repay_assert_amount_range_report():
    # TODO 未测试
    """资产质量-逾期还款标的金额分布报表"""
    # 小于100元
    select_insert(initOverdueRepayAssertAmountRangeSQL0.format(100))
    # 100-500元
    select_insert(initOverdueRepayAssertAmountRangeSQL1.format(100, 500))
    # 500-1000元
    select_insert(initOverdueRepayAssertAmountRangeSQL1.format(500, 1000))
    # 大于1000元
    select_insert(initOverdueRepayAssertAmountRangeSQL2.format(1000))
    print('init_overdue_repay_assert_amount_range_report Finish!')


def init_assert_quality_report():
    init_should_repay_assert_period_range_report()
    init_should_repay_assert_rate_range_report()
    init_should_repay_assert_amount_range_report()
    init_should_repay_compensation_report()
    init_should_repay_compensation_repayed_report()
    init_overdue_repayed_report()
    init_overdue_bid_amount_report()
    init_normal_repay_assert_period_range_report()
    init_normal_repay_assert_rate_range_report()
    init_normal_repay_assert_amount_range_report()
    init_overdue_repay_assert_period_range_report()
    init_overdue_repay_assert_rate_range_report()
    init_overdue_repay_assert_amount_range_report()


if __name__ == '__main__':
    init_assert_quality_report()
