# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1559465537.624
_enable_loop = True
_template_filename = 'C:/Users/X230/PycharmProjects/LanhuSaas/framework/templates/scene/scenecarousel1.html'
_template_uri = './scene/scenecarousel1.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <title>Title</title>\r\n    <script type="text/javascript" src="')
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
        __M_writer(u'css/net/font_997278_ptr5bdmor4j.css" rel="stylesheet">\r\n    <!--\u4ee5\u4e0b\u4e3a\u540e\u53f0\u53c2\u6570-->\r\n    <!--\r\n    "')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'";\t        // app\u7684url\u524d\u7f00,\u5728ajax\u8c03\u7528\u7684\u65f6\u5019\uff0c\u5e94\u8be5\u52a0\u4e0a\u8be5\u524d\u7f00\r\n    "')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'";       // \u9759\u6001\u8d44\u6e90\u524d\u7f00\r\n    **/--->\r\n    <link type="text/css" href="')
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
        __M_writer(u'js/net/jquery-1.10.2.min.js"></script>\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery.range-min.js"></script>\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/csrftoken.js"></script>\r\n\r\n    <link rel="stylesheet" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/net/iconfont.css">\r\n    <script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/net/jsplumb.min.js"></script>\r\n    <link rel="stylesheet" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/net/jsPlumbToolkit-defaults.css" />\r\n    <script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/dataflow/dataflow2.0.js"></script>\r\n    <link rel="stylesheet" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/monitorScene/dataflow-index.css">\r\n    <style>\r\n        .Drigging {\r\n            color: gray;\r\n            position: absolute;\r\n            border-radius: 0;\r\n            border: 1px solid #AAAAAA;\r\n        }\r\n    </style>\r\n</head>\r\n<body style="height: 100%">\r\n<input id="site_url" type="hidden" value="')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'">\r\n<div id="main">\r\n    <el-menu\r\n\r\n            class="el-menu-demo"\r\n            mode="horizontal"\r\n            background-color="#fafafa"\r\n            text-color="#fff"\r\n            active-text-color="#ffd04b">\r\n        <el-form :inline="true" class="demo-form-inline" style="margin: 50px 20px;">\r\n\r\n            <el-form-item label="\u5c97\u4f4d\u540d\u79f0:" size="mini"  prop="users">\r\n                <el-select v-model="position" placeholder="\u8bf7\u9009\u62e9\u5c97\u4f4d" >\r\n                    <el-option v-for="item in options" :label="item.label" :key="item.value"\r\n                               :value="item.value"></el-option>\r\n                </el-select>\r\n            </el-form-item>\r\n            <el-form-item label="\u8d77\u59cb\u65f6\u95f4:" size="mini">\r\n                <el-time-picker v-model="start" placeholder="\u5f00\u59cb\u65f6\u95f4\u70b9" format="HH:mm" value-format="HH:mm" >\r\n                </el-time-picker>\r\n                <el-time-picker v-model="end" placeholder="\u7ed3\u675f\u65f6\u95f4\u70b9" format="HH:mm" value-format="HH:mm" >\r\n                </el-time-picker>\r\n            </el-form-item>\r\n            <el-button type="info" v-on:click="query_scene_info">\u6d4b\u8bd5</el-button>\r\n        </el-form>\r\n    </el-menu>\r\n    <template>\r\n        <div class="block" style="overflow: hidden;">\r\n            <!-- \u9009\u62e9\u5458\u5de5\u4fe1\u606f strat -->\r\n            <div style="width: 100%;">\r\n\r\n            </div>\r\n            <!-- \u9009\u62e9\u5458\u5de5\u4fe1\u606f end -->\r\n            <!--<span class="demonstration">Click \u6307\u793a\u5668\u89e6\u53d1</span>-->\r\n            <!-- \u6bcf\u969410\u79d2\u5207\u6362\u4e00\u6b21\u8d70\u9a6c\u706f -->\r\n            <div id="div_sence"></div>\r\n        </div>\r\n    </template>\r\n</div>\r\n<script>\r\n    vm = new Vue({\r\n        el: "#main",\r\n        data: {\r\n          imgList: [],\r\n          imgHeight: \'\' + document.documentElement.clientHeight + \'px\',\r\n          start: \'09:00\',                                                                   //\u5f00\u59cb\u65f6\u95f4\r\n          end: \'18:00\',                                                                   //\u7ed3\u675f\u65f6\u95f4\r\n          region1: \'1\',                                                                 //\u5c97\u4f4d\u9009\u62e9\r\n          position: \'1\',                                                                  //\u5c97\u4f4d\r\n          options: [],\r\n          show_stop:null,//\u6682\u505c\r\n          show_index:0,\r\n          interval: 10,   //\u9ed8\u8ba410\u79d2\r\n        },\r\n        methods: {\r\n            //\u53d6\u914d\u7f6e\u7684\u8f6e\u64ad\u65f6\u95f4\r\n            get_time_interval(){\r\n                axios({\r\n                    method: \'post\',\r\n                    data:{\r\n                    code:"wheel_cycle"\r\n                    },\r\n                    url:  \'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_scene/open_scene_design/\',\r\n                }).then((res) => {\r\n                    if(res && res.data && res.data.time_interval && res.data.time_interval != ""){\r\n                        var regu = /^\\+?[1-9][0-9]*$/;\r\n                        //\u5237\u65b0\u9891\u7387\u53ea\u80fd\u662f\u975e0\u6b63\u6574\u6570\r\n                        if(regu.test(res.data.time_interval)){\r\n                            if(res.data.time_interval != vm.interval){\r\n                                vm.interval = res.data.time_interval;\r\n                                //\u6e05\u7a7a\u5b9a\u65f6\u4efb\u52a1\r\n                                clearInterval(vm.show_stop)\r\n                                //\u91cd\u65b0\u542f\u52a8\u5b9a\u65f6\u4efb\u52a1\r\n                                vm.time_task()\r\n                            }\r\n                        }\r\n                    }\r\n                })\r\n            },\r\n            get_pos() {\r\n                axios({\r\n                  method: \'post\',\r\n                  url:  \'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_scene/get_all_pos/\',\r\n                }).then((res) => {\r\n                    let json = [];\r\n                    if (res.data.message.length > 0) {\r\n                        for (var i = 0; i < res.data.message.length; i++) {\r\n                            let j = {};\r\n                            j.value = res.data.message[i].id;\r\n                            j.label = res.data.message[i].pos_name;\r\n                            json.push(j);\r\n                        }\r\n                        this.options = json;\r\n                        if(json.length>0){\r\n                            vm.position = json[0].value;\r\n                        }\r\n                    }\r\n                }).catch((res) => {\r\n                    vm.$message.error(\'\u83b7\u53d6\u7528\u6237\u9519\u8bef\')\r\n                })\r\n            },\r\n            time_task(){\r\n                if(vm.show_stop){\r\n                    clearInterval(vm.show_stop);\r\n                }\r\n                vm.show_stop = setInterval(function(){\r\n                    vm.get_time_interval();\r\n                    var iframe_dto = $("#div_sence iframe");\r\n                    if(iframe_dto.length>0){\r\n                        if(vm.show_index==(iframe_dto.length-1)){\r\n                            vm.show_index = -1;\r\n                        }\r\n                        vm.show_index=vm.show_index+1\r\n                        iframe_dto.hide();\r\n                        $(iframe_dto[vm.show_index]).show();\r\n                    }\r\n                },vm.interval*1000);\r\n            },\r\n            query_scene_info:function(){\r\n                //\u53d6\u5f97\u914d\u7f6e\u7684\u8f6e\u64ad\u65f6\u95f4\u95f4\u9694\r\n                vm.get_time_interval();\r\n                $.ajax({\r\n                    url:"')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_scene/query_pos_scene"\r\n                    ,async:false\r\n                    ,data: {\r\n                        \'pos_id\': vm.position,\r\n                        \'start\': vm.start,\r\n                        \'end\': vm.end\r\n                    }\r\n                    ,type:"post"\r\n                    ,dataType:"json"\r\n                    ,success:function(data){\r\n                        if(vm.show_stop!=null){\r\n                            clearInterval(vm.show_stop);//\u8bbe\u7f6e\u505c\u6b62\r\n                            vm.show_stop = null;\r\n                        }\r\n                        $("#div_sence").html("");\r\n                        if(data.message!=""){\r\n                            var djson = data.message ;//eval(\'(\'+data.message+\')\');\r\n                            for(var i=0;i<djson.length;i++){\r\n                                var t="display:none;"\r\n                                if(i ==0){\r\n                                    t="";\r\n                                }\r\n                                var html="<iframe id=\'i"+djson[i]+"\' scrolling=\\"no\\"  src=\'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_scene/page_query_xml_show?id=";\r\n                                html+=djson[i]+"\' style=\'"+t+"width:1200px;height:"+vm.imgHeight+";border:none;\'></iframe>";\r\n                                $("#div_sence").append(html);\r\n                            }\r\n                            vm.time_task()\r\n                        }\r\n                    }\r\n                })\r\n            }\r\n        }\r\n    })\r\n    vm.get_pos();\r\n</script>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "23": 1, "24": 5, "25": 5, "26": 6, "27": 6, "28": 7, "29": 7, "30": 8, "31": 8, "32": 10, "33": 10, "34": 12, "35": 12, "36": 14, "37": 14, "38": 16, "39": 16, "40": 18, "41": 18, "42": 20, "43": 20, "44": 22, "45": 22, "46": 24, "47": 24, "48": 27, "49": 27, "50": 28, "51": 28, "52": 30, "53": 30, "54": 31, "55": 31, "56": 32, "57": 32, "58": 33, "59": 33, "60": 34, "61": 34, "62": 35, "63": 35, "64": 36, "65": 36, "66": 37, "67": 37, "68": 39, "69": 39, "70": 40, "71": 40, "72": 41, "73": 41, "74": 42, "75": 42, "76": 43, "77": 43, "78": 54, "79": 54, "80": 116, "81": 116, "82": 136, "83": 136, "84": 176, "85": 176, "86": 198, "87": 198, "93": 87}, "uri": "./scene/scenecarousel1.html", "filename": "C:/Users/X230/PycharmProjects/LanhuSaas/framework/templates/scene/scenecarousel1.html"}
__M_END_METADATA
"""
