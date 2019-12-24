initShouldRepayAssertPeriodRangeSQL1 = '''
INSERT INTO b2b_pyner_statistic.pyner_report_asset_quality_period_range (should_repay,
                                                                             saas_id,
                                                                             bank_platform_id,
                                                                             depository_id,
                                                                             amount,
                                                                             should_repay_time,
                                                                             period_range,
                                                                             count_num,
                                                                             date_type,
                                                                             create_time,
                                                                             last_update_time,
                                                                             state)
select 0                                should_repay,
       pynerBid.saas_id                 saas_id,
       pynerBid.bank_platform_id        bank_platform_id,
       pynerBid.depository_id           depository_id,
       SUM(pynerBid.amount)             amount,
       '1970-01-02 00:00:00'            should_repay_time,
       '{0}-{1}天'                          period_range,
       COUNT(pynerBid.bank_platform_id) count_num,
       'day'                            date_type,
       now()                            create_time,
       now()                            last_update_time,
       'U'                              state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.state = 'U'
  and pynerBid.period >= {0}
  and pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.period < {1}
group by bank_platform_id, depository_id, saas_id
'''

initShouldRepayAssertPeriodRangeSQL2 = '''
INSERT INTO b2b_pyner_statistic.pyner_report_asset_quality_period_range (should_repay,
                                                                             saas_id,
                                                                             bank_platform_id,
                                                                             depository_id,
                                                                             amount,
                                                                             should_repay_time,
                                                                             period_range,
                                                                             count_num,
                                                                             date_type,
                                                                             create_time,
                                                                             last_update_time,
                                                                             state)
select 0                                should_repay,
       pynerBid.saas_id                 saas_id,
       pynerBid.bank_platform_id        bank_platform_id,
       pynerBid.depository_id           depository_id,
       SUM(pynerBid.amount)             amount,
       '1970-01-02 00:00:00'            should_repay_time,
       '{0}天以上'                          period_range,
       COUNT(pynerBid.bank_platform_id) count_num,
       'day'                            date_type,
       now()                            create_time,
       now()                            last_update_time,
       'U'                              state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.state = 'U'
  and pynerBid.period >= {0}
  and pynerBid.should_repay_time < '2018-12-16'
group by bank_platform_id, depository_id, saas_id
'''

initShouldRepayAssertRateRangeSQL1 = '''
INSERT INTO b2b_pyner_statistic.pyner_report_asset_quality_rate_range (should_repay,
                                                                       saas_id,
                                                                       bank_platform_id,
                                                                       depository_id,
                                                                       amount,
                                                                       should_repay_time,
                                                                       rate_range,
                                                                       count_num,
                                                                       date_type,
                                                                       create_time,
                                                                       last_update_time,
                                                                       state)
select 0                                should_repay,
       pynerBid.saas_id                 saas_id,
       pynerBid.bank_platform_id        bank_platform_id,
       pynerBid.depository_id           depository_id,
       SUM(pynerBid.amount)             amount,
       '1970-01-02 00:00:00'            should_repay_time,
       '{0:.0%}-{1:.0%}'                          rate_range,
       COUNT(pynerBid.bank_platform_id) count_num,
       'day'                            date_type,
       now()                            create_time,
       now()                            last_update_time,
       'U'                              state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.state = 'U'
  and pynerBid.rate >= {0}
  and pynerBid.rate < {1}
  and pynerBid.should_repay_time < '2018-12-16'
group by bank_platform_id, depository_id, saas_id
'''

initShouldRepayAssertRateRangeSQL2 = '''
INSERT INTO b2b_pyner_statistic.pyner_report_asset_quality_rate_range (should_repay,
                                                                       saas_id,
                                                                       bank_platform_id,
                                                                       depository_id,
                                                                       amount,
                                                                       should_repay_time,
                                                                       rate_range,
                                                                       count_num,
                                                                       date_type,
                                                                       create_time,
                                                                       last_update_time,
                                                                       state)
select 0                                should_repay,
       pynerBid.saas_id                 saas_id,
       pynerBid.bank_platform_id        bank_platform_id,
       pynerBid.depository_id           depository_id,
       SUM(pynerBid.amount)             amount,
       '1970-01-02 00:00:00'            should_repay_time,
       '{0:.0%}以上'                          rate_range,
       COUNT(pynerBid.bank_platform_id) count_num,
       'day'                            date_type,
       now()                            create_time,
       now()                            last_update_time,
       'U'                              state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.state = 'U'
  and pynerBid.rate >= {0}
  and pynerBid.should_repay_time < '2018-12-16'
group by bank_platform_id, depository_id, saas_id
'''

initShouldRepayAssertAmountRangeSQL0 = '''
INSERT INTO b2b_pyner_statistic.pyner_report_asset_quality_amount_range (should_repay,
                                                                         saas_id,
                                                                         bank_platform_id,
                                                                         depository_id,
                                                                         amount,
                                                                         should_repay_time,
                                                                         amount_range,
                                                                         count_num,
                                                                         date_type,
                                                                         create_time,
                                                                         last_update_time,
                                                                         state)
select 0                                should_repay,
       pynerBid.saas_id                 saas_id,
       pynerBid.bank_platform_id        bank_platform_id,
       pynerBid.depository_id           depository_id,
       SUM(pynerBid.amount)             amount,
       '1970-01-02 00:00:00'            should_repay_time,
       '小于{0}元'                         amount_range,
       COUNT(pynerBid.bank_platform_id) count_num,
       'day'                            date_type,
       now()                            create_time,
       now()                            last_update_time,
       'U'                              state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.state = 'U'
  and pynerBid.amount >= 0
  and pynerBid.amount < {0}
  and pynerBid.should_repay_time < '2018-12-16'
group by bank_platform_id, depository_id, saas_id'''

initShouldRepayAssertAmountRangeSQL1 = '''
INSERT INTO b2b_pyner_statistic.pyner_report_asset_quality_amount_range (should_repay,
                                                                         saas_id,
                                                                         bank_platform_id,
                                                                         depository_id,
                                                                         amount,
                                                                         should_repay_time,
                                                                         amount_range,
                                                                         count_num,
                                                                         date_type,
                                                                         create_time,
                                                                         last_update_time,
                                                                         state)
select 0                                should_repay,
       pynerBid.saas_id                 saas_id,
       pynerBid.bank_platform_id        bank_platform_id,
       pynerBid.depository_id           depository_id,
       SUM(pynerBid.amount)             amount,
       '1970-01-02 00:00:00'            should_repay_time,
       '{0}-{1}元'                       amount_range,
       COUNT(pynerBid.bank_platform_id) count_num,
       'day'                            date_type,
       now()                            create_time,
       now()                            last_update_time,
       'U'                              state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.state = 'U'
  and pynerBid.amount >= {0}
  and pynerBid.amount < {1}
  and pynerBid.should_repay_time < '2018-12-16'
group by bank_platform_id, depository_id, saas_id'''

initShouldRepayAssertAmountRangeSQL2 = '''
INSERT INTO b2b_pyner_statistic.pyner_report_asset_quality_amount_range (should_repay,
                                                                         saas_id,
                                                                         bank_platform_id,
                                                                         depository_id,
                                                                         amount,
                                                                         should_repay_time,
                                                                         amount_range,
                                                                         count_num,
                                                                         date_type,
                                                                         create_time,
                                                                         last_update_time,
                                                                         state)
select 0                                should_repay,
       pynerBid.saas_id                 saas_id,
       pynerBid.bank_platform_id        bank_platform_id,
       pynerBid.depository_id           depository_id,
       SUM(pynerBid.amount)             amount,
       '1970-01-02 00:00:00'            should_repay_time,
       '大于{0}元'                        amount_range,
       COUNT(pynerBid.bank_platform_id) count_num,
       'day'                            date_type,
       now()                            create_time,
       now()                            last_update_time,
       'U'                              state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.state = 'U'
  and pynerBid.amount >= {0}
  and pynerBid.should_repay_time < '2018-12-16'
group by bank_platform_id, depository_id, saas_id
'''

initShouldRepayCompensationSQL = '''
INSERT INTO b2b_pyner_statistic.pyner_report_asset_quality_compensation (saas_id,
                                                                         bank_platform_id,
                                                                         depository_id,
                                                                         should_repay_time,
                                                                         compensation_amount,
                                                                         count_num,
                                                                         date_type,
                                                                         create_time,
                                                                         last_update_time,
                                                                         state,
                                                                         should_repay)
select pynerBid.saas_id                  saas_id,
       pynerBid.bank_platform_id         bank_platform_id,
       pynerBid.depository_id            depository_id,
       '1970-01-02 00:00:00'             should_repay_time,
       SUM(pynerBid.compensation_amount) compensation_amount,
       COUNT(pynerBid.bank_platform_id)  count_num,
       'day'                             date_type,
       now()                             create_time,
       now()                             last_update_time,
       'U'                               state,
       0                                should_repay
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.state = 'U'
  and pynerBid.compensation_amount > 0
group by bank_platform_id, depository_id, saas_id'''

initShouldRepayCompensationRepayedSQL = '''
INSERT INTO b2b_pyner_statistic.pyner_report_asset_quality_compensation_repayed (saas_id,
                                                                                 bank_platform_id,
                                                                                 depository_id,
                                                                                 should_repay_time,
                                                                                 compensation_repayed_amount,
                                                                                 count_num,
                                                                                 date_type,
                                                                                 create_time,
                                                                                 last_update_time,
                                                                                 state,
                                                                                 should_repay)
select pynerBid.saas_id                          saas_id,
       pynerBid.bank_platform_id                 bank_platform_id,
       pynerBid.depository_id                    depository_id,
       '1970-01-02 00:00:00'                     should_repay_time,
       SUM(pynerBid.compensation_repayed_amount) compensation_repayed_amount,
       COUNT(pynerBid.bank_platform_id)          count_num,
       'day'                                     date_type,
       now()                                     create_time,
       now()                                     last_update_time,
       'U'                                       state,
       0                                should_repay
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.compensation_repayed_amount > 0
  and pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.state = 'U'
group by bank_platform_id, depository_id, saas_id'''

initOverdueRepayedSQL = '''
INSERT INTO b2b_pyner_statistic.pyner_report_asset_quality_repayed (saas_id,
                                                                    bank_platform_id,
                                                                    depository_id,
                                                                    should_repay_time,
                                                                    repayed_overdue_amount,
                                                                    count_num,
                                                                    date_type,
                                                                    create_time,
                                                                    last_update_time,
                                                                    state,
                                                                    should_repay)
select pynerBid.saas_id                     saas_id,
       pynerBid.bank_platform_id            bank_platform_id,
       pynerBid.depository_id               depository_id,
       '1970-01-02 00:00:00'                should_repay_time,
       SUM(pynerBid.repayed_overdue_amount) repayed_overdue_amount,
       COUNT(pynerBid.bank_platform_id)     count_num,
       'day'                                date_type,
       now()                                create_time,
       now()                                last_update_time,
       'U'                                  state,
       0                                should_repay
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.overdue_time is not null
  and pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.state = 'U'
group by bank_platform_id, depository_id, saas_id'''

initOverdueBidAmountSQL = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_amount (saas_id,
                                                                   bank_platform_id,
                                                                   depository_id,
                                                                   should_repay_time,
                                                                   amount,
                                                                   count_num,
                                                                   date_type,
                                                                   create_time,
                                                                   last_update_time,
                                                                   state,
                                                                   should_repay)
select pynerBid.saas_id                 saas_id,
       pynerBid.bank_platform_id        bank_platform_id,
       pynerBid.depository_id           depository_id,
       '1970-01-02 00:00:00'            should_repay_time,
       SUM(pynerBid.amount)             amount,
       COUNT(pynerBid.bank_platform_id) count_num,
       'day'                            date_type,
       now()                            create_time,
       now()                            last_update_time,
       'U'                              state,
       0                                should_repay
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.state = 'U'
group by bank_platform_id, depository_id, saas_id'''

initNormalRepayAssertPeriodRangeSQL1 = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_period_range (should_repay,
                                                                         saas_id,
                                                                         bank_platform_id,
                                                                         depository_id,
                                                                         amount,
                                                                         should_repay_time,
                                                                         period_range,
                                                                         count_num,
                                                                         date_type,
                                                                         create_time,
                                                                         last_update_time,
                                                                         state)
select 3                                   should_repay,
       pynerBid.saas_id                    saas_id,
       pynerBid.bank_platform_id           bank_platform_id,
       pynerBid.depository_id              depository_id,
       SUM(pynerBid.repayed_normal_amount) amount,
       '1970-01-02 00:00:00'               should_repay_time,
       '{0}-{1}天'                             period_range,
       COUNT(pynerBid.bank_platform_id)    count_num,
       'day'                               date_type,
       now()                               create_time,
       now()                               last_update_time,
       'U'                                 state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.period >= {0}
  and pynerBid.period < {1}
  and pynerBid.repayed_normal_amount > 0
  and pynerBid.state = 'U'
group by depository_id, bank_platform_id, saas_id'''

initNormalRepayAssertPeriodRangeSQL2 = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_period_range (should_repay,
                                                                         saas_id,
                                                                         bank_platform_id,
                                                                         depository_id,
                                                                         amount,
                                                                         should_repay_time,
                                                                         period_range,
                                                                         count_num,
                                                                         date_type,
                                                                         create_time,
                                                                         last_update_time,
                                                                         state)
select 3                                   should_repay,
       pynerBid.saas_id                    saas_id,
       pynerBid.bank_platform_id           bank_platform_id,
       pynerBid.depository_id              depository_id,
       SUM(pynerBid.repayed_normal_amount) amount,
       '1970-01-02 00:00:00'               should_repay_time,
       '{0}天以上'                            period_range,
       COUNT(pynerBid.bank_platform_id)    count_num,
       'day'                               date_type,
       now()                               create_time,
       now()                               last_update_time,
       'U'                                 state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.period >= {0}
  and pynerBid.repayed_normal_amount > 0
  and pynerBid.state = 'U'
group by depository_id, bank_platform_id, saas_id'''

initNormalRepayAssertRateRangeSQL1 = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_rate_range (should_repay,
                                                                       saas_id,
                                                                       bank_platform_id,
                                                                       depository_id,
                                                                       amount,
                                                                       should_repay_time,
                                                                       rate_range,
                                                                       count_num,
                                                                       date_type,
                                                                       create_time,
                                                                       last_update_time,
                                                                       state)
select 3                                   should_repay,
       pynerBid.saas_id                    saas_id,
       pynerBid.bank_platform_id           bank_platform_id,
       pynerBid.depository_id              depository_id,
       SUM(pynerBid.repayed_normal_amount) amount,
       '1970-01-02 00:00:00'               should_repay_time,
       '{0:.0%}-{1:.0%}'                             rate_range,
       COUNT(pynerBid.bank_platform_id)    count_num,
       'day'                               date_type,
       now()                               create_time,
       now()                               last_update_time,
       'U'                                 state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.rate >= {0}
  and pynerBid.rate < {1}
  and pynerBid.repayed_normal_amount > 0
  and pynerBid.state = 'U'
group by depository_id, bank_platform_id, saas_id'''

initNormalRepayAssertRateRangeSQL2 = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_rate_range (should_repay,
                                                                       saas_id,
                                                                       bank_platform_id,
                                                                       depository_id,
                                                                       amount,
                                                                       should_repay_time,
                                                                       rate_range,
                                                                       count_num,
                                                                       date_type,
                                                                       create_time,
                                                                       last_update_time,
                                                                       state)
select 3                                   should_repay,
       pynerBid.saas_id                    saas_id,
       pynerBid.bank_platform_id           bank_platform_id,
       pynerBid.depository_id              depository_id,
       SUM(pynerBid.repayed_normal_amount) amount,
       '1970-01-02 00:00:00'               should_repay_time,
       '{0:.0%}以上'                             rate_range,
       COUNT(pynerBid.bank_platform_id)    count_num,
       'day'                               date_type,
       now()                               create_time,
       now()                               last_update_time,
       'U'                                 state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.rate >= {0}
  and pynerBid.repayed_normal_amount > 0
  and pynerBid.state = 'U'
group by depository_id, bank_platform_id, saas_id
'''

initNormalRepayAssertAmountRangeSQL0 = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_amount_range (should_repay,
                                                                         saas_id,
                                                                         bank_platform_id,
                                                                         depository_id,
                                                                         amount,
                                                                         should_repay_time,
                                                                         amount_range,
                                                                         count_num,
                                                                         date_type,
                                                                         create_time,
                                                                         last_update_time,
                                                                         state)
select 3                                   should_repay,
       pynerBid.saas_id                    saas_id,
       pynerBid.bank_platform_id           bank_platform_id,
       pynerBid.depository_id              depository_id,
       SUM(pynerBid.repayed_normal_amount) amount,
       '1970-01-02 00:00:00'               should_repay_time,
       '小于{0}元'                            amount_range,
       COUNT(pynerBid.bank_platform_id)    count_num,
       'day'                               date_type,
       now()                               create_time,
       now()                               last_update_time,
       'U'                                 state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.amount >= 0
  and pynerBid.amount < {0}
  and pynerBid.repayed_normal_amount > 0
  and pynerBid.state = 'U'
group by bank_platform_id, depository_id, saas_id'''

initNormalRepayAssertAmountRangeSQL1 = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_amount_range (should_repay,
                                                                         saas_id,
                                                                         bank_platform_id,
                                                                         depository_id,
                                                                         amount,
                                                                         should_repay_time,
                                                                         amount_range,
                                                                         count_num,
                                                                         date_type,
                                                                         create_time,
                                                                         last_update_time,
                                                                         state)
select 3                                   should_repay,
       pynerBid.saas_id                    saas_id,
       pynerBid.bank_platform_id           bank_platform_id,
       pynerBid.depository_id              depository_id,
       SUM(pynerBid.repayed_normal_amount) amount,
       '1970-01-02 00:00:00'               should_repay_time,
       '{0}-{1}元'                          amount_range,
       COUNT(pynerBid.bank_platform_id)    count_num,
       'day'                               date_type,
       now()                               create_time,
       now()                               last_update_time,
       'U'                                 state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.amount >= {0}
  and pynerBid.amount < {1}
  and pynerBid.repayed_normal_amount > 0
  and pynerBid.state = 'U'
group by bank_platform_id, depository_id, saas_id'''

initNormalRepayAssertAmountRangeSQL2 = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_amount_range (should_repay,
                                                                         saas_id,
                                                                         bank_platform_id,
                                                                         depository_id,
                                                                         amount,
                                                                         should_repay_time,
                                                                         amount_range,
                                                                         count_num,
                                                                         date_type,
                                                                         create_time,
                                                                         last_update_time,
                                                                         state)
select 3                                   should_repay,
       pynerBid.saas_id                    saas_id,
       pynerBid.bank_platform_id           bank_platform_id,
       pynerBid.depository_id              depository_id,
       SUM(pynerBid.repayed_normal_amount) amount,
       '1970-01-02 00:00:00'               should_repay_time,
       '大于{0}元'                           amount_range,
       COUNT(pynerBid.bank_platform_id)    count_num,
       'day'                               date_type,
       now()                               create_time,
       now()                               last_update_time,
       'U'                                 state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.amount >= {0}
  and pynerBid.repayed_normal_amount > 0
  and pynerBid.state = 'U'
group by bank_platform_id, depository_id, saas_id'''

initOverdueRepayAssertPeriodRangeSQL1 = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_period_range (should_repay,
                                                                         saas_id,
                                                                         bank_platform_id,
                                                                         depository_id,
                                                                         amount,
                                                                         should_repay_time,
                                                                         period_range,
                                                                         count_num,
                                                                         date_type,
                                                                         create_time,
                                                                         last_update_time,
                                                                         state)
select 2                                    should_repay,
       pynerBid.saas_id                     saas_id,
       pynerBid.bank_platform_id            bank_platform_id,
       pynerBid.depository_id               depository_id,
       sum(pynerBid.repayed_overdue_amount) repayedOverdueAmount,
       '1970-01-02 00:00:00'                should_repay_time,
       '{0}-{1}天'                              period_range,
       count(pynerBid.bank_platform_id)     count_num,
       'day'                                date_type,
       now()                                create_time,
       now()                                last_update_time,
       'U'                                  state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.overdue_time is not null
  and pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.period >= {0}
  and pynerBid.period < {1}
  and pynerBid.state = 'U'
group by bank_platform_id, depository_id, saas_id'''

initOverdueRepayAssertPeriodRangeSQL2 = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_period_range (should_repay,
                                                                         saas_id,
                                                                         bank_platform_id,
                                                                         depository_id,
                                                                         amount,
                                                                         should_repay_time,
                                                                         period_range,
                                                                         count_num,
                                                                         date_type,
                                                                         create_time,
                                                                         last_update_time,
                                                                         state)
select 2                                    should_repay,
       pynerBid.saas_id                     saas_id,
       pynerBid.bank_platform_id            bank_platform_id,
       pynerBid.depository_id               depository_id,
       sum(pynerBid.repayed_overdue_amount) repayedOverdueAmount,
       '1970-01-02 00:00:00'                should_repay_time,
       '{0}天以上'                             period_range,
       count(pynerBid.bank_platform_id)     count_num,
       'day'                                date_type,
       now()                                create_time,
       now()                                last_update_time,
       'U'                                  state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.overdue_time is not null
  and pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.period >= {0}
  and pynerBid.state = 'U'
group by bank_platform_id, depository_id, saas_id'''

initOverdueRepayAssertRateRangeSQL1 = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_rate_range (should_repay,
                                                                       saas_id,
                                                                       bank_platform_id,
                                                                       depository_id,
                                                                       amount,
                                                                       should_repay_time,
                                                                       rate_range,
                                                                       count_num,
                                                                       date_type,
                                                                       create_time,
                                                                       last_update_time,
                                                                       state)
select 2                                    should_repay,
       pynerBid.saas_id                     saas_id,
       pynerBid.bank_platform_id            bank_platform_id,
       pynerBid.depository_id               depository_id,
       sum(pynerBid.repayed_overdue_amount) repayedOverdueAmount,
       '1970-01-02 00:00:00'                should_repay_time,
       '{0:.0%}-{1:.0%}'                              rate_range,
       COUNT(pynerBid.bank_platform_id)     count_num,
       'day'                                date_type,
       now()                                create_time,
       now()                                last_update_time,
       'U'                                  state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.overdue_time is not null
  and pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.rate >= {0}
  and pynerBid.rate < {1}
  and pynerBid.state = 'U'
group by depository_id, bank_platform_id, saas_id'''

initOverdueRepayAssertRateRangeSQL2 = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_rate_range (should_repay,
                                                                       saas_id,
                                                                       bank_platform_id,
                                                                       depository_id,
                                                                       amount,
                                                                       should_repay_time,
                                                                       rate_range,
                                                                       count_num,
                                                                       date_type,
                                                                       create_time,
                                                                       last_update_time,
                                                                       state)
select 2                                    should_repay,
       pynerBid.saas_id                     saas_id,
       pynerBid.bank_platform_id            bank_platform_id,
       pynerBid.depository_id               depository_id,
       sum(pynerBid.repayed_overdue_amount) repayedOverdueAmount,
       '1970-01-02 00:00:00'                should_repay_time,
       '{0:.0%}以上'                              rate_range,
       COUNT(pynerBid.bank_platform_id)     count_num,
       'day'                                date_type,
       now()                                create_time,
       now()                                last_update_time,
       'U'                                  state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.overdue_time is not null
  and pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.rate >= {0}
  and pynerBid.state = 'U'
group by depository_id, bank_platform_id, saas_id'''

initOverdueRepayAssertAmountRangeSQL0 = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_amount_range (should_repay,
                                                                         saas_id,
                                                                         bank_platform_id,
                                                                         depository_id,
                                                                         amount,
                                                                         should_repay_time,
                                                                         amount_range,
                                                                         count_num,
                                                                         date_type,
                                                                         create_time,
                                                                         last_update_time,
                                                                         state)
select 2                                    should_repay,
       pynerBid.saas_id                     saas_id,
       pynerBid.bank_platform_id            bank_platform_id,
       pynerBid.depository_id               depository_id,
       sum(pynerBid.repayed_overdue_amount) repayedOverdueAmount,
       '1970-01-02 00:00:00'                should_repay_time,
       '小于{0}元'                             amount_range,
       COUNT(pynerBid.bank_platform_id)     count_num,
       'day'                                date_type,
       now()                                create_time,
       now()                                last_update_time,
       'U'                                  state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.overdue_time is not null
  and pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.amount >= 0
  and pynerBid.amount < {0}
  and pynerBid.state = 'U'
group by bank_platform_id, depository_id, saas_id'''

initOverdueRepayAssertAmountRangeSQL1 = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_amount_range (should_repay,
                                                                         saas_id,
                                                                         bank_platform_id,
                                                                         depository_id,
                                                                         amount,
                                                                         should_repay_time,
                                                                         amount_range,
                                                                         count_num,
                                                                         date_type,
                                                                         create_time,
                                                                         last_update_time,
                                                                         state)
select 2                                    should_repay,
       pynerBid.saas_id                     saas_id,
       pynerBid.bank_platform_id            bank_platform_id,
       pynerBid.depository_id               depository_id,
       sum(pynerBid.repayed_overdue_amount) repayedOverdueAmount,
       '1970-01-02 00:00:00'                should_repay_time,
       '{0}-{1}元'                           amount_range,
       COUNT(pynerBid.bank_platform_id)     count_num,
       'day'                                date_type,
       now()                                create_time,
       now()                                last_update_time,
       'U'                                  state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.overdue_time is not null
  and pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.amount >= {0}
  and pynerBid.amount < {1}
  and pynerBid.state = 'U'
group by bank_platform_id, depository_id, saas_id'''

initOverdueRepayAssertAmountRangeSQL2 = '''
insert INTO b2b_pyner_statistic.pyner_report_asset_quality_amount_range (should_repay,
                                                                         saas_id,
                                                                         bank_platform_id,
                                                                         depository_id,
                                                                         amount,
                                                                         should_repay_time,
                                                                         amount_range,
                                                                         count_num,
                                                                         date_type,
                                                                         create_time,
                                                                         last_update_time,
                                                                         state)
select 2                                    should_repay,
       pynerBid.saas_id                     saas_id,
       pynerBid.bank_platform_id            bank_platform_id,
       pynerBid.depository_id               depository_id,
       sum(pynerBid.repayed_overdue_amount) repayedOverdueAmount,
       '1970-01-02 00:00:00'                should_repay_time,
       '大于{0}元'                            amount_range,
       COUNT(pynerBid.bank_platform_id)     count_num,
       'day'                                date_type,
       now()                                create_time,
       now()                                last_update_time,
       'U'                                  state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.overdue_time is not null
  and pynerBid.should_repay_time < '2018-12-16'
  and pynerBid.amount >= {0}
  and pynerBid.state = 'U'
group by bank_platform_id, depository_id, saas_id'''
