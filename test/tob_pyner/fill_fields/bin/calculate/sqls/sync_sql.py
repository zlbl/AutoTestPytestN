updateLanmaotradeOrderInfo = '''
update pyner_trade, pyner_trade_order
set pyner_trade.bank_bid_id = pyner_trade_order.bid_id,
	  pyner_trade.request_time = pyner_trade_order.procession_time,
		pyner_trade.finished_time = pyner_trade_order.finished_time,
		pyner_trade.finished_date = pyner_trade_order.finished_time
where pyner_trade.bank_order_id = pyner_trade_order.bank_order_id
  and pyner_trade.bank_platform_id = pyner_trade_order.bank_platform_id
  and pyner_trade.depository_id = pyner_trade_order.depository_id
	and pyner_trade.depository_id = '1000000002';
'''

updateTradeOrderInfo = '''
update pyner_trade t , pyner_trade_order o
set t.order_trans_code = o.trans_code,
    t.order_sub_trans_code = o.sub_trans_code,
    t.order_traning_code = o.sub_trans_code
where t.bank_order_id = o.bank_order_id
  and t.bank_platform_id = o.bank_platform_id
  and t.depository_id = o.depository_id;'''

syncPlatformNameSQL = '''
update pyner_trade t, pyner_platform p
set t.platform_name = p.platform_name
where t.depository_id = p.depository_id
  and t.bank_platform_id = p.bank_platform_id
'''

syncTransLocationInfoSQL = '''
update pyner_trade, pyner_user
set pyner_trade.belonging_code = concat(province_code, city_code, area_code),
    belonging_name             = concat(province_name, city_name, area_name)
where pyner_trade.depository_id = pyner_user.depository_id
  and pyner_trade.bank_platform_id = pyner_user.bank_platform_id
  and pyner_trade.pay_bank_user_id = pyner_user.bank_user_id;'''

syncTransCodeTypeInfoOfRechargeSQL = '''
update pyner_trade
set trans_code_type = '1000'
where traning_code in
      ('1000', '1001', '1002', '1003', '1004', '1006', '1005', '1021', '1007', '1008', '1011', '1012', '1013', '1015', '7007', '7009')'''

syncTransCodeTypeInfoOfWithdrawSQL = '''
update pyner_trade
set trans_code_type = '2000'
where traning_code in ('2002', '2008', '2019', '2011', '2016', '2018', '2020', '7500')'''

syncTransCodeTypeInfoOfTransferSQL = '''
update pyner_trade set trans_code_type='3100' where traning_code='3022'
'''

calcLastTradeTimeSQL = '''
update pyner_user left join (select pyner_trade.depository_id,
                                    pyner_trade.bank_platform_id,
                                    pyner_trade.pay_bank_user_id,
                                    max(pyner_trade.finished_time) last_trade_time
                             from pyner_trade
                             where pay_bank_user_id is not null 
                               and order_status = 'Success'
                               and finished_time is not null
                             group by pyner_trade.depository_id, pyner_trade.bank_platform_id,
                                      pyner_trade.pay_bank_user_id) pyner_trade on
  pyner_user.depository_id = pyner_trade.depository_id and pyner_user.bank_platform_id = pyner_trade.bank_platform_id
  and pyner_user.bank_user_id = pyner_trade.pay_bank_user_id
set pyner_user.last_trade_time = pyner_trade.last_trade_time'''

calcReportLastTradeTimeSQL = '''
update pyner_user_report left join pyner_user on pyner_user.depository_id = pyner_user_report.depository_id and
                                                 pyner_user.bank_platform_id = pyner_user_report.bank_platform_id and
                                                 pyner_user.bank_user_id = pyner_user_report.bank_user_id
set pyner_user_report.last_trade_time = pyner_user.last_trade_time
'''

calcRepayedNormalAmountSQL = '''
update pyner_bid left join (select depository_id, bank_platform_id, bank_bid_id, sum(ifnull(amount, 0)) amount
                            from pyner_trade
                            where order_traning_code = 7002
                              and traning_code = 7200
                              and order_status = 'Success'
                            group by depository_id, bank_platform_id, bank_bid_id) pyner_trade on
  pyner_bid.depository_id = pyner_trade.depository_id and pyner_bid.bank_platform_id = pyner_trade.bank_platform_id and
  pyner_bid.bank_bid_id = pyner_trade.bank_bid_id
set pyner_bid.repayed_normal_amount = pyner_trade.amount'''

calcRepayedNormalInterestSQL = '''
update pyner_bid left join (select depository_id, bank_platform_id, bank_bid_id, sum(ifnull(amount, 0)) amount
                            from pyner_trade
                            where order_traning_code = 7002
                              and traning_code = 7300
                              and order_status = 'Success'
                            group by depository_id, bank_platform_id, bank_bid_id) pyner_trade on
  pyner_bid.depository_id = pyner_trade.depository_id and pyner_bid.bank_platform_id = pyner_trade.bank_platform_id and
  pyner_bid.bank_bid_id = pyner_trade.bank_bid_id
set pyner_bid.repayed_normal_interest = pyner_trade.amount'''

calcCompensationDirectAmountSQL = '''
update pyner_bid left join (select depository_id, bank_platform_id, bank_bid_id, sum(ifnull(amount, 0)) amount
                            from pyner_trade
                            where order_traning_code = 7006
                              and traning_code = 7200
                              and order_status = 'Success'
                            group by depository_id, bank_platform_id, bank_bid_id) pyner_trade on
  pyner_bid.depository_id = pyner_trade.depository_id and pyner_bid.bank_platform_id = pyner_trade.bank_platform_id and
  pyner_bid.bank_bid_id = pyner_trade.bank_bid_id
set pyner_bid.compensation_direct_amount = pyner_trade.amount'''

calcCompensationDirectInterestSQL = '''
update pyner_bid left join (select depository_id, bank_platform_id, bank_bid_id, sum(ifnull(amount, 0)) amount
                            from pyner_trade
                            where order_traning_code = 7006
                              and traning_code = 7300
                              and order_status = 'Success'
                            group by depository_id, bank_platform_id, bank_bid_id) pyner_trade on
  pyner_bid.depository_id = pyner_trade.depository_id and pyner_bid.bank_platform_id = pyner_trade.bank_platform_id and
  pyner_bid.bank_bid_id = pyner_trade.bank_bid_id
set pyner_bid.compensation_direct_interest = pyner_trade.amount'''

calcCompensationIndirectAmountSQL = '''
update pyner_bid left join (select depository_id, bank_platform_id, bank_bid_id, sum(ifnull(amount, 0)) amount
                            from pyner_trade
                            where order_traning_code = 7007
                              and traning_code = 7200
                              and order_status = 'Success'
                            group by depository_id, bank_platform_id, bank_bid_id) pyner_trade on
  pyner_bid.depository_id = pyner_trade.depository_id and pyner_bid.bank_platform_id = pyner_trade.bank_platform_id and
  pyner_bid.bank_bid_id = pyner_trade.bank_bid_id
set pyner_bid.compensation_indirect_amount = pyner_trade.amount'''

calcCompensationIndirectInterestSQL = '''
update pyner_bid left join (select depository_id, bank_platform_id, bank_bid_id, sum(ifnull(amount, 0)) amount
                            from pyner_trade
                            where order_traning_code = 7007
                              and traning_code = 7300
                              and order_status = 'Success'
                            group by depository_id, bank_platform_id, bank_bid_id) pyner_trade on
  pyner_bid.depository_id = pyner_trade.depository_id and pyner_bid.bank_platform_id = pyner_trade.bank_platform_id and
  pyner_bid.bank_bid_id = pyner_trade.bank_bid_id
set pyner_bid.compensation_indirect_interest = pyner_trade.amount'''

calcCompensationOverdueAmountSQL = '''
update pyner_bid left join (select depository_id, bank_platform_id, bank_bid_id, sum(ifnull(amount, 0)) amount
                            from pyner_trade
                            where order_traning_code = 7008
                              and traning_code = 7200
                              and order_status = 'Success'
                            group by depository_id, bank_platform_id, bank_bid_id) pyner_trade on
  pyner_bid.depository_id = pyner_trade.depository_id and pyner_bid.bank_platform_id = pyner_trade.bank_platform_id and
  pyner_bid.bank_bid_id = pyner_trade.bank_bid_id
set pyner_bid.compensation_overdue_amount = pyner_trade.amount'''

calcCompensationOverdueInterestSQL = '''
update pyner_bid left join (select depository_id, bank_platform_id, bank_bid_id, sum(ifnull(amount, 0)) amount
                            from pyner_trade
                            where order_traning_code = 7008
                              and traning_code = 7300
                              and order_status = 'Success'
                            group by depository_id, bank_platform_id, bank_bid_id) pyner_trade on
  pyner_bid.depository_id = pyner_trade.depository_id and pyner_bid.bank_platform_id = pyner_trade.bank_platform_id and
  pyner_bid.bank_bid_id = pyner_trade.bank_bid_id
set pyner_bid.compensation_overdue_interest = pyner_trade.amount'''

calcBidServiceAmountSQL = '''
update pyner_bid left join (select depository_id, bank_platform_id, bank_bid_id, sum(ifnull(amount, 0)) amount
                            from pyner_trade
                            where order_traning_code in (7002, 7006, 7007, 7008)
                              and traning_code = 7400
                              and order_status = 'Success'
                            group by depository_id, bank_platform_id, bank_bid_id) pyner_trade on
  pyner_bid.depository_id = pyner_trade.depository_id and pyner_bid.bank_platform_id = pyner_trade.bank_platform_id and
  pyner_bid.bank_bid_id = pyner_trade.bank_bid_id
set pyner_bid.service_amount = pyner_trade.amount'''

calcCompensationRepayedAmountInterestSQL = '''
update pyner_bid
set compensation_repayed_amount   = ifnull(compensation_direct_amount, 0) + ifnull(compensation_indirect_amount, 0),
    compensation_repayed_interest = ifnull(compensation_direct_interest, 0) + ifnull(compensation_indirect_interest, 0)
where granted_time is not null'''

calcOverdueTimeAndAmount = '''
update pyner_bid
set overdue_time           = should_repay_time,
    repayed_overdue_amount = granted_amout - ifnull(repayed_normal_amount, 0)
where granted_time is not null
  and overdue_time is null
  and should_repay_time is not null
  and should_repay_time < now()
  and granted_amout > repayed_normal_amount;'''

calcCompensationAmountSQL = '''
update pyner_bid
set compensation_amount = ifnull(repayed_overdue_amount, 0) - ifnull(compensation_repayed_amount, 0)
where granted_time is not null'''

calcRepayedInterestSQL = '''
update pyner_bid
set repayed_interest = ifnull(repayed_normal_interest, 0) + ifnull(compensation_direct_interest, 0) +
                       ifnull(compensation_indirect_interest, 0)
where granted_time is not null'''

calcComprehensiveRateSQL = '''
update pyner_bid
set comprehensive_rate = (ifnull(repayed_amount, 0) + ifnull(repayed_interest, 0) + ifnull(service_amount, 0) -
                          ifnull(granted_amout, 0)) / ifnull(granted_amout, 0)
where granted_time is not null
  and balance_amount = 0'''

updateObligatoryBidInfoSQL = '''
update pyner_obligatory left join pyner_bid on pyner_bid.depository_id = pyner_obligatory.depository_id and
                                               pyner_bid.bank_platform_id = pyner_obligatory.bank_platform_id and
                                               pyner_bid.bank_bid_id = pyner_obligatory.bank_bid_id
set pyner_obligatory.repayed_amount                 = pyner_bid.repayed_amount,
    pyner_obligatory.balance_amount                 = pyner_bid.balance_amount,
    pyner_obligatory.bid_status                     = pyner_bid.bid_status,
    pyner_obligatory.period                         = pyner_bid.period,
    pyner_obligatory.borrower_p2p_user_id           = pyner_bid.p2p_user_id,
    pyner_obligatory.repayed_normal_amount          = pyner_bid.repayed_normal_amount,
    pyner_obligatory.compensation_amount            = pyner_bid.compensation_amount,
    pyner_obligatory.compensation_repayed_amount    = pyner_bid.compensation_repayed_amount,
    pyner_obligatory.compensation_direct_amount     = pyner_bid.compensation_direct_amount,
    pyner_obligatory.compensation_indirect_amount   = pyner_bid.compensation_indirect_amount,
    pyner_obligatory.compensation_overdue_amount    = pyner_bid.compensation_overdue_amount,
    pyner_obligatory.repayed_normal_interest        = pyner_bid.repayed_normal_interest,
    pyner_obligatory.compensation_interest          = pyner_bid.compensation_interest,
    pyner_obligatory.compensation_repayed_interest  = pyner_bid.compensation_repayed_interest,
    pyner_obligatory.compensation_direct_interest   = pyner_bid.compensation_direct_interest,
    pyner_obligatory.compensation_indirect_interest = pyner_bid.compensation_indirect_interest,
    pyner_obligatory.compensation_overdue_interest  = pyner_bid.compensation_overdue_interest'''
