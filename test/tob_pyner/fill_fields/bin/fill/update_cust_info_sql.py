generateSQL = '''
                insert into pyner_customer 
                (user_type, real_name, cred_type, cred_no, saas_id, create_time, last_update_time, creator, last_updater, state)
                select user_type, real_name,cred_type, cred_no, 100000000001, now(),now(),0,0,'U' 
                from pyner_user 
                group by cred_type, cred_no'''

updatePlatformCredInfoUSCCSQL = '''
update pyner_platform set cred_type='USCC',cred_no=social_credit_code where cred_no is null and social_credit_code is not null;
'''
updatePlatformCredInfoBLCSQL = '''
update pyner_platform set cred_type='BLC',cred_no=business_license where cred_no is null and business_license is not null;
'''

generatePlatformSQL = '''
insert ignore into pyner_customer
                (user_type, real_name, cred_type, cred_no, saas_id, create_time, last_update_time, creator, last_updater, state)
select 'Enterprise', platform_name, cred_type, cred_no, 100000000001, now(), now(), 0, 0,'U'
from pyner_platform group by cred_type, cred_no'''

updateUserCustomerIdSQL = '''
                             update pyner_user u, pyner_customer c
                               set u.customer_id = c.customer_id
                             where u.cred_type = c.cred_type
                               and u.cred_no = c.cred_no'''

updatePersonCustomerIdSQL = '''
                            update pyner_user_person p, pyner_user u
                              set p.customer_id = u.customer_id
                            where p.bank_user_id = u.bank_user_id
                            and p.bank_platform_id = u.bank_platform_id 
                            and p.depository_id = u.depository_id'''

updateEnterpriseCustomerIdSQL = '''
                            update pyner_user_enterprise e, pyner_user u
                              set e.customer_id = u.customer_id
                            where e.bank_user_id = u.bank_user_id
                            and e.bank_platform_id = u.bank_platform_id 
                            and e.depository_id = u.depository_id'''

updatePlatformCustomerIdSQL = '''
update pyner_platform p, pyner_customer c
set p.customer_id = c.customer_id
where p.cred_type = c.cred_type
	and p.cred_no = c.cred_no'''

updateAccountCustomerIdSQL1 = '''
                            update pyner_account a, pyner_user u
                            set a.customer_id = u.customer_id
                            where a.bank_user_id = u.bank_user_id
                            and a.bank_platform_id = u.bank_platform_id 
                            and a.depository_id = u.depository_id'''

updateAccountCustomerIdSQL2 = '''
                            update pyner_account a, pyner_platform p
                            set a.customer_id = p.customer_id
                            where a.bank_user_id = p.bank_platform_id
                              and a.bank_platform_id = p.bank_platform_id
                              and a.depository_id = p.depository_id'''

updateBidCustomerIdSQL = '''
                            update pyner_bid b, pyner_user u
                            set b.customer_id   = u.customer_id,
                                b.user_type     = u.user_type,
                                b.real_name     = u.real_name,
                                b.cred_type     = u.cred_type,
                                b.cred_no       = u.cred_no,
                                b.province_code = u.province_code,
                                b.province_name = u.province_name,
                                b.city_code     = u.city_code,
                                b.city_name     = u.city_name,
                                b.longitude     = u.longitude,
                                b.latitude      = u.latitude
                            where b.bank_user_id = u.bank_user_id
                              and b.bank_platform_id = u.bank_platform_id
                              and b.depository_id = u.depository_id'''

updateObligatoryCustomerIdSQL = '''
                            update pyner_obligatory o, pyner_user u
                            set o.customer_id   = u.customer_id,
                                o.user_type     = u.user_type,
                                o.real_name     = u.real_name,
                                o.cred_type     = u.cred_type,
                                o.cred_no       = u.cred_no,
                                o.province_code = u.province_code,
                                o.province_name = u.province_name,
                                o.city_code     = u.city_code,
                                o.city_name     = u.city_name,
                                o.longitude     = u.longitude,
                                o.latitude      = u.latitude
                            where o.bank_user_id = u.bank_user_id
                              and o.bank_platform_id = u.bank_platform_id
                              and o.depository_id = u.depository_id'''

updateTradePayCustomerIdSQL = '''
                              update pyner_trade t, pyner_user u
                              set t.pay_customer_id = u.customer_id,
                                  t.user_type       = u.user_type,
                                  t.real_name       = u.real_name,
                                  t.cred_type       = u.cred_type,
                                  t.cred_no         = u.cred_no
                              where t.pay_bank_user_id = u.bank_user_id
                                and t.bank_platform_id = u.bank_platform_id
                                and t.depository_id = u.depository_id'''

updateTradeReceiveCustomerIdSQL = '''
                                update pyner_trade t, pyner_user u
                                set t.receive_customer_id = u.customer_id
                                where t.receive_bank_user_id = u.bank_user_id
                                  and t.bank_platform_id = u.bank_platform_id
                                  and t.depository_id = u.depository_id'''

updateBidPersonInfoSQL = '''
                            update pyner_bid b , pyner_user_person p 
                            set b.gender = p.gender, b.birthday = p.birthday 
                            where b.bank_user_id = p.bank_user_id
                              and b.bank_platform_id = p.bank_platform_id
                              and b.depository_id = p.depository_id'''

updateObligatoryPersonInfoSQL = '''
                            update pyner_obligatory o , pyner_user_person p
                            set o.gender = p.gender, o.birthday = p.birthday
                            where o.bank_user_id = p.bank_user_id
                              and o.bank_platform_id = p.bank_platform_id
                              and o.depository_id = p.depository_id'''

updateReportPersonInfoSQL = '''
                            update pyner_user_report r , pyner_user_person p
                            set r.gender = p.gender, r.birthday = p.birthday
                            where r.bank_user_id = p.bank_user_id
                              and r.bank_platform_id = p.bank_platform_id
                              and r.depository_id = p.depository_id'''
