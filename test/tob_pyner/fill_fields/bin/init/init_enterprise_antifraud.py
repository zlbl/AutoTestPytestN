from test.tob_pyner.fill_fields.bin.init.sqls.antifraud_sql import *
from test.tob_pyner.fill_fields.util.MySqlHelper import select_insert


def init_enterprise_antifraud_task():
    """初始化企业反欺诈任务"""
    select_insert(initEnterpriseAntifraudTaskSQL)
    print('init_enterprise_antifraud_task Finish!')


def init_enterprise_antifraud_info():
    """初始化企业反欺诈信息"""
    select_insert(initEnterpriseAntifraudInfoSQL)
    print('init_enterprise_antifraud_info Finish!')


def init_enterprise_antifraud():
    """
    注意！需先将 enterprise_task、 pyner_antifraud_org_info设置自增主键
    ALTER TABLE enterprise_task MODIFY id bigint(20) unsigned NOT NULL auto_increment;
    ALTER TABLE pyner_antifraud_org_info MODIFY id bigint(20) NOT NULL auto_increment;
    :return:
    """
    init_enterprise_antifraud_task()
    init_enterprise_antifraud_info()


if __name__ == '__main__':
    init_enterprise_antifraud()
