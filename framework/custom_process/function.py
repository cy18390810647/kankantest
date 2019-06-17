# -*- coding: utf-8 -*-

from position.models import pos_info
from models import TbCustProcess
from models import TdCustProcessLog
from position.models import user_info,user_group
from django.forms.models import model_to_dict
import urllib
import urllib2
import json
import datetime
from django.core.paginator import *


def select_all_nodes(params):
    """
    获取定制流程节点
    :return: List
    """
    node_info = TbCustProcess.objects.order_by('seq').all()
    node_lists = list()
    node_list = None
    node_dict = dict()
    count = 0
    for node in node_info:
        dic1 = model_to_dict(node)
        # 获取该节点对应的节点状态
        temp = TdCustProcessLog.objects.filter(node_id=node.id).get()
        # 临时保存节点的执行时间
        do_time_ori = temp.do_time
        # 节点执行时间置空，防止datetime类型在model_to_dict时转换报错
        temp.do_time = None
        dic2 = model_to_dict(temp)
        # 由于model_to_dict方法不支持datetime类型的数据直接转换字典，手动转换
        if do_time_ori is None:
            dic2['do_time'] = ''
        else:
            dic2['do_time'] = do_time_ori.strftime('%Y-%m-%d %H:%M:%S')
        # 将节点状态放置到节点的status字段中
        dic1['status'] = dic2
        # 每满limit数量节点重新放入一个新的list中
        if count % int(params['limit']) == 0:
            if None is not node_list:
                node_lists.append(node_list)
            node_list = list()
        # 将当前遍历的节点添加到list中
        node_list.append(dic1)
        count += 1
    # 解决未满limit个数的list未被添加的问题
    if count % int(params['limit']) != 0 or len(node_list) != 0:
        node_lists.append(node_list)
    # 节点list
    node_dict['nodes'] = node_lists
    # 节点总个数
    node_dict['count'] = count
    return node_dict


def select_nodes_pagination(node_info):
    """
    # 分页获取定制过程节点
    :param node_info: 包含page和limit
    :return:
    """
    result_dict = dict()
    list_set = list()
    # 获取前台传递的参数：需要第几页的数据
    page = node_info['page']
    # 获取前台传递的参数：每页有多少条数据
    limit = node_info['limit']
    # 获取前台传递参数：检索条件
    condition = node_info['condition']
    # 获取当前所有节点
    if None is not condition and '' != condition:
        nodes_list = TbCustProcess.objects.all().filter(node_name__contains=condition)
    else:
        nodes_list = TbCustProcess.objects.all()
    # 对所有节点进行分页处理
    paginator = Paginator(nodes_list, limit)
    # 获取指定页的数据
    try:
        selected_set = paginator.page(page)
    except PageNotAnInteger:
        selected_set = paginator.page(1)
    except EmptyPage:
        selected_set = paginator.page(paginator.num_pages)
    # 将当前页所有数据转换为字典对象，并添加到list中，统一传递到前端
    for selected_data in selected_set:
        temp = model_to_dict(selected_data)
        list_set.append(temp)
    # 当前页的所有数据
    result_dict['items'] = list_set
    # 当前的总页数
    result_dict['pages'] = paginator.num_pages
    return result_dict


def add_node(node):
    """
    添加或修改一个定制过程节点
    :param node:
    :return:
    """
    status_dic = dict()
    # 添加节点并获取当前操作的节点
    if 'add' == node['method']:
        print 'ADD'
        last_node = TbCustProcess.objects.create(**node['node'])
        TdCustProcessLog(node_id=last_node.id).save()
    elif 'edit' == node['method']:
        print 'EDIT'
        TbCustProcess(**node['node']).save()
    # 获取当前所有节点的数量
    items_count = TbCustProcess.objects.count()
    # 默认每页5条记录，获取总页数
    pages = items_count // 5
    if 0 != items_count % 5:
        pages = pages + 1
    status_dic['message'] = 'ok'
    status_dic['total_pages'] = pages
    return status_dic


def select_all_bkusers():
    """
    获取所有已设置通知方式的蓝鲸用户信息
    :return:
    """
    users_list = list()
    # 获取用户通知方式不为空的记录
    # bk_users = user_info.objects.all().filter(notice_style__isnull=False)
    # for bk_user in bk_users:
    # 通知方式必须为微信、短信、邮件的一种
    #    if bk_user.notice_style not in ('wechat','sms','email'):
    #        continue
    #   user_dict = model_to_dict(bk_user)
    #    users_list.append(user_dict)
    # return users_list
    bk_pos = user_group.objects.all()
    for bk_user in bk_pos:
        user_dict = model_to_dict(bk_user)
        users_list.append(user_dict)
    return users_list


def update_node_status(node):
    """
    修改指定节点id的节点信息
    :param node:
    :return:
    """
    selected_status = TdCustProcessLog.objects.get(node_id=node['node_id'])
    selected_status.is_done = node['is_done']
    selected_status.do_time = node['do_time']
    selected_status.do_person = node['do_person']
    selected_status.save()
    return "ok"


def change_status_flag(node):
    """
    修改指定节点id的节点状态
    :param node:
    :return:
    """
    selected_status = TdCustProcessLog.objects.get(node_id=node['node_id'])
    selected_status.is_done = node['is_done']
    selected_status.save()
    return "ok"


def del_node(node_id):
    """
    删除指定节点id的节点
    :param node_id:
    :return:
    """
    TbCustProcess.objects.filter(id=node_id['id']).delete()
    return "ok"


def select_node(node_id):
    """
    获取指定节点id的节点
    :param node_id:
    :return:
    """
    node = TbCustProcess.objects.filter(id=node_id['id']).get()
    node_list = []
    dic = model_to_dict(node)
    node_list.append(dic)
    return node_list


def truncate_node():
    """
    删除所有已存在的过程通知节点
    :return:
    """
    TbCustProcess.objects.all().delete()
    return "ok"


def clear_execute_status():
    """
    清除所有过程通知节点的执行状态信息
    :return:
    """
    nodes_status = TdCustProcessLog.objects.all()
    for status in nodes_status:
        status.is_done = 'n'
        status.do_time = None
        status.do_person = None
        status.save()
    return "ok"


# 流程节点执行完毕发送通知方法
# def send_notification(notification):
#     """
#     发送通知
#     :param notification:
#     :return:
#     """
#
#     # 是否存在发送错误的标志位
#     send_flag = True
#     # 保存发送完成的信息，以及发送是否存在错误，返回前端
#     status = dict()
#     # 获取接收者账号名称信息，以list保存
#     if -1 != notification['receivers'].find(','):
#         receivers = notification['receivers'].split(',')
#     else:
#         receivers = list()
#         receivers.append(notification['receivers'])
#     # 保存发送完成的信息
#     infos = list()
#     # 获取的微信token
#     access_token = None
#     # 短信发送列表
#     sms_send_list = None
#     # 邮件发送列表
#     mail_send_list = None
#     # 遍历前端传递的接收者列表
#     for receiver in receivers:
#         # 获取当前账户名称的用户信息
#         rec_info = user_info.objects.filter(user_name=receiver).get()
#         # 当用户的通知方式为微信通知方式的情况下--由于微信端限制，非服务号无法使用群发，因此只能在遍历用户时发送，不能统一发送
#         if 'wechat' == rec_info.notice_style:
#             # 如果当前为第一次获取token信息
#             if None is access_token:
#                 access_token = wechat_access_token()
#                 # token获取异常，检查APPID和secret是否正确
#             if None is access_token:
#                 print 'Wechat access token get fail'
#                 send_flag = False
#                 infos.append(u'微信发送失败!Token获取异常!')
#                 break
#             # 根据获取的当前用户的openid和获取的token发送指定内容的推送消息给用户
#             if None is rec_info.open_id or '' == rec_info.open_id.strip():
#                 infos.append(u'%s：微信发送失败!用户openid未设置' % receiver)
#                 send_flag = False
#                 continue
#             res = wechat_send_msg(access_token, rec_info.open_id, notification['content'])
#             # 函数返回为None说明发送正常，否则将返回错误信息
#             if None is not res:
#                 infos.append(u'%s: 微信通知发送失败! %s' % (receiver, res))
#                 # send_flag标志位置False告诉前端有发送失败的任务，前端将会以error框展示
#                 send_flag = False
#         # 当用户的通知方式为短信通知方式的情况下
#         elif 'sms' == rec_info.notice_style:
#             # 如果当前是第一次添加短信接收者信息，新建一个list用于保存
#             if None is sms_send_list:
#                 sms_send_list = list()
#             sms_send_list.append(receiver)
#         # 当用户的通知方式为邮件通知方式的情况下
#         elif 'email' == rec_info.notice_style:
#             # 如果当前是第一次添加邮箱接收者信息，新建一个list用于保存
#             if None is mail_send_list:
#                 mail_send_list = list()
#             mail_send_list.append(receiver)
#     # 短信发送列表如果不为空，则发送短信给列表中的接收者
#     if None is not sms_send_list:
#         sms_send_msg(notification['content'], sms_send_list)
#     # 邮件发送列表如果不为空，则发送邮件给列表中的接收者
#     if None is not mail_send_list:
#         mail_send_msg(u'过程通知信息', notification['content'], mail_send_list)
#     # 根据当前发送状态标志位，返回前端一个相应的发送状态，用于前端判断发送是否存在问题
#     if send_flag:
#         status['message'] = 'ok'
#         status['info'] = u'通知发送成功!'
#     else:
#         status['message'] = 'error'
#         status['info'] = infos
#     # 返回发送的状态信息给前端
#     return status

def send_notification(notification):
    """
    流程节点执行完毕发送通知方法（本方法中的接口需要在生产环境下才能调通，未经过测试，不保证完全可用）
    :param notification: 前端发送的通知信息集
    :return:
    """
    # 返回到前端的通知发送状态信息
    status = dict()
    wechat_infos = None
    sms_infos = None
    # 短信发送接收人列表
    sms_send_list = None
    # 微信发送接收人列表
    wechat_send_list = None
    # 以下为发送的通知信息字典，详细参考中畅的短信和微信接口示例代码
    send_info = dict()
    notification_data = dict()
    notification_data['approver'] = notification['approver']
    notification_data['changeTime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    notification_data['changeSystem'] = u'看板系统-定制流程'
    notification_data['alarmRuleName'] = u'节点已执行完毕'
    send_info['content'] = notification_data
    # 获取接收者账号名称信息，以list保存
    if -1 != notification['receivers'].find(','):
        receivers = notification['receivers'].split(',')
    else:
        receivers = list()
        receivers.append(notification['receivers'])
    # 遍历前端传递的接收者列表
    for receiver in receivers:
        # 获取当前账户名称的用户信息
        rec_info = user_info.objects.filter(user_name=receiver).get()
        # 当用户的通知方式为微信通知方式
        if 'wechat' == rec_info.notice_style:
            # 如果当前是第一次添加微信接收者信息，新建一个list用于保存
            if None is wechat_send_list:
                wechat_send_list = list()
                wechat_send_list.append(receiver)
        # 当用户的通知方式为短信通知方式的情况下
        elif 'sms' == rec_info.notice_style:
            # 如果当前是第一次添加短信接收者信息，新建一个list用于保存
            if None is sms_send_list:
                sms_send_list = list()
            sms_send_list.append(receiver)
    # 短信发送列表如果不为空，则发送短信给列表中的接收者
    if None is not wechat_send_list:
        wechat_infos = send_msg(wechat_send_list, send_info, 'wechat')
    # 邮件发送列表如果不为空，则发送邮件给列表中的接收者
    if None is not sms_send_list:
        sms_infos = send_msg(wechat_send_list, send_info, 'sms')
    # 根据当前发送状态标志位，返回前端一个相应的发送状态，用于前端判断发送是否存在问题
    if wechat_infos['send_flag'] and sms_infos['send_flag']:
        status['message'] = 'ok'
        status['info'] = u'所有通知发送成功!'
    else:
        status['message'] = 'error'
        if None is not sms_infos and None is not wechat_infos:
            status['info'] = wechat_infos['error_info'] + sms_infos['error_info']
        elif None is not sms_infos and None is wechat_infos:
            status['info'] = sms_infos['error_info']
        else:
            status['info'] = wechat_infos['error_info']
    # 返回发送的状态信息给前端
    return status


def send_msg(receivers, send_info, send_type):
    """
    调用发送通知的接口
    :param receivers: 通知接收人列表
    :param send_info: 发送的通知信息
    :param send_type: 发送的类型：sms or wechat
    :return:
    """
    # 发送类型为短信的情况
    if 'sms' == send_type:
        req_url = 'http://10.240.1.127:8008/sms'
    # 发送类型为微信的情况
    else:
        req_url = 'http://10.181.6.160:9091/send'
    # 包含发送通知结果的信息集
    infos = dict()
    # 是否存在发送失败的通知的标记
    send_flag = True
    # 错误信息
    error_info = list()
    try:
        # 遍历消息接收者集
        for receiver in receivers:
            # 消息接收者定义，详细参考中畅的短信和微信接口示例代码
            send_info['tos'] = receiver
            # 消息字典转JSON字符串发送
            json_str = json.dumps(send_info, ensure_ascii=False)
            # 字符串以UTF-8编码
            utf8_str = json_str.encode('utf-8')
            # 字符串URL编码
            # url_encoded_str = urllib.urlencode(utf8_str)
            # 发送POST请求到接口
            req = urllib2.Request(url=req_url, data=utf8_str)
            # 获取接口返回值
            res_data = urllib2.urlopen(req).read()
            print res_data
            # 接口返回数据包含success字符串说明本次通知发送成功
            if -1 == res_data.indexOf("success"):
                error_info.append(res_data)
                send_flag = False
    except Exception as e:
        error_info = e.__str__()
        send_flag = False
    finally:
        # 信息集包括是否有发送失败通知的标记位，及错误信息
        infos['send_flag'] = send_flag
        infos['error_info'] = error_info
        return infos
