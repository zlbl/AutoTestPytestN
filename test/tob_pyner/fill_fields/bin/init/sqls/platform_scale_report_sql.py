initUserScaleReportSQL = '''
INSERT INTO b2b_pyner_statistic.pyner_report_user_scale (count_time,
                                                         saas_id,
                                                         bank_platform_id,
                                                         depository_id,
                                                         count_user,
                                                         user_type,
                                                         business_type,
                                                         date_type,
                                                         create_time,
                                                         last_update_time,
                                                         state)
SELECT '1970-01-02 00:00:00'                    count_time,
       pynerUser.saas_id                        saas_id,
       pynerUser.bank_platform_id               bank_platform_id,
       pynerUser.depository_id                  depository_id,
       COUNT(DISTINCT (pynerUser.bank_user_id)) count_user,
       pynerUser.user_type                      user_type,
       pynerUser.business_type                  business_type,
       'day'                                    date_type,
       now()                                    create_time,
       now()                                    last_update_time,
       'U'                                      state
FROM b2b_pyner_depository.pyner_user pynerUser
WHERE pynerUser.state = 'U'
  AND pynerUser.bank_create_time < '2018-12-16'
  AND pynerUser.business_type in ('Borrower', 'Lender')
GROUP BY bank_platform_id, depository_id, saas_id, user_type,
         business_type'''

initCustoptAddressSQL = '''
INSERT INTO b2b_pyner_statistic.pyner_report_custopt_address (bank_platform_id,
                                                              depository_id,
                                                              saas_id,
                                                              user_type,
                                                              business_type,
                                                              count_bank_user,
                                                              date_type,
                                                              province_code,
                                                              province_name,
                                                              longitude,
                                                              latitude,
                                                              bank_create_time,
                                                              create_time,
                                                              last_update_time,
                                                              state)
SELECT pynerUserReport.bank_platform_id    bank_platform_id,
       pynerUserReport.depository_id       depository_id,
       pynerUserReport.saas_id             saas_id,
       pynerUserReport.user_type           user_type,
       pynerUserReport.business_type       business_type,
       COUNT(pynerUserReport.bank_user_id) count_bank_user,
       'day'                               date_type,
       pynerUserReport.province_code       province_code,
       pynerUserReport.province_name       province_name,
       pynerUserReport.longitude           longitude,
       pynerUserReport.latitude            latitude,
       '1970-01-01 08:00:01'               bank_create_time,
       now()                               create_time,
       now()                               last_update_time,
       'U'                                 state
FROM b2b_pyner_depository.pyner_user_report pynerUserReport
WHERE state = 'U'
  AND province_code IS NOT NULL
  AND business_type in ('Borrower', 'Lender')
  AND bank_create_time
        < '2018-12-16'
GROUP BY bank_platform_id,
         depository_id,
         province_code,
         latitude,
         saas_id,
         user_type,
         province_name,
         business_type,
         longitude'''

initCustoptGenderSQL = '''
INSERT INTO b2b_pyner_statistic.pyner_report_custopt_gender (bank_platform_id,
                                                             depository_id,
                                                             saas_id,
                                                             user_type,
                                                             business_type,
                                                             count_bank_user,
                                                             date_type,
                                                             bank_create_time,
                                                             gender,
                                                             create_time,
                                                             last_update_time,
                                                             state)
SELECT pynerUserReport.bank_platform_id               bank_platform_id,
       pynerUserReport.depository_id                  depository_id,
       pynerUserReport.saas_id                        saas_id,
       pynerUserReport.user_type                      user_type,
       pynerUserReport.business_type                  business_type,
       count(DISTINCT (pynerUserReport.bank_user_id)) count_bank_user,
       'day'                                          date_type,
       '1970-01-02 00:00:00'                          bank_create_time,
       pynerUserReport.gender                         gender,
       now()                                          create_time,
       now()                                          last_update_time,
       'U'                                            state
FROM b2b_pyner_depository.pyner_user_report pynerUserReport
WHERE pynerUserReport.state = 'U'
  AND pynerUserReport.gender IS NOT NULL
  AND pynerUserReport.business_type IN ('Borrower', 'Lender')
  AND pynerUserReport.bank_create_time < '2018-12-16'
  AND pynerUserReport.user_type = 'Person'
GROUP BY gender, bank_platform_id, depository_id, saas_id, user_type, business_type'''

initGrantedReportSQL = '''
INSERT INTO b2b_pyner_statistic.pyner_report_grante (granted_time,
                                                     saas_id,
                                                     bank_platform_id,
                                                     depository_id,
                                                     sum_amount,
                                                     count_num,
                                                     date_type,
                                                     create_time,
                                                     last_update_time,
                                                     state)
SELECT '1970-01-02 00:00:00'       granted_time,
       pynerBid.saas_id            saas_id,
       pynerBid.bank_platform_id   bank_platform_id,
       pynerBid.depository_id      depository_id,
       sum(pynerBid.granted_amout) sum_amount,
       count(pynerBid.bid_flow_id) count_num,
       'day'                       date_type,
       now()                       create_time,
       now()                       last_update_time,
       'U'                         state
FROM b2b_pyner_depository.pyner_bid pynerBid
WHERE pynerBid.state = 'U'
  AND pynerBid.granted_time < '2018-12-16'
GROUP BY bank_platform_id, depository_id, saas_id'''
