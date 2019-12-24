ucfUserSQL = '''
select
u.USER_ID as bank_user_id
,u.REF_USER as p2p_user_id
,'' as user_flow_id
,case u.user_type
   when '1' then 'Person'
   when '2' then 'Enterprise'
   when '3' then 'Platform' end as user_type
,u.REF_MERCHANT as bank_platform_id
,e.SHORT_NAME as platform_name
,case u.BIZ_TYPE
  when '01' then 'Lender'
  when '02' then 'Borrower'
  when '03' then 'GuaranteeCorp'
  when '04' then 'PlatformCounsel'
  when '05' then 'PlatformFundsTransfer'
  when '06' then 'BorrowingHybrid'
  when '08' then 'PlatformMarketing'
  when '10' then 'PlatformIncome'
  when '11' then 'PlatformCompensatory'
  when '12' then 'ThirdMarketing'
  when '13' then 'PlatformUrgent'
  when '14' then 'Transition' end as business_type
,null as last_trade_time
,'' as country
,'' as province_code
,'' as province_name
,'' as city_code
,'' as city_name
,'' as area_code
,'' as area_name
,u.address as address
,u.REGISTERED_CELL as mobile
,case u.ENABLED_STATUS
  when 'T' then 'Normal'
  when 'N' then 'Freeze'
  when 'C' then 'LogOut' end as user_status
,'' as customer_id
,'1000000001' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,0 as creator
,0 as last_updater
,'U' as state
,trim(u.real_name) as real_name
,case u.CERT_TYPE
  when 'IDC' then 'IDC'
  when 'GAT' then 'GAT'
  when 'MILITARY' then 'MILITARY'
  when 'PASS_PORT' then 'PASSPORT'
  when 'BLC' then 'BLC'
  when 'FPR' then 'FPR'
  when 'USCC' then 'USCC' end as cred_type
,u.CERT_NO as cred_no
,'' as fraud_blacklist
,'' as launder_blacklist
,'' as bad_msg
,'' as bull_loan
,'' as enterprise_create_time
,'' as enterprise_report_time
,'' as fraud_modify_time
,'' as relation_group_id
,'' as launder_modify_time
,u.GMT_CREATE as bank_create_time
,nvl(u.GMT_MODIFIED,u.GMT_CREATE) as bank_update_time
,'' as longitude
,'' as latitude
from UCF_MEMBER_USER u left join UCF_MEMBER_MERCHANT_EXTRA e on u.REF_MERCHANT = e.MERCHANT_ID
where u.USER_TYPE != 3
  and (u.GMT_CREATE < to_date('2018-12-16','yyyy-mm-dd')
         or u.GMT_MODIFIED < to_date('2018-12-16','yyyy-mm-dd'));'''

ucfUserPersonSQL = '''
select
 USER_ID as bank_user_id
,REF_MERCHANT as bank_platform_id
,trim(real_name) as real_name
,case CERT_TYPE
  when 'IDC' then 'IDC'
  when 'GAT' then 'GAT'
  when 'MILITARY' then 'MILITARY'
  when 'PASS_PORT' then 'PASSPORT'
  when 'BLC' then 'BLC'
  when 'FPR' then 'FPR'
  when 'USCC' then 'USCC' end as cred_type
,CERT_NO as cred_no
,gender as gender
,'' as birthday
,'' as customer_id
,'1000000001' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,0 as creator
,0 as last_updater
,'U' as state
,GMT_CREATE as bank_create_time
,nvl(GMT_MODIFIED,GMT_CREATE) as bank_update_time
 from UCF_MEMBER_USER where USER_TYPE = 1
 and (GMT_CREATE < to_date('2018-12-16','yyyy-mm-dd')
         or GMT_MODIFIED < to_date('2018-12-16','yyyy-mm-dd'));'''

ucfUserEnterpriseSQL = '''
select
u.USER_ID as bank_user_id
,u.REF_MERCHANT as bank_platform_id
,trim(u.REAL_NAME) as enterprise_name
,'' as bank_license
,'' as org_credit_code
,case u.CERT_TYPE when 'BLC' then u.CERT_NO end as business_license
,'' as tax_no
,case u.CERT_TYPE when 'USCC' then u.CERT_NO end as unified_code
,'' as social_credit_code
,'' as business_lic_reg_address
,'' as legal_person_name
,'' as legal_cred_type
,'' as legal_cred_no
,'' as contact
,'' as contact_phone
,'' as bank_card
,'' as bank_code
,'' as customer_id
,'1000000001' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,0 as creator
,0 as last_updater
,'U' as state
,u.GMT_CREATE as bank_create_time
,nvl(u.GMT_MODIFIED,u.GMT_CREATE) as bank_update_time
,u.CERT_TYPE as cred_type
,u.CERT_NO as cred_no
from UCF_MEMBER_USER u
where u.USER_TYPE = 2
  and (GMT_CREATE < to_date('2018-12-16','yyyy-mm-dd')
         or GMT_MODIFIED < to_date('2018-12-16','yyyy-mm-dd'));'''

ucfPlatformSQL = '''
select
e.MERCHANT_ID as bank_platform_id
,null as platform_flow_id
,e.SHORT_NAME as platform_name
,'CLIENT' as platform_classify
,'' as platform_type
,e.LEGAL_NAME as legal_person_name
,case e.LEGAL_CERT_TYPE
  when 'IDC' then 'IDC'
  when 'GAT' then 'GAT'
  when 'MILITARY' then 'MILITARY'
  when 'PASS_PORT' then 'PASSPORT'
  when 'BLC' then 'BLC'
  when 'FPR' then 'FPR'
  when 'USCC' then 'USCC' end as legal_cred_type
,e.LEGAL_CERT_NO as legal_cred_no
,trim(u.REAL_NAME) as enterprise_name
,'' as cred_type
,'' as cred_no
,e.ORG_CODE as org_no
,e.BANK_PERMIT_CERT_NO as bank_license
,case u.CERT_TYPE when 'BLC' then u.CERT_NO end as business_license
,e.TAX_REG_CERT_NO as tax_no
,case u.CERT_TYPE when 'USCC' then u.CERT_NO end as social_credit_code
,'' as org_credit_code
,u.ADDRESS as business_lic_reg_address
,e.APPLICANT_NAME as contact
,e.APPLICANT_MOBILE as contact_phone
,'' as website_name
,e.MERCHANT_WEBSITE as website_url
,e.REMARK as description
,'1000000001' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,0 as creator
,0 as last_updater
,'U' as state
,'' as customer_id
,'' as relation_group_id
,e.GMT_CREATE as bank_create_time
,nvl(e.GMT_MODIFIED,e.GMT_CREATE) as bank_update_time
,'' as cooperation_status
,'' as submitted_area
,'' as contract_sign_time
,'' as system_launch_time
,'' as customer_manager
,'' as remark
from UCF_MEMBER_MERCHANT_EXTRA e left join UCF_MEMBER_USER u on e.MERCHANT_ID = u.USER_ID
where (e.GMT_CREATE < to_date('2018-12-16','yyyy-mm-dd')
         or e.GMT_MODIFIED < to_date('2018-12-16','yyyy-mm-dd'));'''

ucfAccountSQL = '''
select
a.ACCOUNT_NO as bank_account_id
,'' as account_flow_id
,a.USER_ID as bank_user_id
,a.REF_MERCHANT as bank_platform_id
,case u.BIZ_TYPE
when '01' then 'Normal'
when '02' then 'Normal'
when '03' then 'GuaranteeCorp'
when '04' then 'PlatformCounsel'
when '05' then 'PlatformFundsTransfer'
when '06' then 'BorrowingHybrid'
when '08' then 'PlatformMarketing'
when '10' then 'PlatformIncome'
when '11' then 'PlatformCompensatory'
when '12' then 'ThirdMarketing'
when '13' then 'PlatformUrgent'
when '14' then 'Transition' end as business_type
,a.AMOUNT as balance
,a.FREEZE_AMOUNT as freeze_amount
,'' as customer_id
,'1000000001' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,0 as creator
,0 as last_updater
,'U' as state
,'CNY' as currency
,a.GMT_CREATE as bank_create_time
,nvl(a.GMT_MODIFIED,a.GMT_CREATE) as bank_update_time
from UCF_ACCOUNT a left join UCF_MEMBER_USER u on a.USER_ID = u.USER_ID and a.REF_MERCHANT = u.REF_MERCHANT
where (a.GMT_CREATE < to_date('2018-12-16','yyyy-mm-dd')
         or a.GMT_MODIFIED < to_date('2018-12-16','yyyy-mm-dd'));'''

ucfBidSQL = '''
select
 b.BID_ID as bank_bid_id
,b.ID as bid_flow_id
,b.BORR_INNER_USER_ID as bank_user_id
,b.BORR_OUT_USER_ID as p2p_user_id
,b.MERCHANT_ID as bank_platform_id
,b.BID_NAME as bid_name
,b.AMOUNT as amount
,'CNY' as currency
,b.CYCLE as period
,b.RATE as rate
,'' as interest
,'' as service_amount
,case b.BID_STATUS
  when 'W' then 'Waiting'
  when 'II' then 'Investing'
  when 'GI' then 'Lending'
  when 'GD' then 'Lended'
  when 'CI' then 'Flowing'
  when 'CD' then 'Flowed' end as bid_status
,case b.TYPE
  when '01' then 'Credit'
  when '02' then 'Mortgage'
  when '03' then 'Transfer'
  when '99' then 'Other' end as bid_type
,b.GRANTED_AMOUNT as granted_amout
,b.REPAYED_AMOUNT as repayed_amount
,'' as repayed_interest
,'' as balance_amount
,'' as repayed_normal_amount
,'' as repayed_overdue_amount
,'' as compensation_amount
,'' as compensation_repayed_amount
,'' as compensation_direct_amount
,'' as compensation_indirect_amount
,'' as compensation_overdue_amount
,b.REQUEST_TIME as request_time
,b.GMT_GRANTED as granted_time
,'' as overdue_time
,'' as should_repay_time
,b.GMT_REPAYED as finish_repay_time
,case e.IS_ENTRUSTEDPAY
when '1' then 'Y' else 'N' end as entrusted_pay
,b.IS_AUTO as is_auto
,'' as raise_duration
,'' as deal_rate
,'' as comprehensive_rate
,case b.REPAYMENT_TYPE
  when '01' then 'OneTimeServicing'
  when '02' then 'FixedBasisMortgage'
  when '03' then 'FixedPaymentMortgage'
  when '04' then 'FirstInterestLastPrincipal'
  when '99' then 'Other' end as repayment_type
,b.PRODUCT_TYPE as product_type
,'' as lender_rate
,'' as borr_purpose
,'' as customer_id
,'1000000001' as depository_id
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
,'' as user_type
,'' as real_name
,'' as cred_type
,'' as cred_no
,'' as relation_group_id
,b.GMT_CREATE as bank_create_time
,nvl(b.GMT_MODIFIED,b.GMT_CREATE) as bank_update_time
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
 from UCF_TRADE_BID_INFO b
       left join UCF_TRADE_BID_INFO_EXTRA e on b.BID_ID = e.BID_ID and b.MERCHANT_ID = e.MERCHANT_ID
 where (b.GMT_CREATE < to_date('2018-12-16','yyyy-mm-dd')
         or b.GMT_MODIFIED < to_date('2018-12-16','yyyy-mm-dd'));'''

ucfObligatorySQL = '''
select
o.ID as bank_obligatory_id
,o.ID as obligatory_flow_id
,o.BIDID as bank_bid_id
,u.USER_ID as bank_user_id
,'' as customer_id
,'' as borrower_bank_user_id
,'' as borrower_customer_id
,o.MERCHANTID as bank_platform_id
,o.SUMAMOUNT as sum_amount
,o.FREEZE_AMOUNT as freeze_amount
,o.REPAYEDAMOUNT as repayed_amount
,'' as balance_amount
,'' as repayed_normal_amount
,'' as repayed_overdue_amount
,'' as compensation_amount
,'' as compensation_repayed_amount
,'' as compensation_direct_amount
,'' as compensation_indirect_amount
,'' as compensation_overdue_amount
,'1000000001' as depository_id
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
,b.AMOUNT as bid_amount
,case b.BID_STATUS
  when 'W' then 'Waiting'
  when 'II' then 'Investing'
  when 'GI' then 'Lending'
  when 'GD' then 'Lended'
  when 'CI' then 'Flowing'
  when 'CD' then 'Flowed' end as bid_status
,case b.TYPE
  when '01' then 'Credit'
  when '02' then 'Mortgage'
  when '03' then 'Transfer'
  when '99' then 'Other' end as bid_type
,case u.user_type
  when '1' then 'Person'
  when '2' then 'Enterprise'
  when '3' then 'Platform' end as user_type
,trim(u.REAL_NAME) as real_name
,case u.CERT_TYPE
  when 'IDC' then 'IDC'
  when 'GAT' then 'GAT'
  when 'MILITARY' then 'MILITARY'
  when 'PASS_PORT' then 'PASSPORT'
  when 'BLC' then 'BLC'
  when 'FPR' then 'FPR'
  when 'USCC' then 'USCC' end as cred_type
,u.CERT_NO as cred_no
,b.CYCLE as period
,o.GMT_CREATE as bank_create_time
,nvl(o.GMT_MODIFIED,o.GMT_CREATE) as bank_update_time
,'' as borrower_p2p_user_id
,o.USERID as bank_p2p_user_id
,'' as province_code
,'' as province_name
,'' as city_code
,'' as city_name
,'' as longitude
,'' as latitude
,'' as gender
,'' as birthday
from UCF_TRADE_OBLIGATORY o
       left join UCF_TRADE_BID_INFO b on o.BIDID = b.BID_ID and o.MERCHANTID = b.MERCHANT_ID
       left join UCF_MEMBER_USER u on o.USERID = u.REF_USER and o.MERCHANTID = u.REF_MERCHANT
where (o.GMT_CREATE < to_date('2018-12-16','yyyy-mm-dd')
         or o.GMT_MODIFIED < to_date('2018-12-16','yyyy-mm-dd'));'''

ucfTradeSQL = '''
select
 t.ID as bank_trade_id
,t.ID as trade_flow_id
,t.OUT_ORDER_ID as p2p_flow_id
,t.MERCHANT_ID as bank_platform_id
,'' as platform_name
,t.BID_ID as bank_bid_id
,t.PAY_USER_INNER_ID as pay_bank_user_id
,t.PAY_USER_OUT_ID as pay_p2p_user_id
,'' as pay_customer_id
,t.RECEIVE_USER_INNER_ID as receive_bank_user_id
,t.RECEIVE_USER_OUT_ID as receive_b2b_user_id
,'' as receive_customer_id
,t.AMOUNT as amount
,t.ACC_AMOUNT as acc_amount
,t.ORG_AMOUNT as org_amount
,'CNY' as currency
,t.TRANS_CODE as trans_code
,t.TRANS_CODE as sub_trans_code
,case t.STATUS
  when 'S' then 'Success'
  when 'I' then 'Pending'
  when 'F' then 'Fail' end as order_status
,t.REQUEST_TIME as request_time
,t.REMARK as remark
,t.SOURCE as source
,t.GMT_FINISHED as finished_time
,nvl(t.GMT_MODIFIED,t.GMT_CREATE) as bank_update_time
,t.GMT_FINISHED as finished_date
,t.BANK_CODE as bank_code
,t.ISSUER as issuer
,t.CARD_NAME as card_name
,t.BANK_CARD_NO as bank_card_no
,case t.IS_ENTRUSTEDPAY
 when '1' then 'Y' else 'N' end as entrusted_pay
,t.FEE_AMOUNT as fee_amount
,t.EXPIRE_TIME as order_expire_time
,t.IS_REFUND as is_refund
,'' as trade_type
,'1000000001' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,0 as creator
,0 as last_updater
,'U' as state
,'' as user_type
,'' as real_name
,'' as cred_type
,'' as cred_no
,'' as belonging_code
,'' as belonging_name
,t.SUB_TRANS_CODE as traning_code
,'' as trans_code_type
,t.GMT_CREATE as bank_create_time
,t.INNER_BATCH_ID as bank_order_id
,'' as order_trans_code
,'' as order_sub_trans_code
,'' as order_traning_code
 from UCF_TRADE_TRANS_INFO t 
 where (t.GMT_CREATE < to_date('2018-12-16','yyyy-mm-dd')
         or t.GMT_MODIFIED < to_date('2018-12-16','yyyy-mm-dd'));'''

ucfTradeOrderSQL = '''
select
ID as bank_order_id
,MERCHANT_ID as bank_platform_id
,SOURCE as source
,OUT_BATCH_ID as out_bank_order_id
,REF_ID as ref_order_id
,BID_ID as bid_id
,TRANS_CODE as trans_code
,SUB_TRANS_CODE as sub_trans_code
,SUB_TRANS_CODE as traning_code
,case STATUS
  when 'S' then 'Success'
  when 'I' then 'Pending'
  when 'F' then 'Fail' end as status
,TOTAL_NUM as total_num
,TOTAL_AMOUNT as total_amount
,CURRENCY as currency
,NOTICE_URL as notice_url
,NOTICE_STATUS as notice_status
,REQUEST_TIME as request_time
,REMARK as remark
,GMT_CREATE as bank_create_time
,GMT_MODIFIED as bank_update_time
,GMT_FINISHED as finished_time
,'' as procession_time
,'' as order_version
,RECEIVER_NEED_FREEZE as receiver_need_freeze
,FREEZE_TYPE as freeze_type
,'' as request_no
,'' as flow_no
,'' as total_income
,'' as commission
,'' as trans_type
,'' as marketing
,'' as repair_type
,'' as biz_origin
,'' as fail_code
,'' as fail_reason
,'' as process_type
,'1000000001' as depository_id
,'100000000001' as saas_id
,sysdate as create_time
,sysdate as last_update_time
,0 as creator
,0 as last_updater
,'U' as state
from UCF_TRADE_BATCH_INFO;'''
