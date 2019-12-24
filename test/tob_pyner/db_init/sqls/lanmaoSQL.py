lanmaoUserPersonSQL = '''
select
u.ID as bank_user_id
,u.PLATFORM_USER_NO as p2p_user_id
,'' as user_flow_id
,case u.USER_TYPE
  when 'PERSONAL' then 'Person'
  when 'ORGANIZATION' then 'Enterprise'
  when 'Platform' then 'Platform' end as user_type
,u.PLATFORM_ID as bank_platform_id
,plat.PLATFORM_NAME as platform_name
,case u.USER_ROLE
  when 'PLATFORM_ALTERNATIVE_RECHARGE' then 'PlatformAlternativeRecharge'
  when 'PLATFORM_FUNDS_TRANSFER' then 'PlatformFundsTransfer'
  when 'PLATFORM_INTEREST' then 'PlatformInterest'
  when 'SUPPLIER' then 'Supplier'
  when 'PLATFORM_INCOME' then 'PlatformIncome'
  when 'COLLABORATOR' then 'Collaborator'
  when 'PLATFORM_MARKETING' then 'PlatformMarketing'
  when 'GUARANTEECORP' then 'GuaranteeCorp'
  when 'PLATFORM_PROFIT' then 'PlatformProfit'
  when 'INVESTOR' then 'Lender'
  when 'BORROWERS' then 'Borrower'
  when 'NORMAL' then 'Normal'
  when 'INTERMEDIATOR' then 'Intermediator'
  when 'PLATFORM_COMPENSATORY' then 'PlatformCompensatory'
  when 'PLATFORM_URGENT' then 'PlatformUrgent' end as business_type
,'' as last_trade_time
,'' as country
,'' as province_code
,'' as province_name
,'' as city_code
,'' as city_name
,'' as area_code
,'' as area_name
,'' as address
,u.CELL_PHONE as mobile
,case u.ENABLE
  when '1' then 'Normal'
  when '0' then 'LogOut' end as user_status
,'' as customer_id
,'1000000002' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,0 as creator
,0 as last_updater
,'U' as state
,trim(u.NAME) as real_name
,case p.CRED_TYPE
when 'PRC_ID' then 'IDC'
when 'COMPATRIOTS_CARD' then 'GAT'
when 'PASSPORT' then 'PASSPORT'
when 'BLC' then 'BLC'
when 'PERMANENT_RESIDENCE' then 'FPR'
when 'USCC' then 'USCC' end as cred_type
,p.CRED_NUM as cred_no
,'' as fraud_blacklist
,'' as launder_blacklist
,'' as bad_msg
,'' as bull_loan
,'' as enterprise_create_time
,'' as enterprise_report_time
,'' as fraud_modify_time
,'' as relation_group_id
,'' as launder_modify_time
,u.CREATE_TIME as bank_create_time
,nvl(u.LAST_MODIFY_TIME, u.CREATE_TIME) as bank_update_time
,'' as longitude
,'' as latitude
from T_USER u left join T_USER_PERSONAL p on u.ID = p.ID
              left join T_PLATFORM plat on u.PLATFORM_ID = plat.ID
where u.USER_TYPE = 'PERSONAL'
  and (u.CREATE_TIME < to_date('2018-12-16','yyyy-mm-dd')
         or u.LAST_MODIFY_TIME < to_date('2018-12-16','yyyy-mm-dd'));'''

lanmaoUserEnterpriseSQL = '''
select
u.ID as bank_user_id
,u.PLATFORM_USER_NO as p2p_user_id
,'' as user_flow_id
,case u.USER_TYPE
  when 'PERSONAL' then 'Person'
  when 'ORGANIZATION' then 'Enterprise'
  when 'Platform' then 'Platform' end as user_type
,u.PLATFORM_ID as bank_platform_id
,plat.PLATFORM_NAME as platform_name
,case u.USER_ROLE
  when 'PLATFORM_ALTERNATIVE_RECHARGE' then 'PlatformAlternativeRecharge'
  when 'PLATFORM_FUNDS_TRANSFER' then 'PlatformFundsTransfer'
  when 'PLATFORM_INTEREST' then 'PlatformInterest'
  when 'SUPPLIER' then 'Supplier'
  when 'PLATFORM_INCOME' then 'PlatformIncome'
  when 'COLLABORATOR' then 'Collaborator'
  when 'PLATFORM_MARKETING' then 'PlatformMarketing'
  when 'GUARANTEECORP' then 'GuaranteeCorp'
  when 'PLATFORM_PROFIT' then 'PlatformProfit'
  when 'INVESTOR' then 'Lender'
  when 'BORROWERS' then 'Borrower'
  when 'NORMAL' then 'Normal'
  when 'INTERMEDIATOR' then 'Intermediator'
  when 'PLATFORM_COMPENSATORY' then 'PlatformCompensatory'
  when 'PLATFORM_URGENT' then 'PlatformUrgent' end as business_type
,'' as last_trade_time
,'' as country
,'' as province_code
,'' as province_name
,'' as city_code
,'' as city_name
,'' as area_code
,'' as area_name
,'' as address
,u.CELL_PHONE as mobile
,case u.ENABLE
  when '1' then 'Normal'
  when '0' then 'LogOut' end as user_status
,'' as customer_id
,'1000000002' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,0 as creator
,0 as last_updater
,'U' as state
,trim(u.NAME) as real_name
,nvl2(o.UNIFIED_CODE, 'USCC','BLC') as cred_type
,nvl(o.UNIFIED_CODE, o.BUSINESS_LICENSE) as cred_no
,'' as fraud_blacklist
,'' as launder_blacklist
,'' as bad_msg
,'' as bull_loan
,'' as enterprise_create_time
,'' as enterprise_report_time
,'' as fraud_modify_time
,'' as relation_group_id
,'' as launder_modify_time
,u.CREATE_TIME as bank_create_time
,nvl(u.LAST_MODIFY_TIME, u.CREATE_TIME) as bank_update_time
,'' as longitude
,'' as latitude
from T_USER u left join T_USER_ORGANIZATION o on u.ID = o.ID
              left join T_PLATFORM plat on u.PLATFORM_ID = plat.ID
where u.USER_TYPE = 'ORGANIZATION'
  and (u.CREATE_TIME < to_date('2018-12-16','yyyy-mm-dd')
         or u.LAST_MODIFY_TIME < to_date('2018-12-16','yyyy-mm-dd'));'''

lanmaoPersonSQL = '''
select
u.ID as bank_user_id
,u.PLATFORM_ID as bank_platform_id
,trim(u.NAME) as real_name
,case p.CRED_TYPE
when 'PRC_ID' then 'IDC'
when 'COMPATRIOTS_CARD' then 'GAT'
when 'PASSPORT' then 'PASSPORT'
when 'BLC' then 'BLC'
when 'PERMANENT_RESIDENCE' then 'FPR'
when 'USCC' then 'USCC' end as cred_type
,p.CRED_NUM as cred_no
,'' as gender
,'' as birthday
,'' as customer_id
,'1000000002' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,0 as creator
,0 as last_updater
,'U' as state
,u.CREATE_TIME as bank_create_time
,nvl(u.LAST_MODIFY_TIME, u.CREATE_TIME) as bank_update_time
from T_USER u left join T_USER_PERSONAL p on u.ID = p.ID
where u.USER_TYPE = 'PERSONAL'
  and (u.CREATE_TIME < to_date('2018-12-16','yyyy-mm-dd')
         or u.LAST_MODIFY_TIME < to_date('2018-12-16','yyyy-mm-dd'));'''

lanmaoEnterpriseSQL = '''
select
u.ID as bank_user_id
,u.PLATFORM_ID as bank_platform_id
,trim(u.NAME) as enterprise_name
,o.BANK_LICENSE as bank_license
,o.CREDIT_CODE as org_credit_code
,o.BUSINESS_LICENSE as business_license
,o.TAX_NO as tax_no
,o.UNIFIED_CODE as unified_code
,'' as social_credit_code
,'' as business_lic_reg_address
,o.LEGAL as legal_person_name
,case o.CRED_TYPE
when 'PRC_ID' then 'IDC'
when 'COMPATRIOTS_CARD' then 'GAT'
when 'PASSPORT' then 'PASSPORT'
when 'BLC' then 'BLC'
when 'PERMANENT_RESIDENCE' then 'FPR'
when 'USCC' then 'USCC' end as legal_cred_type
,o.LEGAL_ID_NO as legal_cred_no
,o.CONTACT as contact
,o.CONTACT_PHONE as contact_phone
,o.BANKCARD as bank_card
,o.BANKCODE as bank_code
,'' as customer_id
,'1000000002' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,'0' as creator
,'0' as last_updater
,'U' as state
,u.CREATE_TIME as bank_create_time
,nvl(u.LAST_MODIFY_TIME, u.CREATE_TIME) as bank_update_time
,'USCC' as cred_type
,o.UNIFIED_CODE as cred_no
from T_USER u left join T_USER_ORGANIZATION o on u.ID = o.ID
where u.USER_TYPE = 'ORGANIZATION'
  and (u.CREATE_TIME < to_date('2018-12-16','yyyy-mm-dd')
         or u.LAST_MODIFY_TIME < to_date('2018-12-16','yyyy-mm-dd'));'''

lanmaoPlatformSQL = '''
select
p.ID as bank_platform_id
,'' as platform_flow_id
,p.PLATFORM_NAME as platform_name
,case p.PLATFORM_TYPE
  when 'TEST' then 'TEST'
  when 'SHHDZH' then 'SHHDZH'
  when 'CLIENT' then 'CLIENT' end as platform_classify
,'' as platform_type
,p.LEGAL_PERSON as legal_person_name
,'IDC' as legal_cred_type
,p.LEGAL_CARNO as legal_cred_no
,trim(p.ENTERPRISE_NAME) as enterprise_name
,'' as cred_no
,'' as cred_type
,p.ORG_NO as org_no
,p.BANK_LICENSE as bank_license
,p.BUSINESS_LICENSE as business_license
,p.TAX_NO as tax_no
,p.SOCIAL_CREDIT_CODE as social_credit_code
,p.ORG_CREDIT_CODE as org_credit_code
,p.BUSINESS_LIC_REG_ADDRESS as business_lic_reg_address
,'' as contact
,'' as contact_phone
,p.WEBSITE_NAME as website_name
,p.WEBSITE_URL as website_url
,p.DESCRIPTION as description
,'1000000002' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,'0' as creator
,'0' as last_updater
,'U' as state
,'' as customer_id
,'' as relation_group_id
,p.CREATE_TIME as bank_create_time
,nvl(p.LAST_MODIFY_TIME, p.CREATE_TIME) as bank_update_time
,'' as cooperation_status
,'' as submitted_area
,'' as contract_sign_time
,'' as system_launch_time
,'' as customer_manager
,'' as remark
from T_PLATFORM p
where (p.CREATE_TIME < to_date('2018-12-16','yyyy-mm-dd')
         or p.LAST_MODIFY_TIME < to_date('2018-12-16','yyyy-mm-dd'));'''

lanmaoAccountSQL = '''
select
a.ID as bank_account_id
,'' as account_flow_id
,a.BIZ_ID as bank_user_id
,a.MERCHANT_NO as bank_platform_id
,case a.BIZ_TYPE
  when 'ALTERNATIVE_RECHARGE' then 'PlatformAlternativeRecharge'
  when 'FUNDS_TRANSFER' then 'PlatformFundsTransfer'
  when 'INTEREST' then 'PlatformInterest'
  when 'INCOME' then 'PlatformIncome'
  when 'MARKETING' then 'PlatformMarketing'
  when 'PROFIT' then 'PlatformProfit'
  when 'INVESTOR' then 'Lender'
  when 'DEFAULT' then 'Normal'
  when 'COMPENSATORY' then 'PlatformCompensatory'
  when 'URGENT' then 'PlatformUrgent'
  when 'POUNDAGE' then 'Poundage' end as business_type
,a.BALANCE as balance
,a.FREEZE_AMOUNT as freeze_amount
,'' as customer_id
,'1000000002' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,'0' as creator
,'0' as last_updater
,'U' as state
,'CNY' as currency
,a.CREATE_TIME as bank_create_time
,nvl(a.BALANCE_MODIFY_TIME, a.CREATE_TIME) as bank_update_time
from T_ACCOUNT a
where (a.CREATE_TIME < to_date('2018-12-16','yyyy-mm-dd')
  or a.BALANCE_MODIFY_TIME < to_date('2018-12-16','yyyy-mm-dd'));'''

lanmaoBidSQL = '''
select
p.ID as bank_bid_id
,p.PLATFORM_PROJECT_NO as bid_flow_id
,p.BORROWER_USER_ID as bank_user_id
,p.BORROWER_PLATFORM_USER_NO as p2p_user_id
,p.BORROWER_PLATFORM_ID as bank_platform_id
,p.PLATFORM_PROJECT_NAME as bid_name
,p.PLATFORM_PROJECT_AMOUNT as amount
,'CNY' as currency
,p.PROJECT_PERIOD as period
,p.ANNUAL_INTEREST_RATE as rate
,'' as interest
,'' as service_amount
,case p.STATUS
  when 'COLLECTING' then 'Investing'
  when 'FINISH' then 'Lended'
  when 'MISCARRY' then 'Flowed'
  when 'REPAYING' then 'InRepayment' end as bid_status
,'Credit' as bid_type
,p.TOTAL_LOAN_MONEY as granted_amout
,p.TOTAL_RETURN_PRINCIPAL as repayed_amount
,p.TOTAL_RETURN_INTEREST as repayed_interest
,'' as balance_amount
,'' as repayed_normal_amount
,'' as repayed_overdue_amount
,'' as compensation_amount
,'' as compensation_repayed_amount
,'' as compensation_direct_amount
,'' as compensation_indirect_amount
,'' as compensation_overdue_amount
,p.COLLECTING_STATUS_TIME as request_time
,p.LAST_LOAN_TIME as granted_time
,'' as overdue_time
,'' as should_repay_time
,'' as finish_repay_time
,case p.PROJECT_TYPE
  when 'STANDARDPOWDER' then 'N'
  when 'FIDUCIARYPOWDER' then 'Y' end as entrusted_pay
,case p.PRODUCT_TYPE
  when 'AUTOMATICPRODUCT' then '1'
  when 'COMMONPRODUCT' then '0' end as is_auto
,'' as raise_duration
,'' as deal_rate
,'' as comprehensive_rate
,case p.REPAYMENT_WAY
  when 'ONE_TIME_SERVICING' then 'OneTimeServicing'
  when 'FIXED_BASIS_MORTGAGE' then 'FixedBasisMortgage'
  when 'FIXED_PAYMENT_MORTGAGE' then 'FixedPaymentMortgage'
  when 'FIRSEINTREST_LASTPRICIPAL' then 'FirstInterestLastPrincipal'
  when 'EQUAL_PRINCIPAL_INTEREST' then 'EqualPrincipalInterest'
  when 'Other' then 'Other' end as repayment_type
,'' as product_type
,'' as lender_rate
,p.DESCRIPTION as borr_purpose
,'' as customer_id
,'1000000002' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,'0' as creator
,'0' as last_updater
,'U' as state
,'' as repayed_normal_interest
,'' as repayed_overdue_interest
,'' as compensation_interest
,'' as compensation_repayed_interest
,'' as compensation_direct_interest
,'' as compensation_indirect_interest
,'' as compensation_overdue_interest
,'' as user_type
,'' as real_name
,'' as cred_type
,'' as cred_no
,'' as relation_group_id
,p.CREATE_TIME as bank_create_time
,nvl(p.LAST_MODIFY_TIME, p.CREATE_TIME) as bank_update_time
,'' as flowed_time
,'' as finish_time
,'' as province_code
,'' as province_name
,'' as city_code
,'' as city_name
,'' as longitude
,'' as latitude
,'' as gender
,'' as birthday
,'' as platform_name
from T_PROJECT p
where (p.CREATE_TIME < to_date('2018-12-16','yyyy-mm-dd')
  or p.LAST_MODIFY_TIME < to_date('2018-12-16','yyyy-mm-dd'));'''

lanmaoObligatorySQL = '''
select
 o.ID as bank_obligatory_id
,o.ID as obligatory_flow_id
,o.PROJECT_ID as bank_bid_id
,o.INVESTOR_USER_ID as bank_user_id
,'' as customer_id
,'' as borrower_bank_user_id
,'' as borrower_customer_id
,o.PLATFORM_ID as bank_platform_id
,o.INHAND_SHARE as sum_amount
,o.PRE_PURCHASED_SHARE as freeze_amount
,'' as repayed_amount
,'' as balance_amount
,'' as repayed_normal_amount
,'' as repayed_overdue_amount
,'' as compensation_amount
,'' as compensation_repayed_amount
,'' as compensation_direct_amount
,'' as compensation_indirect_amount
,'' as compensation_overdue_amount
,'1000000002' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,0 as creator
,0 as last_updater
,'U' as state
,'' as repayed_normal_interest
,'' as repayed_overdue_interest
,'' as compensation_interest
,'' as compensation_repayed_interest
,'' as compensation_direct_interest
,'' as compensation_indirect_interest
,'' as compensation_overdue_interest
,p.PLATFORM_PROJECT_AMOUNT as bid_amount
,case p.STATUS
  when 'COLLECTING' then 'Investing'
  when 'FINISH' then 'Lended'
  when 'MISCARRY' then 'Flowed'
  when 'REPAYING' then 'InRepayment' end as bid_status
,'Credit' as bid_type
,'' as user_type
,'' as real_name
,'' as cred_type
,'' as cred_no
,'' as period
,o.CREATE_TIME as bank_create_time
,nvl(o.LAST_MODIFY_TIME, o.CREATE_TIME) as bank_update_time
,'' as borrower_p2p_user_id
,u.PLATFORM_USER_NO as bank_p2p_user_id
,'' as province_code
,'' as province_name
,'' as city_code
,'' as city_name
,'' as longitude
,'' as latitude
,'' as gender
,'' as birthday
 from T_PROJECT_DEBENTURE_REC o
        left join T_USER u on o.INVESTOR_USER_ID = u.ID and o.PLATFORM_ID = u.PLATFORM_ID
 left join T_PROJECT p on o.PROJECT_ID = p.ID
where (o.CREATE_TIME < to_date('2018-12-16','yyyy-mm-dd')
  or o.LAST_MODIFY_TIME < to_date('2018-12-16','yyyy-mm-dd'));'''

lanmaoTradeOrderSQL = '''
select
ID as bank_order_id
,PLATFORM_ID as bank_platform_id
,'' as source
,'' as out_bank_order_id
,'' as ref_order_id
,PROJECT_ID as bid_id
,BIZ_TYPE as trans_code
,BIZ_TYPE as sub_trans_code
,case BIZ_TYPE
  when 'RECHARGE' then '11000'
  when 'WITHDRAW' then '12000'
  when 'TENDER' then '3014'
  when 'CREDIT_ASSIGNMENT' then '3022'
  when 'REPAYMENT' then '7002'
  when 'PRINCIPAL' then '7200'
  when 'INTEREST' then '7300'
  when 'COMPENSATORY' then '7006'
  when 'INDIRECT_COMPENSATORY' then '7007'
  when 'COMPENSATORY_REPAYMENT' then '7008'
  when 'INTEREST_REPAYMENT' then '7700'
  when 'PLATFORM_INDEPENDENT_PROFIT' then '7100'
  when 'COMMISSION' then '7400'
  when 'PROFIT' then '7100'
  when 'DEDUCT' then '7400'
  when 'MARKETING' then '3002'
  when 'ALTERNATIVE_RECHARGE' then '11015'
  when 'WITHDRAW_URGENT' then '12018'
  when 'FREEZE' then '13009'
  when 'UNFREEZE' then '13019'
  when 'BACKROLL_COMMISSION' then '17410'
  when 'ADJUST_INCREASE' then '11901'
  when 'WITHDRAW_URGENT_NORAML' then '12018'
  when 'ADJUST_REDUCE' then '12901'
  when 'FIDUCIARY_PAYMENT' then '13001'
  when 'PLATFORM_URGENT_PAY' then '17009'
  when 'PLATFORM_ACC_ADJUST_INCREASE' then '17001'
  when 'PLATFORM_URGENT_RETURN' then '17002'
  when 'FUNDS_TRANSFER' then '18006'
  when 'DIRECT_TRANSFER' then '18000' end as traning_code
,case STATUS
  when 'SUCCESS' then 'Success'
  when 'CREATED' then 'Pending'
  when 'FAIL' then 'Fail' end as status
,'' as total_num
,TOTAL_AMOUNT as total_amount
,'CNY' as currency
,'' as notice_url
,'' as notice_status
,'' as request_time
,'' as remark
,CREATE_TIME as bank_create_time
,CREATE_TIME as bank_update_time
,COMPLETED_TIME as finished_time
,PROCESSION_TIME as procession_time
,ORDER_VERSION as order_version
,'' as receiver_need_freeze
,'' as freeze_type
,REQUEST_NO as request_no
,FLOW_NO as flow_no
,TOTAL_INCOME as total_income
,COMMISSION as commission
,TRANS_TYPE as trans_type
,MARKETING as marketing
,REPAIR_TYPE as repair_type
,BIZ_ORIGIN as biz_origin
,FAIL_CODE as fail_code
,FAIL_REASON as fail_reason
,PROCESS_TYPE as process_type
,'1000000002' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,0 as creator
,0 as last_updater
,'U' as state
from T_TRANSACTION_ORDER;'''

lanmaoTradeSQL = '''
select
 r.ID as bank_trade_id
,r.FLOW_NO as trade_flow_id
,'' as p2p_flow_id
,r.SOURCE_PLATFORM_ID as bank_platform_id
,'' as platform_name
,'' as bank_bid_id
,r.SOURCE_USER_ID as pay_bank_user_id
,r.SOURCE_PLATFORM_ID as pay_p2p_user_id
,'' as pay_customer_id
,r.TARGET_USER_ID as receive_bank_user_id
,r.TARGET_PLATFORM_USER_NO as receive_b2b_user_id
,'' as receive_customer_id
,r.AMOUNT as amount
,'' as acc_amount
,'' as org_amount
,'CNY' as currency
,r.BIZ_TYPE as trans_code
,r.BIZ_TYPE as sub_trans_code
,case r.STATUS
  when 'SUCCESS' then 'Success'
  when 'CREATED' then 'Pending'
  when 'FAIL' then 'Fail' end as order_status
,'' as request_time
,r.REMARK as remark
,'' as source
,'' as finished_time
,r.CREATE_TIME as bank_update_time
,'' as finished_date
,'' as bank_code
,'' as issuer
,'' as card_name
,'' as bank_card_no
,'' as entrusted_pay
,'' as fee_amount
,'' as order_expire_time
,'' as is_refund
,'' as trade_type
,'1000000002' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,'0' as creator
,'0' as last_updater
,'U' as state
,'' as user_type
,'' as real_name
,'' as cred_type
,'' as cred_no
,'' as belonging_code
,'' as belonging_name
,case r.BIZ_TYPE
  when 'TENDER' then '3014'
  when 'CREDIT_ASSIGNMENT' then '3022'
  when 'REPAYMENT' then '7002'
  when 'INTEREST' then '7300'
  when 'COMPENSATORY' then '7006'
  when 'COMPENSATORY_REPAYMENT' then '7008'
  when 'INTEREST_REPAYMENT' then '7700'
  when 'PLATFORM_INDEPENDENT_PROFIT' then '7100'
  when 'COMMISSION' then '7400'
  when 'PROFIT' then '7400'
  when 'DEDUCT' then '7400'
  when 'MARKETING' then '3002'
  when 'ALTERNATIVE_RECHARGE' then '11015'
  when 'WITHDRAW_URGENT' then '12018'
  when 'FREEZE' then '13009'
  when 'UNFREEZE' then '13019'
  when 'BACKROLL_COMMISSION' then '17410'
  when 'ADJUST_INCREASE' then '11901'
  when 'WITHDRAW_URGENT_NORAML' then '12018'
  when 'ADJUST_REDUCE' then '12901'
  when 'FIDUCIARY_PAYMENT' then '13001'
  when 'PLATFORM_URGENT_PAY' then '17009'
  when 'PLATFORM_ACC_ADJUST_INCREASE' then '17001'
  when 'PLATFORM_URGENT_RETURN' then '17002'
  when 'FUNDS_TRANSFER' then '18006'
  when 'DIRECT_TRANSFER' then '18000' end as traning_code
,'' as trans_code_type
,r.CREATE_TIME as bank_create_time
,r.ORDER_ID as bank_order_id
,'' as order_trans_code
,'' as order_sub_trans_code
,'' as order_traning_code
 from T_TRANSACTION_RECORD r
 where r.BIZ_TYPE not in ('RECHARGE','WITHDRAW','REPAYMENT','COMPENSATORY','COMPENSATORY_REPAYMENT','INDIRECT_COMPENSATORY')
 and r.CREATE_TIME < to_date('2018-12-16','yyyy-mm-dd');'''

lanmaoRechargeTradeSQL = '''
select
 r.ID as bank_trade_id
,r.FLOW_NO as trade_flow_id
,'' as p2p_flow_id
,r.SOURCE_PLATFORM_ID as bank_platform_id
,'' as platform_name
,'' as bank_bid_id
,r.SOURCE_USER_ID as pay_bank_user_id
,r.SOURCE_PLATFORM_ID as pay_p2p_user_id
,'' as pay_customer_id
,r.TARGET_USER_ID as receive_bank_user_id
,r.TARGET_PLATFORM_USER_NO as receive_b2b_user_id
,'' as receive_customer_id
,r.AMOUNT as amount
,'' as acc_amount
,'' as org_amount
,'CNY' as currency
,r.BIZ_TYPE as trans_code
,re.RECHARGE_WAY as sub_trans_code
,case re.STATUS
  when 'PENDDING' then 'Pending'
  when 'SUCCESS' then 'Success'
  when 'FAIL' then 'Fail' end as order_status
,'' as request_time
,r.REMARK as remark
,'' as source
,'' as finished_time
,r.CREATE_TIME as bank_update_time
,'' as finished_date
,re.BANK as bank_code
,'' as issuer
,'' as card_name
,re.CARD_NO as bank_card_no
,'' as entrusted_pay
,'' as fee_amount
,'' as order_expire_time
,'' as is_refund
,'' as trade_type
,'1000000002' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,'0' as creator
,'0' as last_updater
,'U' as state
,'' as user_type
,'' as real_name
,'' as cred_type
,'' as cred_no
,'' as belonging_code
,'' as belonging_name
,case re.RECHARGE_WAY
  when 'PROXY' then '1013'
  when 'WEB' then '1001'
  when 'PROTOCOL' then '1021'
  when 'SWIFT' then '1005'
  when 'ADJUST_BACKROLL' then '11001'
  when 'BACKROLL' then '11002'
  when 'BANK' then '11003' end as traning_code
,'' as trans_code_type
,r.CREATE_TIME as bank_create_time
,r.ORDER_ID as bank_order_id
,'' as order_trans_code
,'' as order_sub_trans_code
,'' order_traning_code
 from T_TRANSACTION_RECORD r left join T_TRANSACTION_ORDER o on r.ORDER_ID = o.ID
 left join T_USER_RECHARGE_RECORD re on o.REQUEST_NO = re.REQUEST_NO
 where r.BIZ_TYPE = 'RECHARGE' and r.CREATE_TIME < to_date('2018-12-16','yyyy-mm-dd');'''

lanmaoWithdrawTradeSQL = '''
select
 r.ID as bank_trade_id
,r.FLOW_NO as trade_flow_id
,'' as p2p_flow_id
,r.SOURCE_PLATFORM_ID as bank_platform_id
,'' as platform_name
,'' as bank_bid_id
,r.SOURCE_USER_ID as pay_bank_user_id
,r.SOURCE_PLATFORM_ID as pay_p2p_user_id
,'' as pay_customer_id
,r.TARGET_USER_ID as receive_bank_user_id
,r.TARGET_PLATFORM_USER_NO as receive_b2b_user_id
,'' as receive_customer_id
,r.AMOUNT as amount
,'' as acc_amount
,'' as org_amount
,'CNY' as currency
,r.BIZ_TYPE as trans_code
,r.BIZ_TYPE as sub_trans_code
,case wi.STATUS
  when 'SUCCESS' then 'Success'
  when 'ACCEPT' then 'Fail'
  when 'FAIL' then 'Fail'
  when 'ACCEPT_FAIL' then 'Fail'
  when 'REMITING' then 'Pending'
  when 'CONFIRMING' then 'Pending' end as order_status
,'' as request_time
,r.REMARK as remark
,'' as source
,'' as finished_time
,r.CREATE_TIME as bank_update_time
,'' as finished_date
,wi.bank as bank_code
,'' as issuer
,'' as card_name
,wi.CARD_NO as bank_card_no
,'' as entrusted_pay
,'' as fee_amount
,'' as order_expire_time
,'' as is_refund
,'' as trade_type
,'1000000002' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,'0' as creator
,'0' as last_updater
,'U' as state
,'' as user_type
,'' as real_name
,'' as cred_type
,'' as cred_no
,'' as belonging_code
,'' as belonging_name
,'12000' as traning_code
,'' as trans_code_type
,r.CREATE_TIME as bank_create_time
,r.ORDER_ID as bank_order_id
,'' as order_trans_code
,'' as order_sub_trans_code
,'' as order_traning_code
 from T_TRANSACTION_RECORD r left join T_TRANSACTION_ORDER o on r.ORDER_ID = o.ID
 left join T_USER_WITHDRAW_RECORD wi on o.REQUEST_NO = wi.REQUEST_NO
 where r.BIZ_TYPE = 'WITHDRAW' and r.CREATE_TIME < to_date('2018-12-16','yyyy-mm-dd');'''

lanmaoPrincipleRepaymentTradeSQL = '''
select
 r.ID as bank_trade_id
,r.FLOW_NO as trade_flow_id
,'' as p2p_flow_id
,r.SOURCE_PLATFORM_ID as bank_platform_id
,'' as platform_name
,'' as bank_bid_id
,r.SOURCE_USER_ID as pay_bank_user_id
,r.SOURCE_PLATFORM_ID as pay_p2p_user_id
,'' as pay_customer_id
,r.TARGET_USER_ID as receive_bank_user_id
,r.TARGET_PLATFORM_USER_NO as receive_b2b_user_id
,'' as receive_customer_id
,r.AMOUNT - r.INCOME as amount
,'' as acc_amount
,'' as org_amount
,'CNY' as currency
,r.BIZ_TYPE as trans_code
,r.BIZ_TYPE as sub_trans_code
,case r.STATUS
  when 'SUCCESS' then 'Success'
  when 'CREATED' then 'Pending'
  when 'FAIL' then 'Fail' end as order_status
,'' as request_time
,r.REMARK as remark
,'' as source
,'' as finished_time
,r.CREATE_TIME as bank_update_time
,'' as finished_date
,'' as bank_code
,'' as issuer
,'' as card_name
,'' as bank_card_no
,'' as entrusted_pay
,'' as fee_amount
,'' as order_expire_time
,'' as is_refund
,'' as trade_type
,'1000000002' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,'0' as creator
,'0' as last_updater
,'U' as state
,'' as user_type
,'' as real_name
,'' as cred_type
,'' as cred_no
,'' as belonging_code
,'' as belonging_name
,'7200' as traning_code
,'' as trans_code_type
,r.CREATE_TIME as bank_create_time
,r.ORDER_ID as bank_order_id
,'' as order_trans_code
,'' as order_sub_trans_code
,'' as order_traning_code
 from T_TRANSACTION_RECORD r
 where r.BIZ_TYPE in ('REPAYMENT','COMPENSATORY','COMPENSATORY_REPAYMENT','INDIRECT_COMPENSATORY')
  and r.AMOUNT > r.INCOME
  and r.CREATE_TIME < to_date('2018-12-16','yyyy-mm-dd');'''

lanmaoInterestRepaymentTradeSQL = '''
select
 concat(r.ID,'A') as bank_trade_id
,r.FLOW_NO as trade_flow_id
,'' as p2p_flow_id
,r.SOURCE_PLATFORM_ID as bank_platform_id
,'' as platform_name
,'' as bank_bid_id
,r.SOURCE_USER_ID as pay_bank_user_id
,r.SOURCE_PLATFORM_ID as pay_p2p_user_id
,'' as pay_customer_id
,r.TARGET_USER_ID as receive_bank_user_id
,r.TARGET_PLATFORM_USER_NO as receive_b2b_user_id
,'' as receive_customer_id
,r.INCOME as amount
,'' as acc_amount
,'' as org_amount
,'CNY' as currency
,r.BIZ_TYPE as trans_code
,r.BIZ_TYPE as sub_trans_code
,case r.STATUS
  when 'SUCCESS' then 'Success'
  when 'CREATED' then 'Pending'
  when 'FAIL' then 'Fail' end as order_status
,'' as request_time
,r.REMARK as remark
,'' as source
,'' as finished_time
,r.CREATE_TIME as bank_update_time
,'' as finished_date
,'' as bank_code
,'' as issuer
,'' as card_name
,'' as bank_card_no
,'' as entrusted_pay
,'' as fee_amount
,'' as order_expire_time
,'' as is_refund
,'' as trade_type
,'1000000002' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,'0' as creator
,'0' as last_updater
,'U' as state
,'' as user_type
,'' as real_name
,'' as cred_type
,'' as cred_no
,'' as belonging_code
,'' as belonging_name
,'7300' as traning_code
,'' as trans_code_type
,r.CREATE_TIME as bank_create_time
,r.ORDER_ID as bank_order_id
,'' as order_trans_code
,'' as order_sub_trans_code
,'' as order_traning_code
 from T_TRANSACTION_RECORD r
 where r.BIZ_TYPE in ('REPAYMENT','COMPENSATORY','COMPENSATORY_REPAYMENT','INDIRECT_COMPENSATORY')
  and r.INCOME > 0
  and r.CREATE_TIME < to_date('2018-12-16','yyyy-mm-dd');'''
