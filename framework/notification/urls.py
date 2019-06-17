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
    'notification.views',
    (r'^index$', 'show_index'),                                          # 告警规则配置页面
    (r'^select_all_rules$', 'select_all_rules'),                         # 获取所有已配置的告警规则
    (r'^select_rule$', 'select_rule'),                                   # 根据id获取指定的告警规则
    (r'^del_rule$', 'del_rule'),                                         # 根据id删除指定的告警规则
    (r'^force_del_rule$', 'force_del_rule'),                             # 在有用户订阅该告警的情况下级联删除告警规则和订阅信息
    (r'^add_rule$', 'add_rule'),                                         # 添加告警规则
    (r'^select_rules_pagination$', 'select_rules_pagination'),          # 分页获取指定页的告警规则
    (r'^get_all_name$','get_all_name'),
)
