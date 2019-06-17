# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from django.conf.urls import patterns

urlpatterns = patterns(
    'monitor_item.views',
    (r'^$', 'index'),  # 首页--服务器选择页面
    (r'^show/$', 'unit_show'),
    (r'^show_message$', 'index'),
    (r'^select/$', 'select_unit'),
    (r'^edit/$', 'edit_unit'),
    (r'^delete/$', 'delete_unit'),
    (r'^add/$', 'add_unit'),
    (r'^basic_test/$', 'basic_test'),
    (r'^job_test/$', 'job_test'),
    (r'^chart_get_test/$', 'chart_get_test'),
    (r'^change_status/$', 'change_status'),  # 改变监控项的启用状态
    (r'^flow_change/$', 'flow_change'),
    (r'^node_name/$', 'node_name'),
    (r'^start_flow_task/$', 'start_flow_task'),
    (r'^node_state/$', 'node_state'),
    (r'^resume_flow/$', 'resume_flow'),
    (r'^node_state_by_item_id/$', 'node_state_by_item_id'),
    (r'^select_test/$', 'select_test'),
    (r'^select_monitor_item/$', 'select_monitor_item'),
    (r'^verify_name_only/$','verify_name_only'),
    (r'^showAPI/$', 'showAPI'),
)
