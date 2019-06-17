# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1559485213.36
_enable_loop = True
_template_filename = 'C:/Users/X230/PycharmProjects/LanhuSaas/framework/templates/scene/scenecarousel.html'
_template_uri = './scene/scenecarousel.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <title>Title</title>\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/net/jquery-1.10.2.min.js"></script>\r\n    <script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/dataflow/dataflow2.0.js"></script>\r\n    <script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/Component-based.js"></script>\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/net/echarts.min.js"></script>\r\n    <!-- \u5f00\u53d1\u73af\u5883\u7248\u672c\uff0c\u5305\u542b\u4e86\u6709\u5e2e\u52a9\u7684\u547d\u4ee4\u884c\u8b66\u544a--2.5.51 ')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/-->\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/vue.development.js"></script>\r\n    <!-- \u751f\u4ea7\u73af\u5883\u7248\u672c\uff0c\u4f18\u5316\u4e86\u5c3a\u5bf8\u548c\u901f\u5ea6 \u529f\u80fd\u5b8c\u5584\u540e\u8bf7\u5c06vue.development.js\u8be5\u4e3avue.js-->\r\n    <!--<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/vue.js"></script>-->\r\n    <!-- element UI\u5f15\u5165\u6837\u5f0f -->\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/element-2.4.11/index.css" rel="stylesheet">\r\n    <!-- element UI\u5f15\u5165\u7ec4\u4ef6\u5e93 -->\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/element-2.4.11/index.js"></script>\r\n    <!-- vue\u7684ajax\u4f9d\u8d56-->\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/axios.min.js"></script>\r\n    <!--jQuery\u5e93\u4f7f\u7528\u65f6\u8bf7\u4f7f\u7528\u6807\u51c6jQuery\u8bed\u6cd5-->\r\n    <!--<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/jquery/jquery-3.1.1.min.js"></script>-->\r\n    <!--\u9875\u9762\u521d\u59cb\u5316css(Tencent)-->\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/common/init.css" rel="stylesheet">\r\n    <!--\u672c\u9875\u9762css-->\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/common/main.css" rel="stylesheet">\r\n    <!--\u963f\u91cc\u5df4\u5df4\u77e2\u91cf\u56fe\u6807\u5e93--\u9879\u76ee\u5b8c\u6210\u540e\u8bf7\u4e0b\u8f7dcss\u5e76\u4e0b\u8f7dcss\u5f15\u7528\u7684\u5b57\u4f53\u6587\u4ef6-->\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/net/font_997278_ptr5bdmor4j.css" rel="stylesheet">\r\n\r\n    <!--\u4ee5\u4e0b\u4e3a\u540e\u53f0\u53c2\u6570-->\r\n    <!--\r\n    "')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'";\t        // app\u7684url\u524d\u7f00,\u5728ajax\u8c03\u7528\u7684\u65f6\u5019\uff0c\u5e94\u8be5\u52a0\u4e0a\u8be5\u524d\u7f00\r\n    "')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'";       // \u9759\u6001\u8d44\u6e90\u524d\u7f00\r\n    **/--->\r\n\r\n    <link type="text/css" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/monitorScene/style.css" rel="stylesheet">\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/net/index.min.js"></script>\r\n    <link rel="stylesheet" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/net/style.min.css">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/net/bk.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/net/jquery.range.css" rel="stylesheet">\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery.range-min.js"></script>\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/csrftoken.js"></script>\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/net/jquery-1.10.2.min.js"></script>\r\n    <link rel="stylesheet" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/net/iconfont.css">\r\n    <script type="text/javascript"\r\n            src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/net/jsplumb.min.js"></script>\r\n    <link rel="stylesheet"\r\n          href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/net/jsPlumbToolkit-defaults.css"/>\r\n    <link rel="stylesheet" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/monitorScene/dataflow-index.css">\r\n</head>\r\n<body>\r\n<input id="site_url" type="hidden" value="')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'">\r\n<div id="main">\r\n    <template>\r\n         <div id="div_sence"></div>\r\n    </template>\r\n</div>\r\n<!--\u6682\u65f6\u7684css\u6837\u5f0f-->\r\n\r\n<script>\r\n      vm = new Vue({\r\n          el: "#main",\r\n          data: {\r\n              imgList: [],\r\n              imgWidth:\'\'+(document.documentElement.clientWidth-20)+\'px\',\r\n              imgHeight: \'\' + (document.documentElement.clientHeight-50) + \'px\',\r\n              region1: \'1\',                                                                 //\u5c97\u4f4d\u9009\u62e9\r\n              position: \'1\',                                                                  //\u5c97\u4f4d\r\n              options: [],\r\n              show_stop:null,//\u6682\u505c\r\n              show_index:0,\r\n              interval: 10,   //\u9ed8\u8ba410\u79d2\r\n          },\r\n          methods: {\r\n              //\u53d6\u914d\u7f6e\u7684\u8f6e\u64ad\u65f6\u95f4\r\n              get_time_interval(){\r\n                  axios({\r\n                      method: \'post\',\r\n                      data:{\r\n                          code:"wheel_cycle"\r\n                      },\r\n                      url:  \'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_scene/open_scene_design/\',\r\n                  }).then((res) => {\r\n                      if(res && res.data && res.data.time_interval && res.data.time_interval != ""){\r\n                          let reg = /^\\+?[1-9][0-9]*$/;\r\n                          if(reg.test(res.data.time_interval)){\r\n                              if(res.data.time_interval != vm.interval){\r\n                                  vm.interval = res.data.time_interval;\r\n                                  //\u6e05\u7a7a\u5b9a\u65f6\u4efb\u52a1\r\n                                  clearInterval(vm.show_stop);\r\n                                  //\u91cd\u65b0\u542f\u52a8\u5b9a\u65f6\u4efb\u52a1\r\n                                  vm.time_task();\r\n                              }\r\n                          }\r\n                      }\r\n                  })\r\n              },\r\n              time_task(){\r\n                  if(vm.show_stop){\r\n                     clearInterval(vm.show_stop);\r\n                  }\r\n                  vm.show_stop = setInterval(function(){\r\n                      vm.get_time_interval()\r\n                      var iframe_dto = $("#div_sence iframe");\r\n                      if(iframe_dto.length>0){\r\n                          if(vm.show_index==(iframe_dto.length-1)){\r\n                              vm.show_index = -1;\r\n                          }\r\n                          vm.show_index=vm.show_index+1\r\n                          iframe_dto.hide();\r\n                          $(iframe_dto[vm.show_index]).show();\r\n                      }\r\n                  },vm.interval*1000);\r\n              },\r\n              query_scene_info:function(){\r\n                  //\u53d6\u5f97\u914d\u7f6e\u7684\u8f6e\u64ad\u65f6\u95f4\u95f4\u9694\r\n                  vm.get_time_interval();\r\n                  $.ajax({\r\n                      url:"')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_scene/query_curr_user_scene"\r\n                      ,async:false\r\n                      ,type:"post"\r\n                      ,dataType:"json"\r\n                      ,success:function(data){\r\n                          if(vm.show_stop!=null){\r\n                              clearInterval(vm.show_stop);//\u8bbe\u7f6e\u505c\u6b62\r\n                              vm.show_stop = null;\r\n                          }\r\n                          $("#div_sence").html("");\r\n                          if(data.message!=""){\r\n                              var djson = data.message ;//eval(\'(\'+data.message+\')\');\r\n                              for(var i=0;i<djson.length;i++){\r\n                                 var t="display:none;"\r\n                                 if(i ==0){\r\n                                     t="";\r\n                                 }\r\n                                 var html="<iframe id=\'i"+djson[i]+"\' scrolling=\\"auto\\" src=\'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_scene/page_query_xml_show?id=";\r\n                                 html+=djson[i]+"\' style=\'"+t+"width:"+vm.imgWidth+";height:1200px;border:none;\'></iframe>";\r\n                                 $("#div_sence").append(html);\r\n                                 //$("#div"+djson[i]).load("')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_scene/page_query_xml_show?id="+djson[i]);\r\n                                 //html.hide()\r\n                              }\r\n                              vm.time_task();\r\n                          }\r\n                      }\r\n                  })\r\n              }\r\n          }\r\n      })\r\n      vm.query_scene_info();\r\n</script>\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "23": 1, "24": 5, "25": 5, "26": 6, "27": 6, "28": 7, "29": 7, "30": 8, "31": 8, "32": 9, "33": 9, "34": 10, "35": 10, "36": 12, "37": 12, "38": 14, "39": 14, "40": 16, "41": 16, "42": 18, "43": 18, "44": 20, "45": 20, "46": 22, "47": 22, "48": 24, "49": 24, "50": 26, "51": 26, "52": 30, "53": 30, "54": 31, "55": 31, "56": 34, "57": 34, "58": 35, "59": 35, "60": 36, "61": 36, "62": 37, "63": 37, "64": 38, "65": 38, "66": 39, "67": 39, "68": 40, "69": 40, "70": 41, "71": 41, "72": 42, "73": 42, "74": 44, "75": 44, "76": 46, "77": 46, "78": 47, "79": 47, "80": 50, "81": 50, "82": 80, "83": 80, "84": 117, "85": 117, "86": 134, "87": 134, "88": 137, "89": 137, "95": 89}, "uri": "./scene/scenecarousel.html", "filename": "C:/Users/X230/PycharmProjects/LanhuSaas/framework/templates/scene/scenecarousel.html"}
__M_END_METADATA
"""
