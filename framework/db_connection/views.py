# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from common.mymako import render_json, render_mako_context
import function
import json


def data_base(request):
    """

    :param request:
    :return:
    """
    return render_mako_context(request, './db_connection/database.html')


# 菜单管理
def menu_manage(request):
    """

    :param request:
    :return:
    """
    return render_mako_context(request, './db_connection/muenu_manage.html')


def selecthor(request):
    """
    模糊查询
    :param request:
    :return:
    """
    res = function.selecthor(request)
    return render_json(res)


def selecthor2(request):
    """
    模糊查询2
    :param request:
    :return:
    """
    res = function.selecthor2(request)
    return render_json(res)


def save_conn(request):
    """
    保存
    :param request:
    :return:
    """
    re = function.saveconn_all(request)
    return render_json(re)


def edit_conn(request):
    """
    修改
    :param request:
    :return:
    """
    re = function.editconn(request)
    return render_json(re)


def test_conn(request):
    """
    测试
    :param request:
    :return:
    """
    r = function.testConn(request)
    return render_json(r)


def delete_conn(request, id):
    """
    删除
    :param request:
    :param id:
    :return:
    """
    function.delete_conn(request, id)
    return render_json(0)


def get_all_db_connection(request):
    """
    获取所有的数据库连接
    :param request:
    :return: json结果集
    """
    res = function.get_all_db_connection(request)
    return render_json(res)


def get_user_menu(request):
    """
    获取所有菜单
    :param request:
    :return:
    """
    res = function.get_user_muenu(request)
    return render_json(res)


def add_menu(request):
    """
    新增菜单
    :param request:
    :return:
    """
    res = function.addmuenus(request)
    return render_json(res)


def edit_menu(request):
    """
    修改菜单
    :param request:
    :return:
    """
    res = function.edit_muenu(request)
    return render_json(res)


def delete_menu(request, id):
    """
    删除菜单
    :param request:
    :param id:
    :return:
    """
    res = function.delete_muenu(request, id)
    return render_json(res)


def get_conname(request):
    """
    获取名称
    :param request:
    :return:
    """
    res = function.get_conname(request)
    return render_json(res)


def get_roleAmuenus(request):
    """
    获取所有角色对应菜单
    :param request:
    :return:
    """
    res = function.get_roleAmuenus(request)
    return render_json(res)


def checked_menu(request):
    """
    获取勾选ID
    :param request:
    :return:
    """
    res = function.checked_menu(request)
    return render_json(res)


def save_menu(request):
    """
    保存勾选ID
    :param request:
    :return:
    """
    res = function.savemnus(request)
    return render_json(res)

def get_all_mImgs(request):
    '''
    获取所有的图标代码
    :return:
    '''
    res=function.get_all_mImgs()
    return render_json(res)

def verify_name_only(request):
    '''
    验证名字的唯一性
    :param request:
    :return:
    '''
    body=json.loads(request.body)
    name=body['name'];id=body['id']
    res=function.verify_name_only(name,id)
    return render_json(res)