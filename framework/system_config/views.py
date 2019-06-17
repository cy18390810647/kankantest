# encoding:utf-8
from common.mymako import render_mako_context
from common.mymako import render_json
from shell_app import tools
import json
import crawl_template
import function
import sys
from logmanagement.function import add_log, make_log_info, get_active_user
import datetime


# Create your views here.
def crawl_config_html(request):
    """
    网页抓取配置页面
    :param request:
    :return:
    """
    return render_mako_context(request, './system_config/crawl_config.html')


def scene_type_html(request):
    """
    场景分组配置
    :param request:
    :return:
    """
    return render_mako_context(request, './system_config/scene_type.html')


def crawl_content_html(request):
    """
    爬虫内容
    :param request:
    :return:
    """
    return render_mako_context(request, './system_config/crawl_content.html')


def manage_crawl(request):
    """
    爬虫信息新增和修改
    :param request:
    :return:
    """
    res = function.crawl_manage(request)
    return render_json(res)


def delete_crawl(request):
    """
    根据ID删除爬虫配置信息
    :param request:
    :return:
    """
    res = function.delete_crawl_config_id(request)
    return render_json(res)


def get_crawls(request):
    """
    获取爬虫配置信息
    :param request:
    :return:
    """
    res = function.get_crawls_config(request)
    return render_json(res)


def get_crawl_by_name(request):
    """
    条件查询
    :param request:
    :return:
    """
    res = function.get_crawl_by_name(request)
    return render_json(res)


def crawl(request):
    """
    爬虫测试
    :param request:
    :return:
    """
    # 上交所
    # url = 'http://www.sse.com.cn/services/tradingservice/tradingtech/newnotice/'
    # total_xpath = '//div[@class="sse_list_1 js_listPage"]//dl//dd'
    # title_xpath = 'a/text()'
    # time_xpath = 'span/text()'
    # url_xpath = 'a/@href'

    # 深交所
    url = 'http://www.szse.cn/aboutus/trends/news/index.html'
    total_xpath = '//div[@class="article-list"]//div[@class="g-content-list"]//ul//li//div[@class="title"]'
    title_xpath = 'a/@title'
    time_xpath = 'span/text()'  # yes
    url_xpath = 'a/@href'

    # china clear
    # url = 'http://www.chinaclear.cn/zdjs/gszb/center_clist.shtml'
    # total_xpath = '//div[@class="pageTabContent"]//ul//li'
    # title_xpath = 'a/@title'
    # # time_xpath = ''  # yes
    # time_xpath = 'span/text()'  # yes
    # # url_xpath = 'a/@href'
    # url_xpath = ''
    res = crawl_template.crawl_temp(url, total_xpath, title_xpath, time_xpath, url_xpath)
    return render_json(res)


def start_crawl(request):
    """
    开始爬虫
    :param request:
    :return:
    """
    res = function.start_crawl(request)
    return render_json(res)


def crawl_test(request):
    """
    用户爬虫测试
    :param request:
    :return:
    """
    res = function.crawl_test(request)
    return render_json(res)


def json_test(request):
    """
    josn测试
    :param request:
    :return:
    """
    res = function.get_email_address_list(request)
    return render_json(res)


def mail_send(request):
    """
    邮件发送
    :param request:
    :return:
    """
    res = function.send(request)
    return render_json(res)


def get_scene_type(request):
    """
    获取场景分组信息
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    page = request_body['page']
    limit = request_body['limit']
    if request_body['query_name'] is None or request_body['query_name'] == '':
        res = function.get_scene_type('', page, limit)
        return render_json(res)
    else:
        query_name = json.loads(request.body)['query_name']
        print query_name
        res = function.get_scene_type(query_name, page, limit)
        return render_json(res)


def add_scene_type(request):
    """
    新增场景类型
    :param request:
    :return:
    """
    try:
        request_body = json.loads(request.body)
        start_time = datetime.datetime.strptime(request_body['start_time'], "%H:%M:%S")
        stop_time = datetime.datetime.strptime(request_body['stop_time'], "%H:%M:%S")
        scene_type_name = request_body['name']
        client = tools.interface_param(request)
        user = client.bk_login.get_user({})
        res = function.add_scene_type(user['data']['bk_username'], scene_type_name, start_time, stop_time)
        info = make_log_info(u'增加场景类型', u'业务日志', u'SceneType', sys._getframe().f_code.co_name,
                             get_active_user(request)['data']['bk_username'], '成功', '无')
    except Exception as e:
        info = make_log_info(u'增加场景类型', u'业务日志', u'SceneType', sys._getframe().f_code.co_name,
                             get_active_user(request)['data']['bk_username'], '失败', repr(e))
        res = {}
    # add_log(info)
    return render_json(res)


def edit_scene_type_by_uuid(request):
    """
    修改场景分组
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    print request_body['start_time']
    print request_body['stop_time']
    start_time = datetime.datetime.strptime(request_body['start_time'], "%H:%M:%S")
    stop_time = datetime.datetime.strptime(request_body['stop_time'], "%H:%M:%S")
    scene_type_name = request_body['name']
    uuid = request_body['uuid']
    client = tools.interface_param(request)
    user = client.bk_login.get_user({})
    res = function.edit_scene_type_by_uuid(uuid, user['data']['bk_username'], scene_type_name, start_time, stop_time)
    return render_json(res)
    # try:
    #     request_body = json.loads(request.body)
    #     request_body['start_time']
    #     start_time = datetime.datetime.strptime(request_body['start_time'], "%H:%M")
    #     stop_time = datetime.datetime.strptime(request_body['stop_time'], "%H:%M:%s")
    #     scene_type_name = request_body['name']
    #     uuid = request_body['uuid']
    #     client = tools.interface_param(request)
    #     user = client.bk_login.get_user({})
    #     res = function.edit_scene_type_by_uuid(uuid, user['data']['bk_username'], scene_type_name, start_time, stop_time)
    #     info = make_log_info(u'编辑场景类型', u'业务日志', u'SceneType', sys._getframe().f_code.co_name,
    #                          get_active_user(request)['data']['bk_username'], '成功', '无')
    # except Exception as e:
    #     info = make_log_info(u'编辑场景类型', u'业务日志', u'SceneType', sys._getframe().f_code.co_name,
    #                          get_active_user(request)['data']['bk_username'], '失败', repr(e))
    #     # add_log(info)
    #     res = {}
    # return render_json(res)


def delete_scene_by_uuid(request):
    """
    删除场景分组
    :param request:
    :return:
    """
    try:
        print request.body
        print request
        request_body = json.loads(request.body)
        uuid = request_body['uuid']
        res = function.delete_scene_by_uuid(uuid)
        info = make_log_info(u'删除场景分组', u'业务日志', u'SceneType', sys._getframe().f_code.co_name,
                             get_active_user(request)['data']['bk_username'], '成功', '无')
    except Exception as e:
        info = make_log_info(u'删除场景分组', u'业务日志', u'SceneType', sys._getframe().f_code.co_name,
                             get_active_user(request)['data']['bk_username'], '失败', repr(e))
        add_log(info)
    return render_json(res)


def get_crawl_content(request):
    """
    获取爬虫内容
    :param request:
    :return:
    """
    request_body = json.loads(request.body)
    title_content = request_body['title_content']
    crawl_name = request_body['crawl_name']
    page = request_body['page']
    limit = request_body['limit']
    print request_body
    res = function.get_crawl_content(title_content, crawl_name, page, limit)
    return render_json(res)


def start_crawl_test(request):

    res = function.start_crawl(request)
    return render_json(res)


def test(request):
    """

    :param request:
    :return:
    """
    res = function.test(request)
    return render_json(res)

#jlq-2019-05-27-add-看板标题修改
def update_board(request,name):
    """
    根据ID删除爬虫配置信息
    :param request:
    :return:
    """
    res = function.update_board(request,name)
    return render_json(res)

def selectBoard(request):
    """
    获取看板标题
    :param request:
    :return: json结果集
    """
    res = function.selectBoard(request)
    return render_json(res)