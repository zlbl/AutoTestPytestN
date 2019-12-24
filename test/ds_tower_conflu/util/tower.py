# -*- coding: utf-8 -*-
import sys
from imp import reload

import requests
import json
import datetime
import time
import pytz
import re
import os

# reload(sys)
# sys.setdefaultencoding('utf-8')
requests.packages.urllib3.disable_warnings()

# 全局token,一次授权2小时内有效,此处为初始值
ACCESS_TOKEN = 'cd5ceabe24ba4ea5f142c7efedac8fe201310baed56341cf8712ef9800db91e5'
REFRESH_TOKEN = '58742a0c68221be74177de027f17a923f84a63072d409036d537136a0cdec7ad'
# git 工程ID列表
GIT_PROJECT_IDS = [31, 62, 176, 291, 187, 198, 322, 356, 406, 434, 446, 490, 579, 589, 649]
GIT_PROJECT_NAMES = ['信审', '催收', '客服', '运营', '渠道对外', '渠道', 'acrm-provider', 'acrm-uc', '委外', 'acrm', 'call-center',
                     '反欺诈', '费用', '钱包', '电销']
# tower 作业系统项目ID
TOWER_PROJECT_ID = 'b7ffb95f3d104dd988c59598cb3cb770'
# tower 工作序列
NEEDS = '1df8035926b64d65997f7e7407cdee84'  # 需求
DEVELOP = '086ac15eef81401ab723fe19caa93c2a'  # 开发
TO_BE_TEST = 'e199da40824c4268a4527ad684219080'  # 待测试
TO_BE_PUBLISH = 'bf6cd934e30f430b8033eb50b23034db'  # 待上线
MILESTONE = '6e8fdf16de23424a8787ea36e16c860f'  # 发版计划

# todo格式
TODO_FORMAT = '[%s] issue#%d:%s'
# milestone格式
MILESTONE_FORMAT = '[%s] Release_%s'

utc = pytz.UTC  # tower是UTC时间


# 打印并写文件
def write_file_token(refresh_token):
    f = open('token.txt', 'wt')
    f.truncate()
    f.close()
    f = open('token.txt', 'a')
    f.write(refresh_token + '\n')
    f.close()


# 读文件
def read_file_token():
    f = open('token.txt', 'r')
    refresh_token = f.read()
    f.close()
    return refresh_token


def write_md_file(title, out_str):
    f = open(title + '.md', 'wt')
    f.truncate()
    f.close()
    f = open(title + '.md', 'a')
    f.write(out_str + '\n')
    f.close()


# list进行链式扩展
class ListWithLinkExtend(list):
    def extend(self, value):
        super(ListWithLinkExtend, self).extend(value)
        return self


# 获取datetime
def get_date_time(date_str):
    date_str = date_str.replace('T', ' ')
    date_str = date_str.replace('Z', '')
    date_str = date_str[:19]
    return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")


# 获取date
def get_date(date_str):
    if date_str is not None:
        date_str = date_str.replace('T', ' ')
        date_str = date_str.replace('Z', '')
        date_str = date_str[:10]
        return datetime.datetime.strptime(date_str, "%Y-%m-%d")
    else:
        return None


# 过滤HTML中的标签
# 将HTML中标签等信息去掉
# @param htmlstr HTML字符串.
def filter_tags(htmlstr):
    # 先过滤CDATA
    # re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
    # re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    # re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    # re_br = re.compile('<br\s*?/?>')  # 处理换行
    # re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    # re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    # s = re_cdata.sub('', htmlstr)  # 去掉CDATA
    # s = re_script.sub('', s)  # 去掉SCRIPT
    # s = re_style.sub('', s)  # 去掉style
    # s = re_br.sub('\n', s)  # 将br转换为换行
    # s = re_h.sub('', s)  # 去掉HTML 标签
    # s = re_comment.sub('', s)  # 去掉HTML注释
    # # 去掉多余的空行
    # blank_line = re.compile('\n+')
    # s = blank_line.sub('\n', s)
    # s = replaceCharEntity(s)  # 替换实体
    # return s
    print('filter_tags')


# 替换常用HTML字符实体.
# 使用正常的字符替换HTML中特殊的字符实体.
# 你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
# @param htmlstr HTML字符串.
def replaceCharEntity(htmlstr):
    CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
                     'lt': '<', '60': '<',
                     'gt': '>', '62': '>',
                     'amp': '&', '38': '&',
                     'quot': '"', '34': '"'}

    re_charEntity = re.compile(r'&#?(?P<name>\w+);')
    sz = re_charEntity.search(htmlstr)
    while sz:
        entity = sz.group()  # entity全称，如&gt;
        key = sz.group('name')  # 去除&;后entity,如&gt;为gt
        try:
            htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
        except KeyError:
            # 以空串代替
            htmlstr = re_charEntity.sub('', htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
    return htmlstr


def repalce(s, re_exp, repl_string):
    return re_exp.sub(repl_string, s)


# 判断是否是pending状态
def assert_pending(labels):
    for label in labels:
        if label.lower() == 'pending':
            return True
    return False


# 获取工程名
def get_project_name_by_id(project_id):
    for i in range(len(GIT_PROJECT_IDS)):
        if GIT_PROJECT_IDS[i] == project_id:
            return GIT_PROJECT_NAMES[i]


# 获取指定项目issue
def get_issues(project_id, state):
    url = 'http://192.168.5.252/api/v3/projects/' + str(project_id) + '/issues?state=' + \
          state + '&private_token=-pkAfsfwGL-nw7xxz36y&per_page=100'
    if state == '':
        url = 'http://192.168.5.252/api/v3/projects/' + str(project_id) + \
              '/issues?order_by=updated_at&private_token=-pkAfsfwGL-nw7xxz36y&per_page=100'
    # print url
    r = requests.get(url)
    issues = json.loads(r.text)

    return issues


# 获取指定项目milestone
def get_milestones(project_id):
    url = 'http://192.168.5.252/api/v3/projects/' + str(project_id) + '/milestones?private_token=-pkAfsfwGL-nw7xxz36y'
    # print url
    r = requests.get(url)
    milestones = json.loads(r.text)

    return milestones


# 按时间过滤issue
def filter_issues_by_date(issues, start_day, end_day):
    rows = []
    if issues.__len__ > 0:
        for issue in issues:
            pending = assert_pending(issue[u'labels'])
            if pending:
                continue
            update_at = get_date_time(issue[u'updated_at'])
            if start_day <= update_at < end_day:
                rows.append(issue)
    return rows


# 按时间和状态过滤milestone
def filter_milestone_by_date(milestones, state, start_day, end_day):
    rows = []
    if milestones.__len__ > 0:
        for milestone in milestones:
            update_at = get_date_time(milestone[u'updated_at'])
            if start_day <= update_at < end_day and milestone[u'state'] == state:
                rows.append(milestone)
    return rows


# 获取所有milestones
def get_git_all_milestone_by_condition(state, start, end):
    rows = []
    for project_id in GIT_PROJECT_IDS:
        milestones = get_milestones(project_id)
        if milestones and milestones.__len__ > 0:
            rows.append(filter_milestone_by_date(milestones, state, start, end))
    return rows


# 获取所有issues
def get_git_all_issues_by_condition(state, start, end):
    rows = []
    for project_id in GIT_PROJECT_IDS:
        issues = get_issues(project_id, state)
        if issues and issues.__len__ > 0:
            rows.append(filter_issues_by_date(issues, start, end))
    return rows


# 过滤出特定标签的issue
def filter_git_issue_labels(issues, label):
    rows = []
    if issues.__len__ > 0:
        for issue in issues:
            if issue[u'labels'] == label:
                rows.append(issue)
    return rows


# 过滤出有效的todos(未删除且状态不是已完成)
def filter_tower_active_not_complete_todos(todos):
    rows = []
    if todos.__len__ > 0:
        for todo in todos:
            if todo[u'attributes'][u'is-active'] and not todo[u'attributes'][u'is-completed']:
                rows.append(todo)
    return rows


# 过滤出有效的todos(未删除)
def filter_tower_active_todos(todos):
    rows = []
    if todos.__len__ > 0:
        for todo in todos:
            if todo[u'attributes'][u'is-active']:
                rows.append(todo)
    return rows


def get_now_access_token():
    url = 'https://tower.datatrees.com.cn/token'
    r = requests.get(url, verify=False)
    token = r.text.strip('\n')
    return token


def get_access_token():
    url = 'https://tower.im/oauth/token?client_id=e22f236652929ec85082800a50ba60f4241043e9d3b6e1047fa17d14d5d857f6' \
          '&client_secret=ef966ba17bd8c6e049bdb0d3a8bed3995193624d22142a4b6ceac093ec4fa433' \
          '&refresh_token=' + REFRESH_TOKEN + '&grant_type=refresh_token'
    r = requests.post(url)
    token = json.loads(r.text)
    return token[u'access_token'], token[u'refresh_token']


# --获取所有工程在指定日期内关闭的milestone--
def get_git_closed_milestones(start, end):
    return get_git_all_milestone_by_condition('closed', start, end)


# --获取所有工程在指定日期内未关闭的milestone--
def get_git_opened_milestones(start, end):
    return get_git_all_milestone_by_condition('active', start, end)


# --获取所有工程在指定日期内关闭的issues--
def get_git_closed_issues(start, end):
    return get_git_all_issues_by_condition('closed', start, end)


# --获取所有工程在指定日期内未关闭的issues--
def get_git_opened_issues(start, end):
    return get_git_all_issues_by_condition('opened', start, end)


# --获取tower上各个序列的todos列表--
def get_tower_todos_by_id(todolist_id):
    url = 'https://api.tower.im/v1/todolists/' + todolist_id + '/todos?access_token=' + ACCESS_TOKEN
    #print url
    r = requests.get(url)
    todos = json.loads(r.text)
    return todos[u'data']


# --获取tower特定项目的todolist列表--
def get_tower_todo_list(project_id):
    url = 'https://api.tower.im/v1/projects/' + project_id + '/todolists?access_token=' + ACCESS_TOKEN
    # print url
    r = requests.get(url)
    todos = json.loads(r.text)
    return todos[u'data']


# --新增todo--
def add_tower_todos_by_listid(todolist_id, content):
    url = 'https://api.tower.im/v1/todolists/' + todolist_id + '/todos?access_token=' + ACCESS_TOKEN
    # print url
    payload = json.dumps(content)
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, data=payload)
    resp = json.loads(r.text)
    return resp


# --更新todo状态为已完成--
def complete_todo_by_id(todo_id):
    url = 'https://api.tower.im/v1/todos/' + todo_id + '/completion?access_token=' + ACCESS_TOKEN
    # print url
    r = requests.post(url)
    resp = json.loads(r.text)
    return resp


# --更新todo的due_at--
def assign_todo_due_to_by_id(todo_id, due_at):
    url = 'https://api.tower.im/v1/todos/' + todo_id + '/due?access_token=' + ACCESS_TOKEN
    # print url
    payload = '{ "todos_due": { "due_at": "' + due_at + '" }}'
    headers = {'Content-Type': 'application/json'}
    r = requests.patch(url, headers=headers, data=payload)
    resp = json.loads(r.text)
    return resp


# --清除序列上未完成的todo--
def delete_todo_by_id(todo_id):
    url = 'https://api.tower.im/v1/todos/' + todo_id + '?access_token=' + ACCESS_TOKEN
    # print url
    requests.delete(url)
    return


# 检查milestone是否需要新增
def if_exist_in_milestones(todos, milestone, project_name):
    if todos.__len__ > 0:
        for todo in todos:
            content = todo[u'attributes'][u'content']
            if todo[u'attributes'][u'due-at'] is not None and content.find('[') >= 0:
                todo_project_name = content[content.find('[') + 1:content.find(']')]
                due_at = get_date(todo[u'attributes'][u'due-at'])
                if milestone[0][u'due_date'] is not None:
                    due_date = get_date(milestone[0][u'due_date'])
                    if due_at == due_date and todo_project_name == project_name:
                        return todo
            else:
                continue
    return None


# 检查todo是否已存在
def if_exist_in_todos(todos, issue, project_name):
    if todos.__len__ > 0:
        for todo in todos:
            content = todo[u'attributes'][u'content']
            if content is not None and content.find('issue') > 0 and content.find(':') > 0:
                todo_issue_id = content[content.find('#') + 1:content.find(':')]
                todo_project_name = content[content.find('[') + 1:content.find(']')]
                issue_id = issue[u'iid']
                if todo_issue_id == str(issue_id) and todo_project_name == project_name:
                    return todo
            else:
                continue
    return None


# 检查是否需要新增
def if_add_to_list(todos, milestone):
    if todos.__len__ > 0:
        for todo in todos:
            due_at = get_date(todo[u'attributes'][u'is-completed'])
            due_date = get_date(milestone[0][u'due_date'])
            if due_at == due_date:
                return False
            else:
                return True


# 获取标签
def get_flag(labels, state):
    for label in labels:
        if state == 'closed':
            return ""
        if label == '待测试':
            return TO_BE_TEST
        if label == '待上线':
            return TO_BE_PUBLISH
    return DEVELOP


# 业务方法
def milestone_update(start, end):
    # 获取未关闭的git上milestone,同时获取todo列表里未关闭的todo
    # 匹配是否有未加入todo列表的,未加入的加入
    milestones = get_git_opened_milestones(start, end)
    milestone_todos = filter_tower_active_not_complete_todos(get_tower_todos_by_id(MILESTONE))
    for milestone in milestones:
        if len(milestone) > 0:
            # 检查issue的变动是否需要新增todo
            project_name = get_project_name_by_id(milestone[0][u'project_id'])
            exist_todo = if_exist_in_milestones(milestone_todos, milestone, project_name)
            if exist_todo is None and milestone[0][u'due_date'] is not None:
                todo_content = MILESTONE_FORMAT % (
                    get_project_name_by_id(milestone[0][u'project_id']),
                    get_date(milestone[0][u'due_date']).strftime('%Y_%m_%d'))
                content = {'todo': {'content': todo_content, 'desc': milestone[0][u'title']}}
                print(content)
                resp = add_tower_todos_by_listid(MILESTONE, content)
                if resp is not None:
                    todo_id = resp[u'data'][u'id']
                    assign_todo_due_to_by_id(todo_id, milestone[0][u'due_date'])
    # 获取已关闭的milestone,查找todo列表里未关闭todo是否有,有的话更新成已完成
    close_milestones = get_git_closed_milestones(start, end)
    for milestone in close_milestones:
        if len(milestone) > 0:
            project_name = get_project_name_by_id(milestone[0][u'project_id'])
            exist_todo = if_exist_in_milestones(milestone_todos, milestone, project_name)
            if exist_todo is not None:
                complete_todo_by_id(exist_todo[u'id'])
    print("发版计划同步完毕")


# 工作序列更新
def dev_update(start, end):
    # 获取已关闭的git上issue,同时获取todo列表里未关闭的todo
    # 匹配是否有issueid匹配上的todo,关闭这个todo
    # 获取未关闭的issue,先判断todo列表里是否有相同issueid的,有的话删除后根据当前label加入到最新队列
    # 如果没有匹配到有,则直接根据label加入到相应队列
    issues_closed = get_git_closed_issues(start, end)
    todos = []
    for todolist in [NEEDS, DEVELOP, TO_BE_TEST, TO_BE_PUBLISH]:  # 获取所有todo并合并
        todos.extend(filter_tower_active_not_complete_todos(get_tower_todos_by_id(todolist)))
    for issue_project in issues_closed:
        if len(issue_project) > 0:
            for issue in issue_project:
                exist_todo = if_exist_in_todos(todos, issue, get_project_name_by_id(issue[u'project_id']))
                if exist_todo is not None:
                    complete_todo_by_id(exist_todo[u'id'])

    issues_opened = get_git_opened_issues(start, end)
    for issue_project in issues_opened:
        if len(issue_project) > 0:
            for issue in issue_project:
                exist_todo = if_exist_in_todos(todos, issue, get_project_name_by_id(issue[u'project_id']))
                if exist_todo is not None:
                    delete_todo_by_id(exist_todo[u'id'])
                # 加入最新序列
                if issue[u'assignee'] is not None and issue[u'assignee'][u'username'] == 'huanglizhou':  # 需求序列
                    queue = NEEDS
                else:
                    queue = get_flag(issue[u'labels'], issue[u'state'])
                todo_content = TODO_FORMAT % (
                    get_project_name_by_id(issue[u'project_id']), issue[u'iid'], issue[u'title'])
                content = {'todo': {'content': todo_content, 'desc': issue[u'title']}}
                print(content)
                add_tower_todos_by_listid(queue, content)
    print("工作序列同步完毕")


# PMO projectID
PMO_PROJECT_ID = '4076fe9fa73f41c4956d4eda5d4edd50'  # PMO项目跟踪情况

# PMO todolist列表
PMO_IMPORTANT_TODO_LIST = '4e6a943463f445fba5874d1156702eaa'  # 重点事项序列
PMO_PUBLISHED_LIST = 'db601edde6b24f00b612fbf9566f70b5'  # 已上线序列
PMO_PREPARE_PUBLISH_LIST = '96ea5bca5f744475b8e96b2b62e8801a'  # 待上线序列
PMO_TESTING_LIST = '9d0927f417b8446f9bd9bb27ec05337e'  # 测试中序列
PMO_DEVELOPING_LIST = '3ec39c5638e7490d9739821523d00f1b'  # 开发中序列
PMO_PREPARE_DEVELOP_LIST = 'd5a703a73a084cba8fa7aa40617ecea9'  # 待开发序列
PMO_ANALYSING_LIST = 'd8eba54face14734b5636b1a5c41a1f0'  # 需求分析中序列
PMO_BUSINESS_LIST = '0a4d5eda5bf44ce1b3372482b148504a'  # 业务（商务）阶段序列
PMO_MAINTENANCE_LIST = 'cbbbb493ca184a0198b227f17faf3d4f'  # 运维序列

important_todos = []
published_todos = []
prepare_publish_todos = []
testing_todos = []
developing_todos = []
prepare_develop_todos = []
analysing_todos = []
business_todos = []
maintenance_todos = []


# 获取PMO项目所有的有效todo列表
def get_all_todo():
    # 先获取所有todolist列表的有效todo列表
    important_todos = filter_tower_active_todos(get_tower_todos_by_id(PMO_IMPORTANT_TODO_LIST))
    published_todos = filter_tower_active_todos(get_tower_todos_by_id(PMO_PUBLISHED_LIST))
    prepare_publish_todos = filter_tower_active_todos(get_tower_todos_by_id(PMO_PREPARE_PUBLISH_LIST))
    testing_todos = filter_tower_active_todos(get_tower_todos_by_id(PMO_TESTING_LIST))
    developing_todos = filter_tower_active_todos(get_tower_todos_by_id(PMO_DEVELOPING_LIST))
    prepare_develop_todos = filter_tower_active_todos(get_tower_todos_by_id(PMO_PREPARE_DEVELOP_LIST))
    analysing_todos = filter_tower_active_todos(get_tower_todos_by_id(PMO_ANALYSING_LIST))
    business_todos = filter_tower_active_todos(get_tower_todos_by_id(PMO_BUSINESS_LIST))
    maintenance_todos = filter_tower_active_todos(get_tower_todos_by_id(PMO_MAINTENANCE_LIST))
    return important_todos, published_todos, prepare_publish_todos, testing_todos, developing_todos, \
           prepare_develop_todos, analysing_todos, business_todos, maintenance_todos


# 获取本周新增项目
def get_now_week_new_todo(todos, start_day, end_day):
    cnt = 0
    if todos.__len__ > 0:
        for todo in todos:
            if todo[u'attributes'][u'created-at'] is not None:
                create_at = get_date_time(todo[u'attributes'][u'created-at'])
                if start_day.replace(tzinfo=pytz.utc) <= create_at.replace(tzinfo=pytz.utc) < \
                        end_day.replace(tzinfo=pytz.utc):
                    cnt += 1
            else:
                continue
    return cnt


# 获取本周上线项目
def get_now_week_published_todo(todos, start_day, end_day):
    cnt = 0
    if todos.__len__ > 0:
        for todo in todos:
            if todo[u'attributes'][u'closed-at'] is not None:
                closed_at = get_date_time(todo[u'attributes'][u'closed-at'])
                if start_day.replace(tzinfo=pytz.utc) <= closed_at.replace(tzinfo=pytz.utc) < \
                        end_day.replace(tzinfo=pytz.utc):
                    cnt += 1
            else:
                continue
    return cnt


# 获取重点事项(非完成状态的本周todo)
def get_now_week_important_todo(todos, start_day, end_day):
    rows = []
    if todos.__len__ > 0:
        for todo in todos:
            if todo[u'attributes'][u'updated-at'] is not None and not todo[u'attributes'][u'is-completed']:
                closed_at = get_date_time(todo[u'attributes'][u'updated-at'])
                if start_day.replace(tzinfo=pytz.utc) <= closed_at.replace(tzinfo=pytz.utc) < \
                        end_day.replace(tzinfo=pytz.utc):
                    rows.append(todo)
            else:
                continue
    return rows


CONTENT_FORMAT_1 = '%d. %s: %s **[%s]**  \n'
CONTENT_FORMAT_2 = '%d. %s **[%s]**  \n'


# 获取某组本周已上线todo,待上线,测试中,开发中,待开发,需求分析中,业务(商务)阶段
def get_now_week_todo_by_dept(todos, dept, start_day, end_day, out, state, cnt):
    # if todos.__len__ > 0 and dept is not None:
    #     for todo in todos:
    #         content = todo[u'attributes'][u'content']
    #         if todo[u'attributes'][u'updated-at'] is not None:
    #             if content is not None and content.find(dept) >= 0:
    #                 content = content[content.find(dept) + len(dept.decode('utf-8')):len(content.decode('utf-8'))]
    #                 closed_at = get_date_time(todo[u'attributes'][u'updated-at'])
    #                 if start_day.replace(tzinfo=pytz.utc) <= closed_at.replace(tzinfo=pytz.utc) < \
    #                         end_day.replace(tzinfo=pytz.utc):
    #                     desc = todo[u'attributes'][u'desc']
    #                     # dr = re.compile(r'<[^>]+>', re.S)
    #                     desc = filter_tags(desc)
    #                     # BA组特别处理,根据是否完成变更state
    #                     if dept in ['[BA]', '[运维]'] and todo[u'attributes'][u'is-completed']:
    #                         state = '已完成'
    #
    #                     if desc is not None and len(desc.decode('utf-8')) > 0:
    #                         out += CONTENT_FORMAT_1 % (cnt, content, desc, state)
    #                     else:
    #                         out += CONTENT_FORMAT_2 % (cnt, content, state)
    #                     cnt += 1
    #         else:
    #             continue
    # return out, cnt
    print('get_now_week_todo_by_dept')


# 先读取最近一次的refresh_token,然后获取最新的access_token,并将新的refresh_token写文件
# REFRESH_TOKEN = read_file_token()
# ACCESS_TOKEN, REFRESH_TOKEN = get_access_token()
# print 'ACCESS_TOKEN:' + ACCESS_TOKEN
# print 'REFRESH_TOKEN:' + REFRESH_TOKEN
# write_file_token(REFRESH_TOKEN)

# 新方式获取token
# ACCESS_TOKEN = get_now_access_token()


# 作业系统组状态更新
def my_dept(start, end):
    # milestone_update(start, end)
    # dev_update(start, end)
    print('my_dept')


# 项目状态汇报
# 数据准备
def pmo_out(start, end):
    year_now = time.strftime("%Y")
    week_now = time.strftime("%W")
    new_todo_cnt = 0
    published_todo_cnt = 0
    titie = '# %s年第%d周项目状态汇报'
    file_title = '%s年第%d周项目状态汇报'
    # important_todos, published_todos, prepare_publish_todos, testing_todos, developing_todos, \
    # prepare_develop_todos, analysing_todos, business_todos, maintenance_todos = get_all_todo()
    # common_todos = [published_todos, prepare_publish_todos, testing_todos, developing_todos,
    #                 prepare_develop_todos, analysing_todos, business_todos, maintenance_todos]
    # common_todos = list(reduce(lambda a, b: ListWithLinkExtend(a).extend(ListWithLinkExtend(b)), common_todos))
    # new_todo_cnt = get_now_week_new_todo(common_todos, start, end)
    # published_todo_cnt = get_now_week_published_todo(published_todos, start, end)
    #
    # # 开始输出
    # out = ''
    # out += titie % (year_now, int(week_now)) + '\n'  # 输出标题
    # out += "### 项目摘要" + '\n'
    # out += "**新增项目：%d**  " % new_todo_cnt + '\n'
    # out += "**上线项目：%d**  " % published_todo_cnt + '\n\n'
    # # 输出重要事项
    # out += "### 重点事项" + '\n'
    # i = 1
    # for todo in get_now_week_important_todo(important_todos, start, end):
    #     out += str(i) + '. ' + todo[u'attributes'][u'content'] + ": " + todo[u'attributes'][u'desc'] + '\n'
    #     i += 1
    # # 输出作业系统工作摘要
    # i = 1
    # out += '\n' + "### 作业系统相关" + '\n'
    # out, i = get_now_week_todo_by_dept(published_todos, '[作业系统]', start, end, out, '已上线', i)
    # out, i = get_now_week_todo_by_dept(prepare_publish_todos, '[作业系统]', start, end, out, '待上线', i)
    # out, i = get_now_week_todo_by_dept(testing_todos, '[作业系统]', start, end, out, '测试中', i)
    # out, i = get_now_week_todo_by_dept(developing_todos, '[作业系统]', start, end, out, '开发中', i)
    # out, i = get_now_week_todo_by_dept(prepare_develop_todos, '[作业系统]', start, end, out, '待开发', i)
    # out, i = get_now_week_todo_by_dept(analysing_todos, '[作业系统]', start, end, out, '需求分析中', i)
    # out, i = get_now_week_todo_by_dept(business_todos, '[作业系统]', start, end, out, '业务(商务)阶段', i)
    #
    # # 输出资金管理工作摘要
    # i = 1
    # out += '\n' + "### 资金管理相关" + '\n'
    # out, i = get_now_week_todo_by_dept(published_todos, '[资金管理]', start, end, out, '已上线', i)
    # out, i = get_now_week_todo_by_dept(prepare_publish_todos, '[资金管理]', start, end, out, '待上线', i)
    # out, i = get_now_week_todo_by_dept(testing_todos, '[资金管理]', start, end, out, '测试中', i)
    # out, i = get_now_week_todo_by_dept(developing_todos, '[资金管理]', start, end, out, '开发中', i)
    # out, i = get_now_week_todo_by_dept(prepare_develop_todos, '[资金管理]', start, end, out, '待开发', i)
    # out, i = get_now_week_todo_by_dept(analysing_todos, '[资金管理]', start, end, out, '需求分析中', i)
    # out, i = get_now_week_todo_by_dept(business_todos, '[资金管理]', start, end, out, '业务(商务)阶段', i)
    #
    # # 输出数据研发工作摘要
    # i = 1
    # out += '\n' + "### 数据研发相关" + '\n'
    # out, i = get_now_week_todo_by_dept(published_todos, '[数据研发]', start, end, out, '已上线', i)
    # out, i = get_now_week_todo_by_dept(prepare_publish_todos, '[数据研发]', start, end, out, '待上线', i)
    # out, i = get_now_week_todo_by_dept(testing_todos, '[数据研发]', start, end, out, '测试中', i)
    # out, i = get_now_week_todo_by_dept(developing_todos, '[数据研发]', start, end, out, '开发中', i)
    # out, i = get_now_week_todo_by_dept(prepare_develop_todos, '[数据研发]', start, end, out, '待开发', i)
    # out, i = get_now_week_todo_by_dept(analysing_todos, '[数据研发]', start, end, out, '需求分析中', i)
    # out, i = get_now_week_todo_by_dept(business_todos, '[数据研发]', start, end, out, '业务(商务)阶段', i)
    #
    # # 输出产品整合工作摘要
    # i = 1
    # out += '\n' + "### 产品整合相关" + '\n'
    # out, i = get_now_week_todo_by_dept(published_todos, '[产品整合]', start, end, out, '已上线', i)
    # out, i = get_now_week_todo_by_dept(prepare_publish_todos, '[产品整合]', start, end, out, '待上线', i)
    # out, i = get_now_week_todo_by_dept(testing_todos, '[产品整合]', start, end, out, '测试中', i)
    # out, i = get_now_week_todo_by_dept(developing_todos, '[产品整合]', start, end, out, '开发中', i)
    # out, i = get_now_week_todo_by_dept(prepare_develop_todos, '[产品整合]', start, end, out, '待开发', i)
    # out, i = get_now_week_todo_by_dept(analysing_todos, '[产品整合]', start, end, out, '需求分析中', i)
    # out, i = get_now_week_todo_by_dept(business_todos, '[产品整合]', start, end, out, '业务(商务)阶段', i)
    #
    # # 输出共享服务工作摘要
    # i = 1
    # out += '\n' + "### 共享服务相关" + '\n'
    # out, i = get_now_week_todo_by_dept(published_todos, '[共享服务]', start, end, out, '已上线', i)
    # out, i = get_now_week_todo_by_dept(prepare_publish_todos, '[共享服务]', start, end, out, '待上线', i)
    # out, i = get_now_week_todo_by_dept(testing_todos, '[共享服务]', start, end, out, '测试中', i)
    # out, i = get_now_week_todo_by_dept(developing_todos, '[共享服务]', start, end, out, '开发中', i)
    # out, i = get_now_week_todo_by_dept(prepare_develop_todos, '[共享服务]', start, end, out, '待开发', i)
    # out, i = get_now_week_todo_by_dept(analysing_todos, '[共享服务]', start, end, out, '需求分析中', i)
    # out, i = get_now_week_todo_by_dept(business_todos, '[共享服务]', start, end, out, '业务(商务)阶段', i)
    #
    # # 输出leaf系统工作摘要
    # i = 1
    # out += '\n' + "### leaf系统相关" + '\n'
    # out, i = get_now_week_todo_by_dept(published_todos, '[Leaf]', start, end, out, '已上线', i)
    # out, i = get_now_week_todo_by_dept(prepare_publish_todos, '[Leaf]', start, end, out, '待上线', i)
    # out, i = get_now_week_todo_by_dept(testing_todos, '[Leaf]', start, end, out, '测试中', i)
    # out, i = get_now_week_todo_by_dept(developing_todos, '[Leaf]', start, end, out, '开发中', i)
    # out, i = get_now_week_todo_by_dept(prepare_develop_todos, '[Leaf]', start, end, out, '待开发', i)
    # out, i = get_now_week_todo_by_dept(analysing_todos, '[Leaf]', start, end, out, '需求分析中', i)
    # out, i = get_now_week_todo_by_dept(business_todos, '[Leaf]', start, end, out, '业务(商务)阶段', i)
    #
    # # 输出BA工作摘要
    # i = 1
    # out += '\n' + "### BA相关" + '\n'
    # out, i = get_now_week_todo_by_dept(prepare_develop_todos, '[BA]', start, end, out, '待开发', i)
    # out, i = get_now_week_todo_by_dept(analysing_todos, '[BA]', start, end, out, '需求分析中', i)
    # out, i = get_now_week_todo_by_dept(business_todos, '[BA]', start, end, out, '业务(商务)阶段', i)
    #
    # # 输出运维工作摘要
    # i = 1
    # out += '\n' + "### 运维相关" + '\n'
    # out, i = get_now_week_todo_by_dept(maintenance_todos, '[运维]', start, end, out, '工作中', i)
    #
    # print(out)
    # out_title = file_title % (year_now, int(week_now))
    # write_md_file(out_title, out)
    # pathAll = os.environ
    # pathAll['PATH'] += ":" + '/usr/local/texlive/2017basic/bin/x86_64-darwin'
    # os.environ["PATH"] = pathAll['PATH']
    # # print "设置之后的环境变量:", os.environ["PATH"]
    # os.system("pandoc " + out_title + ".md --pdf-engine=xelatex -o " + out_title + ".pdf -V CJKmainfont='SimHei'")


start_d = datetime.datetime(2018, 9, 10, 0, 0, 0)
end_d = datetime.datetime(2018, 9, 15, 0, 0, 0)

# my_dept(start_d, end_d)
# pmo_out(start_d, end_d)
# get_tower_todo_list(PMO_PROJECT_ID)  # 获取项目下的todolist列表

def test_pmo_out():
    pmo_out(start_d, end_d)

