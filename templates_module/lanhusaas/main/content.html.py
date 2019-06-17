# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1558341673.787
_enable_loop = True
_template_filename = 'C:/Users/X230/PycharmProjects/LanhuSaas/framework/templates/main/content.html'
_template_uri = './main/content.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <title>\u591c\u95f4\u503c\u73ed</title>\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/vue.development.js"></script>\r\n    <!-- \u751f\u4ea7\u73af\u5883\u7248\u672c\uff0c\u4f18\u5316\u4e86\u5c3a\u5bf8\u548c\u901f\u5ea6 \u529f\u80fd\u5b8c\u5584\u540e\u8bf7\u5c06vue.development.js\u8be5\u4e3avue.js-->\r\n    <!--<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/vue.js"></script>-->\r\n    <!-- vue\u7684ajax\u4f9d\u8d56-->\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/axios.min.js"></script>\r\n    <!-- element UI\u5f15\u5165\u6837\u5f0f -->\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/element-2.4.11/index.css" rel="stylesheet">\r\n    <!-- element UI\u5f15\u5165\u7ec4\u4ef6\u5e93 -->\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/element-2.4.11/index.js"></script>\r\n    <script src=\'')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u"js/jquery.min.js'></script>\r\n    <script src='")
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery-ui.js\'></script>\r\n    <!--jQuery\u5e93\u4f7f\u7528\u65f6\u8bf7\u4f7f\u7528\u6807\u51c6jQuery\u8bed\u6cd5-->\r\n    <!--<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/jquery/jquery-3.1.1.min.js"></script>-->\r\n    <!--\u9875\u9762\u521d\u59cb\u5316css(Tencent)-->\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/init.css" rel="stylesheet">\r\n    <!-- \u5f15\u5165\u989d\u5916\u7684\u5305-->\r\n\r\n</head>\r\n<body style="overflow: scroll;">\r\n<div id="content">\r\n<template>\r\n  <el-tabs v-model="activeName" @tab-click="handleClick">\r\n    <el-tab-pane label="\u503c\u73ed\u7ba1\u7406" name="first"><iframe  v-show="true"  style="width: 100%;height: 1050px;"\r\n                            :src="\'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'\'+nightFirst"\r\n                            frameborder="0"></iframe></el-tab-pane>\r\n    <el-tab-pane label="\u591c\u95f4\u503c\u73ed\u6d41\u7a0b\u56fe1" name="second"><iframe  v-show="true" style="width: 100%;height: 1050px;"\r\n                            :src="\'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'\'+nightSecond"\r\n                            frameborder="0" style="width: 1166px;height: 1050px;"></iframe></el-tab-pane>\r\n    <el-tab-pane label="\u591c\u95f4\u503c\u73ed\u6d41\u7a0b\u56fe2" name="third"><iframe  v-show="true" style="width: 100%;height: 1050px;"\r\n                            :src="\'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'\'+nightThird"\r\n                            frameborder="0" style="width: 1166px;height: 1050px;"></iframe></el-tab-pane>\r\n  </el-tabs>\r\n</template>\r\n</div>\r\n</body>\r\n\r\n\r\n\r\n<script type="text/javascript">\r\n\r\n    var ve = new Vue({\r\n        el: \'#content\',\r\n        data() {\r\n          return {\r\n            activeName: \'first\',\r\n            nightFirst:\'night_first\',\r\n            nightSecond:\'night_second\',\r\n            nightThird:\'night_third\',\r\n\r\n          };\r\n        },\r\n        methods: {\r\n          handleClick(tab, event) {\r\n            console.log(tab, event);\r\n          }\r\n        }\r\n    });\r\n</script>\r\n\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "23": 1, "24": 6, "25": 6, "26": 8, "27": 8, "28": 10, "29": 10, "30": 12, "31": 12, "32": 14, "33": 14, "34": 15, "35": 15, "36": 16, "37": 16, "38": 18, "39": 18, "40": 20, "41": 20, "42": 29, "43": 29, "44": 32, "45": 32, "46": 35, "47": 35, "53": 47}, "uri": "./main/content.html", "filename": "C:/Users/X230/PycharmProjects/LanhuSaas/framework/templates/main/content.html"}
__M_END_METADATA
"""
