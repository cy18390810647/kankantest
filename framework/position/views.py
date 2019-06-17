# -*- coding: utf-8 -*-
import function
from common.mymako import render_json, render_mako_context
from django.conf import settings
from position.models import user_info
from django.forms import model_to_dict


# Create your views here.

def index(request):
    """

    :param request:
    :return:
    """
    return render_mako_context(request, './position/position.html')


def show(request):
    """

    :param request:
    :return:
    """
    res = function.show(request)
    return render_json(res)


def select_pos(request):
    """

    :param request:
    :return:
    """
    res = function.select_pos(request)
    return render_json(res)


def delete_pos(request):
    """

    :param request:
    :return:
    """
    res = function.delete_pos(request)
    return render_json(res)


def add_pos(request):
    """

    :param request:
    :return:
    """
    r = function.add_pos(request)
    return render_json(r)


def add_person(request):
    """

    :param request:
    :return:
    """
    function.add_person(request)
    return render_json(0)


def edit_pos(request):
    """

    :param request:
    :return:
    """
    r = function.edit_pos(request)
    return render_json(r)


def filter_user(request):
    """

    :param request:
    :return:
    """
    r = function.filter_user(request)
    return render_json(r)


def get_user_group(request):

    res = function.get_user_group(request)
    return render_json(res)


def add_group(request):

    res = function.add_group(request)
    return render_json(res)




def get_tree(request):
    r = function.get_tree(request)
    return render_json(r)


def synchronize(request):
    r = function.synchronize(request)
    return render_json(r)


def get_active_user(req):
    bk_username = req.user.username
    bk_user_type = function.get_user_type(bk_username)
    print bk_username
    print bk_user_type
    return render_json({"bk_username": bk_username, "bk_user_type": bk_user_type})


# 获取退出登录地址
def get_logout_address(request):
    """
    获取退出登录地址,退出登录地址不同环境可以不一样，所以要在配置中配置
    :param request:
    :return:
    """
    logout_address = settings.LOG_OUT_ADDRESS
    return render_json(logout_address)
