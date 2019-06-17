# -*- coding: utf-8 -*-
from django.forms import model_to_dict

from blueking.component.shortcuts import get_client_by_request
from common.log import logger
import base64
from account.models import *
from blueking.component.shortcuts import *
from gather_data.function import gather_data
from datetime import datetime
import time
import json
from django.core.paginator import Paginator
from monitor_item.models import Job
from gather_data.function import gather_data_migrate,gather_data, get_db
from gather_data import models as mo
from notification.function import rule_check
from market_day import celery_opt as co
from market_day.models import HeaderData as hd
from djcelery import models as celery_models
from models import *
import requests
from settings import BK_PAAS_HOST
from gather_data.models import TDGatherData

def error_result(e):
    """
    失败统一JSON
    :param e:   异常
    :return:    json数据
    """
    result = {
        "result": False,
        "message": u"失败 %s" % e,
        "code": 1,
        "results": None
    }
    return result


def success_result(results):
    """
    成功统一JSON
    :param results:
    :return:
    """
    result = {
        "result": True,
        "message": u'成功',
        "code": 0,
        "results": results,
    }
    return result


def page_paging(abj, limit, page):
    """
    :param abj: 对象
    :param limit: 个数
    :param page: 页数
    :return: 当前页数据，总页数
    """
    p = Paginator(abj, limit)  # 分页
    page_count = p.page_range[-1]  # 总页数
    page_data = p.page(page)  # 当前页数据
    return page_data, page_count


def common_obt_dic(page_data, page_count):
    """
    将分页model结果转为字典
    :param page_data:
    :param page_count:
    :return: 对应值list
    """
    obj_list = []
    for i in page_data:
        obj_dic = model_to_dict(i)
        obj_dic['page_count'] = page_count
        obj_list.append(obj_dic)
    return obj_list


def obt_dic(page_data, page_count):
    """
    监控项取值
    :param page_data:
    :param page_count:
    :return: 对应值list
    """
    obj_list = []
    # 数据库的连接配置

    db = get_db()
    cursor = db.cursor()
    #  id, scene_name, scene_startTime, scene_endTime,
    sql = "SELECT item_id,data_value from td_gather_data";
    cursor.execute(sql);
    gather_data = cursor.fetchall();
    gather_data_list = list(gather_data)
    cursor.close();
    #temp_list = [];#八字点存在
    dict = {};#存储查询拿到的值，用字典形式
    for item in gather_data_list:
        dict[item.__getitem__(0)] = item.__getitem__(1)
    for i in page_data:
        """
        # 这里不需要转换为中文，直接在前台页面上处理
        if i.monitor_type == 1:
            i.monitor_type = u'基本监控项'
        elif i.monitor_type == 2:
            i.monitor_type = u'图表监控项'
        elif i.monitor_type == 3:
            i.monitor_type = u'作业监控项'
        elif i.monitor_type == 4:
            i.monitor_type = u'流程监控项'
        """
        obj_dic = model_to_dict(i)
        obj_dic['page_count'] = page_count
        obj_dic['edit_time'] = str(i.edit_time)
        obj_dic['create_time'] = str(i.create_time)
        obj_dic['start_time'] = str(i.start_time)
        obj_dic['end_time'] = str(i.end_time)
        obj_dic['status'] = str(i.status)
        # 以下两个参数很重要，新增场景中必须用到
        obj_dic['item_id'] = str(i.id)
        #gather_data = TDGatherData.objects.filter(item_id=i.id)
        if dict.get(str(i.id)) ==None:
            obj_dic['data_value'] = None;
        else:
            obj_dic['data_value'] = dict[str(i.id)];
        # for gather_data_obj in gather_data:
        #     obj_dic['data_value'] = gather_data_obj.data_value
        obj_list.append(obj_dic)
    return obj_list


def interface_param(request):
    """
    返回client对象
    :param request:
    :return:
    """
    client = get_client_by_request(request)  # 获取code、secret参数
    client.set_bk_api_ver('v2')  # 以v2版本调用接口
    return client


def user_interface_param():
    """
    返回client对象
    :param :
    :return:
    """

    user_account = BkUser.objects.filter(username='admin').get()
    client = get_client_by_user(user_account)
    client.set_bk_api_ver('v2')  # 以v2版本调用接口
    return client


# 采集测试
def job_interface(res):
    try:
        params = res['params']  # ip
        gather_params = res['gather_params']  # 脚本参数
        bk_job_id = res['job_id'][0]['id']
        script_param = base64.b64encode(gather_params)
        # 根据id为1的用户获取客户端操作快速执行脚本
        client = user_interface_param()
        select_job_params = {
            'bk_biz_id': 2,
            'bk_job_id': bk_job_id,
        }
        # 查询作业模板详情接口
        select_job = client.job.get_job_detail(select_job_params)
        if select_job.get('result'):
            select_job_list = select_job.get('data')
        else:
            select_job_list = []
            logger.error(u"请求作业模板失败：%s" % select_job.get('message'))
        # 获取作业步骤ID
        step_id = select_job_list['steps'][0]['step_id']
        cloud_params = {
            'bk_biz_id': 2,
            'ip': {
                'data': [params, ],
                'exact': 1
            },
            "condition": [
                {
                    "bk_obj_id": "host",
                    "fields": [],
                    "condition": [
                        {
                            "field": "bk_host_innerip",
                            "operator": "$eq",
                            "value": params
                        }
                    ]
                }]
        }
        # 根据条件查询主机接口
        cloud_select = client.cc.search_host(cloud_params)
        if cloud_select.get('result'):
            cloud_id = cloud_select['data']['info'][0]['host']['bk_cloud_id'][0]['id']
        else:
            cloud_id = -1
            logger.error(u"请求主机信息失败：%s" % cloud_select.get('message'))
        job_params = {
            'bk_biz_id': 2,
            'bk_job_id': bk_job_id,
            'steps': [{
                'step_id': step_id,
                'script_param': script_param,
                "ip_list": [{
                    "bk_cloud_id": cloud_id,
                    "ip": params
                }, ]
            }, ],
        }
        # 启动作业接口
        job = client.job.execute_job(job_params)
        if job.get('result'):
            job_list = job.get('data')
            job_instance_id = job_list['job_instance_id']
        else:
            job_list = []
            job_instance_id = 0
            logger.error(u"请求作业模板失败：%s" % job.get('message'))
        log_params = {
            "bk_biz_id": "2",
            "job_instance_id": job_instance_id
        }
        # 根据实列ID查询日志接口
        log = client.job.get_job_instance_log(log_params)
        while 'True' != str(log['data'][0]['is_finished']):
            time.sleep(3)
            log = client.job.get_job_instance_log(log_params)
        # 获取作业执行日志
        json_data = log['data'][0]['step_results'][0]['ip_logs'][0]['log_content']
        # 状态为3则执行成功其余情况全部为失败
        if log['data'][0]['status'] == 3:
            status = 1
        else:
            status = -2
        res1 = success_result(job_list)
    except Exception as e:
        res1 = error_result(e)
        status = -1
    try:
        name_status = job['data']['job_instance_name']
        info = {
            'id': res['id'],  # 关联id
            'data_key': name_status,  # 状态key
            'gather_params': 'space_interface',  # 类型
            'data_value': status,  # 状态value
            'gather_error_log': {  # 采集数据
                'data_key': json_data
            },
            'instance_id': job_list['job_instance_id']  # 实列id
        }
        gather_data(**info)
        if res['id'] == 0:
            Job(instance_id=job_instance_id, status=status, test_flag=0, job_log=info['gather_error_log'],
                job_id=bk_job_id).save()
        else:
            Job(instance_id=job_instance_id, status=status, test_flag=1, job_log=info['gather_error_log'],
                job_id=bk_job_id).save()
    except Exception as e:
        res1 = error_result(e)
    return res1


# 流程的数据采集方法，采集测试和celery调度公用的方法
def flow_gather_task(**info):
    task_id = info['task_id']
    item_id = info['item_id']
    mess = hd.objects.get(id=1).header
    headers = json.loads(mess.decode('utf-8').replace("'", "\""))
    node_times = info['node_times']
    user_account = BkUser.objects.filter(id=1).get()
    client = get_client_by_user(user_account)
    client.set_bk_api_ver('v2')
    param = {
        'bk_biz_id': '2',
        'task_id': task_id
    }
    # 先从v2中取出id和状态
    res_temp = client.sops.get_task_status(param)
    ids = res_temp['data']['children']
    v2_data = []
    state = res_temp['data']['state']
    for id in ids:
        temp = {}
        temp['id'] = id
        temp['status'] = res_temp['data']['children'][id]['state']
        v2_data.append(temp)
    a_url = BK_PAAS_HOST + "/o/bk_sops/api/v3/taskflow/{}/".format(task_id);
    req = requests.get(url=a_url, headers=headers,verify=False)
    req.encoding = req.apparent_encoding
    req.raise_for_status()
    # 再从v3中取出节点对应的名字和id
    res = json.loads(req.text)
    res1 = json.loads(res['pipeline_tree'])
    activities = res1['activities']
    req_data = []
    for key in activities:
        print activities[key]
        activities1 = {}
        activities1['id'] = str(activities[key]['id'])
        activities1['name'] = activities[key]['name']
        activities1['code'] = activities[key]['component']['code']
        req_data.append(activities1)
    data = []
    # 最后根据v2，v3的结果中的id匹配得到最后的名字对应状态结果集
    for req in req_data:
        for v2 in v2_data:
            if req['id'] == v2['id']:
                temp = {}
                temp['name'] = req['name']
                temp['status'] = v2['status']
                temp['code'] = req['code']
                data.append(temp)
    task_name = info['task_name']
    gather_data_migrate(item_id=item_id)
    if state == 'FAILED':
        # 判断是否是采集测试，采集测试给定的测试id为100000
        if item_id == 1000000:
            co.delete_task(task_name)
        for d in data:
            if d['status'] == u'FAILED':
                msg = d['name'] + u'节点执行出错，请检查这个节点'
    elif state == 'RUNNING':
        msg = u'该任务正在执行中'
    elif state == 'SUSPENDED':
        msg = u'该任务被暂停'
    elif state == 'REVOKED':
        msg = u'该任务已被终止'
        if item_id == 1000000:
            co.delete_task(task_name)
    elif state == 'FINISHED':
        msg = u'该任务成功执行'
        if item_id == 1000000:
            co.delete_task(task_name)
    for d in data:
        s = d['status']
        if s == 'FAILED':
            status = 0
        elif s == 'RUNNING':
            status = 1
            # 节点只有是运行状态下，才有可能超时，判断节点是否超时,状态5代表超时
            for node in node_times:
                if d['name'] == node['node_name']:
                    strnow = datetime.strftime(datetime.now(), '%H:%M')
                    if strnow > node['endtime']:
                        status = 5
            if d['code'] == 'pause_node':
                status = 2
        elif s == 'SUSPENDED':
            status = 2
        elif s == 'REVOKED':
            status = 3
        elif s == 'FINISHED':
            status = 4
        mo.TDGatherData.objects.create(item_id=item_id, instance_id=task_id, data_key=d['name'], data_value=status,
                                       gather_error_log=msg)
    if item_id != 0:
        rule_check(item_id)


# 流程采集测试开始流程的方法
def start_flow_task(**info):
    # 得到client对象，方便调用接口
    user_account = BkUser.objects.filter(id=1).get()
    client = get_client_by_user(user_account)
    client.set_bk_api_ver('v2')
    template_id = info['template_list']['id']
    constants_temp = info['constants']
    constants = {}
    for temp in constants_temp:
        constants[temp['key']] = temp['value']
    strnow = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    name = info['template_list']['name'] + strnow
    param = {
        "bk_biz_id": "2",
        "template_id": template_id,
        'name': name,
        'constants': constants
    }
    res = client.sops.create_task(param)
    # 调用接口创建任务并得到任务的id
    task_id = res['data']['task_id']
    # 调用接口启动任务，开始执行任务
    param = {
        "bk_biz_id": "2",
        'task_id': task_id
    }
    res = client.sops.start_task(param)
    flag = res['result']
    status = 0
    # 如果启动任务成功创建一个定时查看节点状态的任务
    if flag:
        node_times = info['node_times']
        starthour = str(node_times[-1]['starttime']).split(':')[0]
        endhour = str(node_times[0]['endtime'])[:2].split(':')[0]
        period = info['period']
        item_id = 1000000
        args = {
            'item_id': item_id,
            'task_id': task_id,  # 启动流程的任务id
            'node_times': node_times,
            'period': period,
            'task_name': info['template_list']['name'] + '_check_status_test'
        }
        ctime = {
            'every': period,
            'period': 'seconds'
        }
        co.create_task_interval(name=info['template_list']['name'] + '_check_status_test',
                                task='market_day.tasks.gather_data_task_thrid_test', interval_time=ctime,
                                task_args=args, desc=name)
        status = 1
    Flow(instance_id=task_id, status=flag, test_flag=1, flow_id=item_id).save()
    return task_id


# 让流程继续执行，调用v2接口
def resume_flow(item_id, name):
    task_id = Flow.objects.filter(flow_id=item_id).last().instance_id
    task_id = 188
    d = {
        "action": "resume",
        "bk_biz_id": "2",
        "task_id": task_id
    }
    user_account = BkUser.objects.filter(id=1).get()
    client = get_client_by_user(user_account)
    client.set_bk_api_ver('v2')
    res = client.sops.operate_task(d)
    # v2接口继续整个流程
    mess = hd.objects.get(id=1).header
    headers = json.loads(mess.decode('utf-8').replace("'", "\""))
    a_url = BK_PAAS_HOST + "/o/bk_sops/api/v3/taskflow/{}/".format(task_id);
    req = requests.get(url=a_url, headers=headers,verify=False)
    req.encoding = req.apparent_encoding
    req.raise_for_status()
    res = json.loads(req.text)
    res1 = json.loads(res['pipeline_tree'])
    activities = res1['activities']
    node_id = ''
    for key in activities:
        if name == activities[key]['name']:
            node_id = str(activities[key]['id'])
    url = BK_PAAS_HOST + "/o/bk_sops/taskflow/api/nodes/action/callback/2/"
    payload = "instance_id=" + str(
        task_id) + "&node_id=" + node_id + "&data=%7B%22callback%22%3A%22resume%22%7D&undefined="
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Connection': "keep-alive",
        'Content-Length': "97",
        'Cookie': headers['Cookie'],
        'Host': "paas.bk.com",
        'Origin': BK_PAAS_HOST,
        'Referer': BK_PAAS_HOST + "/o/bk_sops/taskflow/execute/2/?instance_id=" + str(task_id),
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        'X-CSRFToken': "TRcGm7VPnTWNMYgC9r34TsvBmIncTRls",
        'X-Requested-With': "XMLHttpRequest",
        'cache-control': "no-cache",
        'Postman-Token': "d4f27086-758e-40aa-813f-067b45422393"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return 'success'
