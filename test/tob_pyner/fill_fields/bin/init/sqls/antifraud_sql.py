initEnterpriseAntifraudTaskSQL = '''
insert into b2b_pyner_antifraud.enterprise_task
    (finish, customer_id, enterprise_id, enterprise_name, creator, last_updater, state, create_time, last_update_time)
select 'A', customer_id, bank_user_id, enterprise_name, 0, 0, 'U', now(), now()
from pyner_user_enterprise group by customer_id'''

initEnterpriseAntifraudInfoSQL = '''
insert into b2b_pyner_antifraud.pyner_antifraud_org_info (customer_id,
                                                              group_id,
                                                              name,
                                                              biz_license_code,
                                                              bad_credit,
                                                              area,
                                                              registered_capitalcol,
                                                              legal_person_id,
                                                              legal_person,
                                                              create_time,
                                                              last_update_time,
                                                              creator,
                                                              last_updater,
                                                              state)
select customer_id,
       null,
       enterprise_name,
       business_license,
       'N',
       null,
       null,
       null,
       legal_person_name,
       now(),
       now(),
       0,
       0,
       'U'
from pyner_user_enterprise group by customer_id'''
