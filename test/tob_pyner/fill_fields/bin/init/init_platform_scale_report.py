from test.tob_pyner.fill_fields.bin.init.sqls.platform_scale_report_sql import *
from test.tob_pyner.fill_fields.util.MySqlHelper import select_insert


def init_user_scale_report():
    """初始化用户规模报表信息"""
    select_insert(initUserScaleReportSQL)
    print('init_user_scale_report Finish!')


def init_custopt_address_report():
    """地区(日/累计)报表"""
    select_insert(initCustoptAddressSQL)
    print('init_custopt_address_report Finish!')


def init_custopt_gender_report():
    """用户性别总数(日/累计)报表"""
    select_insert(initCustoptGenderSQL)
    print('init_custopt_gender_report Finish!')


def init_granted_report():
    """放款金额报表"""
    select_insert(initGrantedReportSQL)
    print('init_granted_report Finish!')


def init_platform_scale_report():
    init_user_scale_report()
    init_custopt_address_report()
    init_custopt_gender_report()
    init_granted_report()


if __name__ == '__main__':
    init_platform_scale_report()
