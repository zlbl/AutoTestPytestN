from datetime import datetime

from test.tob_pyner.fill_fields.bin.calculate.calc_bid import calc_bid
from test.tob_pyner.fill_fields.bin.calculate.sync_info import sync_info
from test.tob_pyner.fill_fields.bin.fill.customer_bin import generate_customer_id
from test.tob_pyner.fill_fields.bin.fill.person_info_bin import person_info_transform, update_person_info
from test.tob_pyner.fill_fields.bin.fill.user_info_bin import user_area_transform
from test.tob_pyner.fill_fields.bin.fill.user_report_bin import generate_user_report
from test.tob_pyner.fill_fields.bin.init.init_assert_quality_report import init_assert_quality_report
from test.tob_pyner.fill_fields.bin.init.init_deal_info_report import init_deal_info_report
from test.tob_pyner.fill_fields.bin.init.init_enterprise_antifraud import init_enterprise_antifraud
from test.tob_pyner.fill_fields.bin.init.init_platform_scale_report import init_platform_scale_report


def step_1():
    """计算用户信息"""
    # 生成用户地区、坐标信息 进入user表
    user_area_transform()

    # 个人信息 性别、出生日期转换
    person_info_transform()
    """
    注意!
    ALTER TABLE pyner_customer MODIFY customer_id bigint(20) NOT NULL auto_increment COMMENT '客户ID';
    ALTER TABLE pyner_customer AUTO_INCREMENT = 1000000001;
    """
    # 生成 customer_id 相关信息
    generate_customer_id()

    # 创建用户报表信息
    generate_user_report()

    # 更新个人信息的性别 出生日期
    update_person_info()


def step_2():
    """企业反欺诈任务创建"""
    """
        注意！需先将 enterprise_task、 pyner_antifraud_org_info设置自增主键
        ALTER TABLE enterprise_task MODIFY id bigint(20) unsigned NOT NULL auto_increment;
        ALTER TABLE pyner_antifraud_org_info MODIFY id bigint(20) NOT NULL auto_increment;
    """
    init_enterprise_antifraud()


def step_3():
    """计算值处理"""
    # 计算标的表相关信息
    calc_bid()

    # 同步交易信息用于冗余查询
    sync_info()


def step_4():
    """生成报表数据"""
    # 初始化平台规模报表数据
    init_platform_scale_report()

    # 初始化交易信息报表数据
    init_deal_info_report()

    # 初始化资产质量报表数据
    init_assert_quality_report()


def main():
    print('开始时间:', datetime.now())
    step_1()
    # step_2()
    # step_3()
    # step_4()
    print('结束时间:', datetime.now())


if __name__ == '__main__':
    main()
