queryHistoryAccountUserSQL = '''
select bank_user_id, bank_platform_id, depository_id, saas_id
from pyner_account
where customer_id is null 
group by bank_user_id,bank_platform_id,depository_id
'''

queryHistoryBidUserSQL = '''
select bank_user_id, bank_platform_id, depository_id, saas_id
from pyner_bid
where customer_id is null
group by bank_user_id, bank_platform_id, depository_id'''

queryHistoryObligatoryUserSQL = '''
select bank_user_id, bank_platform_id, depository_id, saas_id
from pyner_obligatory
where bank_user_id is not null
  and customer_id is null
group by bank_user_id, bank_platform_id, depository_id'''

queryHistoryTradePayerSQL = '''
select pay_bank_user_id, bank_platform_id, depository_id, saas_id
from pyner_trade
where pay_bank_user_id is not null
  and pay_customer_id is null
group by pay_bank_user_id, bank_platform_id, depository_id'''

queryHistoryTradeReceiverSQL = '''
select receive_bank_user_id, bank_platform_id, depository_id, saas_id
from pyner_trade
where receive_bank_user_id is not null
  and receive_customer_id is null
group by receive_bank_user_id, bank_platform_id, depository_id'''


updatePlatformNameSQL = '''
update pyner_user u, pyner_platform p
set u.platform_name = p.platform_name
where u.platform_name is null
  and u.bank_platform_id = p.bank_platform_id'''
