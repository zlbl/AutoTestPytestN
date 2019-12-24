#!/usr/bin/python3
# -*- coding:utf-8 -*-
# pip3 install atlassian-python-api

from atlassian import Confluence
import os

global_nums = 1

confluence = Confluence(
    url='http://confluence.treefinance.com.cn',
    username='你的用户名',
    password='你的密码')

projects_path = '/Users/yandongjun/Downloads/tower_documents'

global_space = 'DSDOC'

def get_project_files2(project_dir):
    """
    获取project_dir目录下的所有一级目录，及一级目录中的文件信息
    :param project_dir:
    :return:
    """
    projects_files_map = {}

    for root, dirs, files in os.walk(project_dir):
        if root is project_dir:
            for dir_name in dirs:
                md_file_names = os.listdir(root + '/' + str(dir_name))
                projects_files_map[dir_name] = md_file_names

    print('projects_files_map is', projects_files_map)
    return projects_files_map


def create_update_pages(projects_files_map):
    """
    map的格式是 k:project_name v:file_name集合
    :param projects_files_map:
    :return:
    """
    for project_name, md_file_names in projects_files_map.items():
        # 先判断项目页面是否创建
        project_page_id = check_create_space_page(project_name)

        if project_page_id and int(project_page_id) > 0:
            # 轮询将文件添加至项目页面下
            for md_file_name in md_file_names:
                # 单个文件创建
                file_content = get_project_file_content(project_name, md_file_name)
                create_update_page(project_page_id, md_file_name, file_content)
                global global_nums
                global_nums = global_nums + 1
            print('项目 - ', project_name, ' 页面创建完成')
        else:
            print('项目 - ', project_name, ' 目录创建失败，请检查')


def create_update_page(parent_id, file_name, file_content):
    print('parent_id ', parent_id, ' file_name is ', file_name)
    status = confluence.update_or_create(parent_id=parent_id, title=file_name,
                                         body=file_content,
                                         representation='wiki')
    print('create_update_page status is ', status)


def check_create_space_page(page_title):
    status = get_space_page(page_title)

    if status and int(status['id']) > 0:
        page_id = status['id']
        print('check_create_space_page 已存在page_id=', page_id)
    else:
        status_create = create_space_page(page_title)

        if status_create and int(status_create['id']) > 0:
            page_id = status_create['id']
            print('check_create_space_page 生成page_id=', page_id)
    return page_id


def check_create_space():
    res = get_space(global_space)
    if 'No space' in res:
        res = create_space(global_space)
        print('check_create_space 生成page_id=', res)

    else:
        print('check_create_space 已存在global_space=', global_space)


def create_space_page(page_title):
    status = confluence.create_page(space=global_space, title=page_title, body='', representation='wiki')
    print('create_space_page status is ', status)
    return status


def get_space_page(page_title):
    status = confluence.get_page_by_title(space=global_space, title=page_title)
    print('get_space_page status is ', status)
    return status


def get_space(space_key):
    status = confluence.get_space(space_key=space_key)
    print('get_space_page status is ', status)
    return status


def create_space(space_key):
    status = confluence.create_space(space_key=space_key, space_name='TOWER文档迁移')
    print('create_space status is ', status)
    return status
    # curl -u 你的用户名:你的密码 -X POST -H 'Content-Type: application/json' -d ' {"key": "DSDOC", "name": "TOWER文档迁移", "description": { "plain": { "value": "This is an common space", "representation": "plain" } }, "metadata": {}}' http://confluence.treefinance.com.cn/rest/api/space
    # print('请手动创建')


def delete_space(space_key):
    resp = confluence.delete_space(space_key=space_key)
    print('test_delete_confluence_space resp is ', resp)
    return resp
    print("请谨慎使用这个方法")


def get_project_file_content(project_name, md_file_name):
    """
    读取特定某项目下的某文件的内容
    :param project_name:
    :param md_file_name:
    :return:
    """
    with open(projects_path + '/' + project_name + '/' + md_file_name, 'r') as f:
        content = f.read()
        return content
    return None


def test_delete_confluence_space():
    """
    提示：如果你希望删除一个页面和这个页面下面的很多子页面。
    1. 创建一个临时新空间。
    2. 移动上级页面到新空间中。这个页面的所有子页面也会被一同移动。
    3. 删除这个空间。
    :return:
    """
    print('test_delete_confluence_space')
    # resp = delete_space(global_space)
    # print('test_delete_confluence_space resp is ', resp)
    # resp = create_space(global_space)
    # print('create_space resp is ', resp)


def test_init_confluence_pages():
    """
    tower to confluence tool main method
    :return:
    """
    projects_files_map = get_project_files2(projects_path)

    # check_create_space()

    create_update_pages(projects_files_map)
