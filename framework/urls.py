# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.

urls config
"""
from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from apscheduler.scheduler import Scheduler
from datetime import datetime
from monitor_item.models import Monitor
from django.forms import model_to_dict
from market_day.celery_opt import enable_task,disable_task
import time
# admin.autodiscover()

# 公共URL配置
urlpatterns = patterns(
    '',
    # Django后台数据库管理
    url(r'^admin/', include(admin.site.urls)),
    # 用户登录鉴权--请勿修改
    url(r'^account/', include('account.urls')),
    # 应用功能开关控制--请勿修改
    url(r'^app_control/', include('app_control.urls')),

    # 在home_application(根应用)里开始开发你的应用的主要功能
    # url(r'^', include('home_application.urls')),

    # shell_app主页
    url(r'^', include('shell_app.urls')),
    # 监控项_APP_URL
    url(r'^monitor_item/', include('monitor_item.urls')),
    # 系统设置
    url(r'^system_config/', include('system_config.urls')),
    url(r'^monitor_scene/', include('monitor_scene.urls')),
    # 岗位管理
    url(r'^position/', include('position.urls')),
    url(r'market_day/', include('market_day.urls')),
    url(r'^db_connection/', include('db_connection.urls')),
    # 定制过程通知
    url(r'^custom_process/', include('custom_process.urls')),
    # 基本监控单元数据采集
    url(r'^gather_data/', include('gather_data.urls')),
    # 告警规则配置
    url(r'^notification/', include('notification.urls')),
    # 操作日志记录
    url(r'^logmanagement/', include('logmanagement.urls')),
    # 报表统计
    url(r'^history_chart/', include('history_chart.urls')),
    # 自定义查询
    url(r'^custom_query/', include('custom_query.urls')),
    url(r'^home_page/', include('home_page.urls')),
    # iqube接口
    url(r'^iqube_interface/', include('iqube_interface.urls')),
)
sched = Scheduler()  #实例化，固定格式
@sched.interval_schedule(seconds=60)  #装饰器，seconds=60意思为该函数为1分钟运行一次
def mytask():
    death_func()

sched.start ()  # 启动该脚本
def death_func():
    while True:
        task_obj = Monitor.objects.filter(status=1)
        for monitor_mod in task_obj:
            monitor = model_to_dict(monitor_mod)
            start_time = str(monitor['start_time'])
            end_time = str(monitor['end_time'])
            schename = monitor['id']
            strnow = datetime.strftime (datetime.now (), '%H:%M')
            starttime = start_time.split (':')[0] + ":" + start_time.split (':')[1]
            endtime = end_time.split (':')[0] + ":" + end_time.split (':')[1]
            print schename
            if starttime <= strnow <= endtime:

                print True
                enable_task(schename)
            else:
                print False
                disable_task(schename)
        time.sleep(10)

handler404 = 'error_pages.views.error_404'
handler500 = 'error_pages.views.error_500'
handler403 = 'error_pages.views.error_403'
handler401 = 'error_pages.views.error_401'
