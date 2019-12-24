from test.tob_pyner.fill_fields.bin.init.sqls.deal_info_report_sql import *
from test.tob_pyner.fill_fields.util.MySqlHelper import *


def init_raise_duration_report():
    """初始化标的募集期报表"""
    select_insert(initRaiseDurationSQL)
    print('init_deal_information_report Finish!')


def init_flowed_count_report():
    """初始化标的流标率报表"""
    update(initFlowedCountSQL)
    print('init_init_flowed_count_report Finish!')


def init_entrusted_count_report():
    """初始化标的受托数报表"""
    update(initEntrustedCountSQL)
    print('init_entrusted_count_report Finish!')


def init_deal_amount_report():
    """初始化成交金额分布报表"""
    select_insert(initDealAmountSQL)
    print('init_deal_amount_report Finish!')


def init_deal_info_report():
    init_raise_duration_report()
    init_flowed_count_report()
    init_entrusted_count_report()
    init_deal_amount_report()


if __name__ == '__main__':
    init_deal_info_report()
