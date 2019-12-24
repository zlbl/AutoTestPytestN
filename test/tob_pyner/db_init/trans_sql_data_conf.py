"""

Configuration file for migrating Oracle..

"""

from test.tob_pyner.db_init.sqls.ucfSQL import *
from test.tob_pyner.db_init.sqls.lanmaoSQL import *

'''Oracle配置信息 参数1 为先锋库配置信息  参数2 为懒猫库配置信息'''
oracle_auths = [('B2B_PYNER_UCFLOAN', 'oracle', '192.168.5.164', '1521',
                 'db11g'),
                ('b2b_pyner_lanmaoloan', 'oracle', '192.168.5.164', '1521',
                 'db11g')]

# 每次批量处理多少条数据
batch_num = 2000

'''0为先锋  1 为懒猫'''
db_select = 0
# db_select = 1

'''选择割接的数据库 可单个执行 也可多个串行执行'''
sqls_ucf = [
    # (ucfUserSQL, "pyner_user"),
    # (ucfUserPersonSQL, "pyner_user_person"),
    # (ucfUserEnterpriseSQL, "pyner_user_enterprise"),
    # (ucfPlatformSQL, "pyner_platform"),
    (ucfAccountSQL, "pyner_account_test"),
    # (ucfBidSQL, "pyner_bid"),
    # (ucfObligatorySQL, "pyner_obligatory"),
    # (ucfTradeSQL, "pyner_trade"),
    # (ucfTradeOrderSQL, "pyner_trade_order")
]

sqls_lanmao = [
    # (lanmaoUserPersonSQL, "pyner_user"),
    # (lanmaoUserEnterpriseSQL, "pyner_user"),
    # (lanmaoPersonSQL, "pyner_user_person"),
    # (lanmaoEnterpriseSQL, "pyner_user_enterprise"),
    # (lanmaoPlatformSQL, "pyner_platform"),
    # (lanmaoAccountSQL, "pyner_account"),
    # (lanmaoBidSQL, "pyner_bid"),
    # (lanmaoObligatorySQL, "pyner_obligatory"),
    # # # 非充值、提现、还款交易
    # (lanmaoTradeSQL, "pyner_trade"),
    # # # 充值交易
    # (lanmaoRechargeTradeSQL, "pyner_trade"),
    # # # 提现交易
    # (lanmaoWithdrawTradeSQL, "pyner_trade"),
    # # # 还本金交易
    # (lanmaoPrincipleRepaymentTradeSQL, "pyner_trade"),
    # # # 还利息交易
    # (lanmaoInterestRepaymentTradeSQL, "pyner_trade")
]
