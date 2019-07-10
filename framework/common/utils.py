# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.

开发框架公用方法
1. 页面输入内容转义（防止xss攻击）
from common.utils import html_escape, url_escape, texteditor_escape
2. 转义html内容
html_content = html_escape(input_content)
3. 转义url内容
url_content = url_escape(input_content)
4. 转义富文本内容
texteditor_content = texteditor_escape(input_content)
"""
from common.pxfilter import XssHtml
from common.log import logger
from db_connection.function import get_db
from monitor_item import tools


def html_escape(html, is_json=False):
    """
    Replace special characters "&", "<" and ">" to HTML-safe sequences.
    If the optional flag quote is true, the quotation mark character (")
    is also translated.
    rewrite the cgi method
    @param html: html代码
    @param is_json: 是否为json串（True/False） ，默认为False
    """
    # &转换
    if not is_json:
        html = html.replace("&", "&amp;")  # Must be done first!
    # <>转换
    html = html.replace("<", "&lt;")
    html = html.replace(">", "&gt;")
    # 单双引号转换
    if not is_json:
        html = html.replace(' ', "&nbsp;")
        html = html.replace('"', "&quot;")
        html = html.replace("'", "&#39;")
    return html


def url_escape(url):
    url = url.replace("<", "")
    url = url.replace(">", "")
    url = url.replace(' ', "")
    url = url.replace('"', "")
    url = url.replace("'", "")
    return url


def texteditor_escape(str_escape):
    """
    富文本处理
    @param str_escape: 要检测的字符串
    """
    try:
        parser = XssHtml()
        parser.feed(str_escape)
        parser.close()
        return parser.get_html()
    except Exception, e:
        logger.error(u"js脚本注入检测发生异常，错误信息：%s" % e)
        return str_escape


def get_current_time():
    """
    获取当前系统时间
    :return:
    """
    res = ""
    try:
        sql = "SELECT DATE_FORMAT(now(), '%H:%i:%S') AS cur_time;"
        db = get_db()
        cursor = db.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        db.close()
    except Exception as e:
        return tools.error_result(e)
    # scene_list = list(res1)
    return res


def get_previous_day_ts():
    """
        获取当前系统时间前一天的时间戳
        :return:
        """
    res = ""
    try:
        sql = "SELECT unix_timestamp(date_sub(now(), INTERVAL 1 DAY)) as timestamp;"
        db = get_db()
        cursor = db.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        db.close()
    except Exception as e:
        return tools.error_result(e)
    # scene_list = list(res1)
    return res
