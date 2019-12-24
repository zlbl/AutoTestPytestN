initRaiseDurationSQL = '''
INSERT INTO b2b_pyner_statistic.pyner_report_deal_information (raise_duration,
                                                                   bid_count,
                                                                   bank_platform_id,
                                                                   depository_id,
                                                                   saas_id,
                                                                   finish_time,
                                                                   flowed_count,
                                                                   entrusted_pay_count,
                                                                   date_type,
                                                                   create_time,
                                                                   last_update_time,
                                                                   state)
select sum(pynerBid.raise_duration)     raise_duration,
       count(pynerBid.bank_platform_id) bid_count,
       pynerBid.bank_platform_id        bank_platform_id,
       pynerBid.depository_id           depository_id,
       pynerBid.saas_id                 saas_id,
       '1970-01-02 00:00:00'            finish_time,
       0                                flowed_count,
       0                                entrusted_pay_count,
       'day'                            date_type,
       now()                            create_time,
       now()                            last_update_time,
       'U'                              state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.finish_time < '2018-12-16'
  and pynerBid.state = 'U'
group by bank_platform_id, depository_id, saas_id'''

initFlowedCountSQL = '''
update b2b_pyner_statistic.pyner_report_deal_information i
set i.flowed_count     = (select count(pynerBid.bank_platform_id) countNum
                          from b2b_pyner_depository.pyner_bid pynerBid
                          where pynerBid.flowed_time < '2018-12-16'
                            and pynerBid.state = 'U'
                            and pynerBid.bank_platform_id = i.bank_platform_id
                            and pynerBid.depository_id = i.depository_id
                            and pynerBid.saas_id = i.saas_id),
    i.last_update_time = now()
where i.finish_time = '1970-01-02 00:00:00'
'''

initEntrustedCountSQL = '''
update b2b_pyner_statistic.pyner_report_deal_information i
set i.entrusted_pay_count = (select count(pynerBid.bank_platform_id) countNum
                             from b2b_pyner_depository.pyner_bid pynerBid
                             where pynerBid.finish_time < '2018-12-16'
                               and pynerBid.entrusted_pay = '1'
                               and pynerBid.state = 'U'
                               and pynerBid.bank_platform_id = i.bank_platform_id
                               and pynerBid.depository_id = i.depository_id
                               and pynerBid.saas_id = i.saas_id),
    i.last_update_time    = now()
where i.finish_time = '1970-01-02 00:00:00'
'''

initDealAmountSQL = '''
INSERT INTO b2b_pyner_statistic.pyner_report_deal_amount (saas_id,
                                                          bank_platform_id,
                                                          depository_id,
                                                          finish_time,
                                                          amount,
                                                          user_type,
                                                          date_type,
                                                          create_time,
                                                          last_update_time,
                                                          state)
select pynerBid.saas_id          saas_id,
       pynerBid.bank_platform_id bank_platform_id,
       pynerBid.depository_id    depository_id,
       '1970-01-02 00:00:00'     finish_time,
       sum(pynerBid.amount)      amount,
       pynerBid.user_type        user_type,
       'day'                     date_type,
       now()                     create_time,
       now()                     last_update_time,
       'U'                       state
from b2b_pyner_depository.pyner_bid pynerBid
where pynerBid.finish_time < '2018-12-16'
  and pynerBid.state = 'U'
  and pynerBid.user_type in ('Person', 'Enterprise')
group by bank_platform_id, depository_id, saas_id, user_type
'''
