# encoding:utf-8
import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import function
from common.mymako import render_json, render_mako_context


# Create your views here.

def index(request):
    """

    :param request:
    :return:
    """
    return render_mako_context(request, './logmanagement/logmanagement.html')


def add_log(info):
    """

    :param info:
    :return:
    """
    res = function.add_log(info)
    return render_json(res)


@csrf_exempt
def show_all(request):
    """

    :param request:
    :return:
    """
    res = function.show_all(request)
    return render_json(res)


@csrf_exempt
def select_log(request):
    """

    :param request:
    :return:
    """
    res = function.select_log(request)
    return render_json(res)
