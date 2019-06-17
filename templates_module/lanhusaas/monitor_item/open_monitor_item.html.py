# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1558080801.077
_enable_loop = True
_template_filename = 'C:/Users/X230/PycharmProjects/LanhuSaas/framework/templates/monitor_item/open_monitor_item.html'
_template_uri = './monitor_item/open_monitor_item.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<html>\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <!-- \u5f00\u53d1\u73af\u5883\u7248\u672c\uff0c\u5305\u542b\u4e86\u6709\u5e2e\u52a9\u7684\u547d\u4ee4\u884c\u8b66\u544a--2.5.51 -->\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/vue.development.js"></script>\r\n    <!-- element UI\u5f15\u5165\u6837\u5f0f -->\r\n    <link rel="stylesheet" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/element-2.4.11/index.css">\r\n    <!-- element UI\u5f15\u5165\u7ec4\u4ef6\u5e93 -->\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/element-2.4.11/index.js"></script>\r\n    <!--axios.min.js--vue.js\u7684ajax\u652f\u6301-->\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/axios.min.js"></script>\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/jquery/jquery-3.1.1.min.js"></script>\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/csrftoken.js"></script>\r\n    <link type="text/css" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/home.css" rel="stylesheet">\r\n    <link rel="stylesheet" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/net/style.min.css">\r\n\r\n    <script type="text/javascript"\r\n            src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/net/jsplumb.min.js"></script>\r\n    <link rel="stylesheet"\r\n          href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/net/jsPlumbToolkit-defaults.css"/>\r\n    <link rel="stylesheet" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/monitorScene/dataflow-index.css">\r\n    <link rel="stylesheet" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/net/iconfont.css">\r\n    <link rel="stylesheet" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/maintenanceIndex/maintenanceIndex.css">\r\n</head>\r\n<body >\r\n<div align="right" ><img src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'img/close.jpg" onclick="vm.hide_this_win()" width="20px" height="20px" align="right"></img></div>\r\n<div id="app" style="background: #ffffff;height:300px;width:600px;" >\r\n    <!-- div1 start-->\r\n    <div class="div_one" style="padding: 20px 40px 0px 40px;">\r\n\r\n        <div @keyup.enter="select">\r\n            <el-input placeholder="\u8bf7\u8f93\u5165\u5185\u5bb9" clearable v-model="contents" style="width:70%" @keyup.enter="select"></el-input>\r\n            <el-button type="primary" icon="el-icon-search" v-on:click="select" style="width:20%;margin-left:40px;">\u641c\u7d22</el-button>\r\n        </div>\r\n        <div style="height: 20px"></div>\r\n        <div >\r\n            <el-table :data=\'sites\'  style="width: 100%;" border header-align="center">\r\n                <el-table-column prop="id" min-width="15%" label="\u5e8f\u53f7" sortable></el-table-column>\r\n                <el-table-column prop="monitor_name" show-overflow-tooltip="true" min-width="40%" label="\u76d1\u63a7\u540d\u79f0" sortable></el-table-column>\r\n                <el-table-column prop="monitor_type" show-overflow-tooltip="true" min-width="30%" label="\u76d1\u63a7\u7c7b\u578b" :formatter="format_monitor_type" sortable></el-table-column>\r\n                <el-table-column label="\u64cd\u4f5c" min-width="15%">\r\n                    <template slot-scope="scope">\r\n                        <el-button size="mini" type="text" v-on:click="select_one(scope.row)">\u5173\u8054</el-button>\r\n                    </template>\r\n                </el-table-column>\r\n            </el-table>\r\n            <el-pagination :page-count="page_count" background layout="prev, pager, next" style="float:right"\r\n                           @current-change="current_change1" :current-page="page"></el-pagination>\r\n        </div>\r\n    </div>\r\n</div>\r\n</body>\r\n<script>\r\n    //csrf\u9a8c\u8bc1\r\n    axios.interceptors.request.use((config) => {\r\n        config.headers[\'X-Requested-With\'] = \'XMLHttpRequest\';\r\n        let regex = /.*csrftoken=([^;.]*).*$/; // \u7528\u4e8e\u4ececookie\u4e2d\u5339\u914d csrftoken\u503c\r\n        config.headers[\'X-CSRFToken\'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];\r\n        return config\r\n    });\r\n    var vm = new Vue({\r\n        el: \'#app\',\r\n        data: {\r\n            page_count: 100,                            //\u603b\u9875\u7801\u6570\r\n            page: 1,                                    //\u5206\u9875\u9875\u7801\u6570\r\n            sites: [],                                  //table\u5185\u5bb9\r\n            message: \'\',                                //\u5f39\u6846\u63d0\u793a\u4fe1\u606f\r\n            contents:\'\',\r\n            base: {\r\n                //\u57fa\u672c\u5355\u5143\r\n                dimension_data:[],//\u7ef4\u5ea6\u540d\u79f0\r\n                measures_name:\'\',//\u6307\u6807\u540d\u79f0\r\n                measures:\'\',       //\u6307\u6807\u96c6\r\n                interface_type:\'\',//\u63a5\u53e3\u7c7b\u578b\r\n                show_rule_type:\'\',//\u5c55\u793a\u89c4\u5219\r\n                monitor_name: \'\',                      //\u5355\u5143\u540d\u79f0\r\n                monitor_type: \'\',                      //\u5355\u5143\u7c7b\u578b\r\n                font_size: \'20\',                         //\u5b57\u53f7\r\n                height: \'480\',                            //\u9ad8\u5ea6\r\n                width: \'422\',                             //\u5bbd\u5ea6\r\n                start_time: \'\',                        //\u5f00\u59cb\u65f6\u95f4\r\n                end_time: \'\',                          //\u7ed3\u675f\u65f6\u95f4\r\n                period: \'10\',                            //\u91c7\u96c6\u5468\u671f\r\n                params: \'\',                            //\u76d1\u63a7\u53c2\u6570\r\n                status: \'\',                            //\u76d1\u63a7\u72b6\u6001\r\n                gather_rule: \'\',                       //\u91c7\u96c6\u89c4\u5219\r\n                gather_params: \'sql\',                  //\u91c7\u96c6\u53c2\u6570\r\n                monitor_area: \'\'                             //\u65e5\u5386\u5730\u533a\r\n            },\r\n        },\r\n        methods: {\r\n            show() {\r\n                axios({\r\n                    method: \'post\',\r\n                    url: \'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u"monitor_item/show/',\r\n                    data: {\r\n                        page: vm.page,\r\n                        limit: 5\r\n                    },\r\n                }).then(function (res) {\r\n                    vm.sites = res.data.results.res_list;\r\n                    vm.page_count = res.data.results.res_list[0].page_count;\r\n                })\r\n            },\r\n            select() {\r\n                axios({\r\n                    method: 'post',\r\n                    url: '")
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_item/select/\',\r\n                    data: {\r\n                        data: vm.contents,\r\n                        page: vm.page,\r\n                        limit: 5\r\n                    }\r\n                }).then((res) => {\r\n                    if (res.data.results.length == 0) {\r\n                        vm.sites = [];\r\n                        vm.page_count = 1\r\n                    } else {\r\n                        vm.sites = res.data.results;\r\n                        vm.page_count = res.data.results[0].page_count;\r\n                    }\r\n                }).catch(function (e) {\r\n                vm.$message.error(\'\u83b7\u53d6\u6570\u636e\u5931\u8d25\uff01\');\r\n                });\r\n            },\r\n            current_change1(value) {\r\n                vm.page = value;\r\n                vm.select()\r\n            },\r\n            select_one(row) {\r\n                $("#openMonitorItem", window.parent.document).hide();\r\n                window.parent.relation_monitor_item_id(row.id,row.monitor_name);\r\n                //alert(row.id);\r\n            },\r\n            hide_this_win(){\r\n                $("#openMonitorItem", window.parent.document).hide();\r\n            },\r\n            format_monitor_type(row,column){\r\n                if(row.monitor_type === 1){\r\n                    return "\u57fa\u672c\u76d1\u63a7\u9879"\r\n                }else if(row.monitor_type === 2){\r\n                    return "\u56fe\u8868\u76d1\u63a7\u9879"\r\n                }else if(row.monitor_type === 3){\r\n                    return "\u4f5c\u4e1a\u76d1\u63a7\u9879"\r\n                }else if(row.monitor_type === 4){\r\n                    return "\u6d41\u7a0b\u76d1\u63a7\u9879"\r\n                }else if(row.monitor_type === 5){\r\n                    return "\u57fa\u672c\u76d1\u63a7\u9879\uff08\u4e00\u4f53\u5316\u5e73\u53f0\uff09"\r\n                }\r\n            }\r\n        },\r\n    });\r\n    vm.select();\r\n</script>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "23": 1, "24": 5, "25": 5, "26": 7, "27": 7, "28": 9, "29": 9, "30": 11, "31": 11, "32": 12, "33": 12, "34": 13, "35": 13, "36": 14, "37": 14, "38": 15, "39": 15, "40": 18, "41": 18, "42": 20, "43": 20, "44": 21, "45": 21, "46": 22, "47": 22, "48": 23, "49": 23, "50": 26, "51": 26, "52": 95, "53": 95, "54": 108, "55": 108, "61": 55}, "uri": "./monitor_item/open_monitor_item.html", "filename": "C:/Users/X230/PycharmProjects/LanhuSaas/framework/templates/monitor_item/open_monitor_item.html"}
__M_END_METADATA
"""
