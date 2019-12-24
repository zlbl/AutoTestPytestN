updateBidPlatformNameSQL = '''
update pyner_bid, pyner_platform
set pyner_bid.platform_name = pyner_platform.platform_name
where pyner_bid.bank_platform_id = pyner_platform.bank_platform_id
	and pyner_bid.depository_id = pyner_platform.depository_id;'''

calcFlowBidTimeSQL = '''
update pyner_bid
set flowed_time = bank_update_time,
    finish_time = bank_update_time
where bid_status = 'FLOWED'
  and flowed_time is null'''

calcRequestTimeSQL = '''
update pyner_bid
set request_time = bank_create_time
where request_time is null'''

calcGrantedTimeSQL = '''
update pyner_bid
set granted_time = request_time
where granted_time is null
	and (granted_amout > 0 or repayed_amount > 0)'''

calcLendedBidTimeSQL = '''
update pyner_bid
set finish_time = granted_time
where granted_time is not null
  and bid_status = 'LENDED' '''

calcRaiseDurationSQL = '''
update pyner_bid
set raise_duration = timestampdiff(second, request_time, granted_time)
where granted_time is not null
	and granted_time > request_time'''

calcRaiseDurationSQL1 = '''
update pyner_bid
set raise_duration = 0
where granted_time is not null
	and granted_time <= request_time'''

calcShowRepayTimeSQL = '''
update pyner_bid
set should_repay_time = timestampadd(day, period, granted_time)
where granted_time is not null
  and period is not null'''

calcGrantedAmountSQL = '''
update pyner_bid
set granted_amout = amount
where granted_time is not null
	and granted_amout is null
	and granted_amout = 0'''

calcRepayedAmountSQL = '''
update pyner_bid
set repayed_amount = 0
where granted_time is not null
	and repayed_amount is null'''

calcBalanceAmountSQL = '''
update pyner_bid
set balance_amount = granted_amout - repayed_amount
where granted_time is not null
	and granted_amout > repayed_amount'''

calcBalanceAmountSQL1 = '''
update pyner_bid
set balance_amount   = 0,
		repayed_interest = ifnull(repayed_interest, 0) + (repayed_amount - granted_amout)
where granted_time is not null
	and granted_amout <= repayed_amount'''

calcCloseBidStatusSQL = '''
update pyner_bid
set finish_repay_time  = ifnull(finish_repay_time, bank_update_time),
    finish_time        = finish_repay_time,
    bid_status         = 'Closed',
    comprehensive_rate = (ifnull(repayed_amount, 0) + ifnull(repayed_interest, 0) + ifnull(service_amount, 0) -
                          ifnull(granted_amout, 0)) / ifnull(granted_amout, 0)
where granted_time is not null
  and balance_amount = 0'''

syncObligatoryBorrowerInfoSQL = '''
update pyner_obligatory left join pyner_bid on pyner_obligatory.depository_id = pyner_bid.depository_id and
                                               pyner_obligatory.bank_platform_id = pyner_bid.bank_platform_id and
                                               pyner_obligatory.bank_bid_id = pyner_bid.bank_bid_id
set pyner_obligatory.borrower_bank_user_id = pyner_bid.bank_user_id,
    pyner_obligatory.borrower_customer_id  = pyner_bid.customer_id'''
