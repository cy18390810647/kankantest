# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1562756191.882
_enable_loop = True
_template_filename = 'D:/Users/X230/lanhusaas/framework/templates/monitor_scene/page_query_xml_show.html'
_template_uri = '/monitor_scene/page_query_xml_show.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        data = context.get('data', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!--[if IE]><meta http-equiv="X-UA-Compatible" content="IE=5,IE=9" ><![endif]-->\r\n<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <title>\u6570\u636e\u5e93\u8bfb\u53d6\u6d41\u7a0b\u5e76\u5c55\u793a</title>\r\n\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\r\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">\r\n    <style type="text/css">\r\n\t\t.flow {\r\n\t\t  stroke-dasharray: 8;\r\n\t\t  animation: dash 0.5s linear;\r\n\t\t  animation-iteration-count: infinite;\r\n\t\t}\r\n\t\t@keyframes dash {\r\n\t\t  to {\r\n\t\t    stroke-dashoffset: -16;\r\n\t\t  }\r\n\t\t}\r\n\t</style>\r\n\t<script type="text/javascript">\r\n\t\tvar static_url = "')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'";\r\n        var site_url = "')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'";\r\n\t</script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Init.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/jscolor/jscolor.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/sanitizer/sanitizer.min.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/../../../src/js/mxClient.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Graph.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Format.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Shapes.js"></script>\r\n    <script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery-1.10.2.min.js"></script>\r\n</head>\r\n\t<script type="text/javascript">\r\n\t\t// Extends EditorUi to update I/O action states based on availability of backend\r\n        //\u9ed8\u8ba4\u53d6\u8f6e\u64ad\u6570\u636e\u7684\u65f6\u95f4\u95f4\u9694\u4e3a10\u79d2\r\n        let interval = 10;\r\n        let get_data_stop = null;\r\n\t\tvar graph =null;\r\n\t\tvar data_xml= \'')
        __M_writer(unicode(data))
        __M_writer(u'\'\r\n        let id = getUrlParam(\'id\');\r\n        function main(container){\r\n\t\t\tgraph = new mxGraph(container);\r\n\t\t\tgraph.setTooltips(true);\r\n\t\t\tgraph.setEnabled(false);\r\n\t\t\tload_Data();\r\n\t\t}\r\n\t\tfunction getUrlParam(name) {\r\n            //\u6784\u9020\u4e00\u4e2a\u542b\u6709\u76ee\u6807\u53c2\u6570\u7684\u6b63\u5219\u8868\u8fbe\u5f0f\u5bf9\u8c61\r\n            var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");\r\n            //\u5339\u914d\u76ee\u6807\u53c2\u6570\r\n            var r = window.location.search.substr(1).match(reg);\r\n            //\u8fd4\u56de\u53c2\u6570\u503c\r\n            if (r != null) return unescape(r[2]); return null;\r\n        }\r\n\t\tfunction get_time_interval(){\r\n            axios({\r\n                method: \'post\',\r\n                data:{\r\n                    code:"wheel_data_cycle"\r\n                },\r\n              url:  \'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_scene/open_scene_design/\',\r\n            }).then((res) => {\r\n                if(res && res.data && res.data.time_interval && res.data.time_interval != ""){\r\n                    let reg = /^\\+?[1-9][0-9]*$/;\r\n                    if(reg.test(res.data.time_interval)){\r\n                        if(res.data.time_interval != interval){\r\n                            interval = res.data.time_interval;\r\n                            //\u6e05\u7a7a\u5b9a\u65f6\u4efb\u52a1\r\n                            clearInterval(get_data_stop);\r\n                            //\u91cd\u65b0\u542f\u52a8\u5b9a\u65f6\u4efb\u52a1\r\n                            get_data_stop = setInterval(load_Data,interval*1000);\r\n                        }\r\n                    }\r\n                }\r\n            })\r\n            }\r\n\t\tget_data_stop = setInterval(load_Data,interval*1000)\r\n\t\t//\u4fbf\u4e8e\u91c7\u96c6\u6570\u636e\r\n        function load_Data(){\r\n\t\t    if(data_xml!=""&&data_xml!="None"){\r\n\t\t\t    var doc = mxUtils.parseXml(data_xml);\r\n                var codec = new mxCodec(doc)\r\n                try{//\u5c06xml\u4e2d\u7684\u8282\u70b9\u8f6c\u6362\u6210svg\uff0c\u5728\u6d4f\u89c8\u5668\u6e32\u67d3\r\n                    codec.decode(doc.documentElement, graph.getModel());\r\n                }catch (e) {\r\n\r\n                }\r\n                var model = graph.getModel();\r\n                var param = ""\r\n                var param_map={} //\u6839\u636e\u76d1\u63a7\u9879id\u67e5\u8be2\u7ec4\u4ef6id\r\n                for(key_index in model.cells){\r\n                    var cell = model.cells[key_index];\r\n                    if(cell.value!=undefined\r\n                            &&typeof(cell.value) == "object"){\r\n                        if(param!=""){\r\n                            param+="&";\r\n                        }\r\n                        if(param_map[cell.value.getAttribute("item_id")] != undefined){\r\n                            continue;\r\n                        }\r\n                        param_map[cell.value.getAttribute("item_id")] = cell.id;\r\n                        param +="id="+ cell.value.getAttribute("item_id");\r\n                        //cell.value = cell.value.getAttribute("item_id")+"_"+cell.id\r\n                    }\r\n                }\r\n                $.ajax({\r\n                    url:"')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_scene/query_scene_item_data?"+param\r\n                    ,async:false\r\n                    ,dataType:"json"\r\n                    ,success:function(data){\r\n                        var ifr_data = document.getElementsByTagName("iframe");\r\n                        if(ifr_data.length>0){\r\n                            for(var i=0;i<ifr_data.length;i++){\r\n                               ifr_data[i].remove();\r\n                             //  document.body.parentElement.remove(ifr_data[i]);\r\n                            }\r\n                        }\r\n                        if(data.message!=""){\r\n                            var data_json = eval(\'(\'+data.message+\')\');\r\n                            //darr[0]["key_name"].split(/[\\r\\n]/)\r\n                            for(var temp_num in data_json){\r\n                                var temp_dto= data_json[temp_num];//\u83b7\u53d6\u5bf9\u8c61\r\n                                if(temp_dto["item_type"] == 2){ //\u4e3a\u56fe\u8868\u76d1\u63a7\r\n                                    graph.getModel().cells[param_map[temp_dto["id"]]].attribute\r\n                                       = temp_dto["key_name"]\r\n                                    continue;\r\n                                }\r\n                                // var str_val = temp_dto["key_name"].split(/[\\r\\n]/);\r\n                                var  calc_key = "";\r\n                                if(temp_dto["key_val"].indexOf("@")>-1){\r\n                                    calc_key = "@";\r\n                                }else if(temp_dto["key_val"].indexOf("#")>-1){\r\n                                    calc_key = "#";\r\n                                }else if(temp_dto["key_val"].indexOf("%")>-1){\r\n                                    calc_key = "%";\r\n                                }\r\n                                if(calc_key == ""){\r\n                                    continue;\r\n                                }\r\n                                var  calc_data = temp_dto["key_val"].split(calc_key);\r\n                                if(calc_key=="#"){//\u6587\u672c\u6846\u5185\u5bb9\u8bbe\u7f6e\u989c\u8272\r\n                                    var color_val = calc_data[1];\r\n                                    if(calc_data.length>2){\r\n                                        color_val = temp_dto["key_val"].split(calc_key)[1];\r\n                                    }\r\n                                    var color_cell =graph.getModel().cells[param_map[temp_dto["id"]]]\r\n                                    color_cell.value = "";\r\n                                    graph.setCellStyles(mxConstants.STYLE_FILLCOLOR,\r\n                                       \'#\'+color_val, [color_cell]);\r\n                                }else if(calc_key == "@"){\r\n                                    var txt = calc_data[1]\r\n                                    var cell_dto =graph.getModel().cells[param_map[temp_dto["id"]]];\r\n                                    if(txt.indexOf("[")>-1){\r\n                                        txt = txt.split("[")[0]\r\n                                    }\r\n                                    cell_dto.value= getNewline(txt);//\u53d6\u51fa\u6570\u636e,\u8d85\u8fc720\u4e2a\u5b57\u7b26\u5c31\u6298\u884c\r\n                                    if(temp_dto["key_val"].indexOf("@") == 0){\r\n                                         graph.setCellStyles(mxConstants.STYLE_FILLCOLOR,\r\n                                       \'#cecece\', [cell_dto]);\r\n                                    }else if(temp_dto["key_val"].indexOf("db@") == 0){//\u6570\u636e\u5e93\u76d1\u63a7\u9879\u503c\u4e3a0\r\n                                         var color_str ="#cecece";\r\n                                         var txt_str = calc_data[1]\r\n                                             .replace(txt,"").replace("[","")\r\n                                             .replace("]","");\r\n                                         if(txt_str == "1"){\r\n                                             color_str ="#7CFC00";\r\n                                         }\r\n                                       graph.setCellStyles(mxConstants.STYLE_FILLCOLOR,\r\n                                       color_str, [cell_dto]);\r\n                                    }\r\n                                }else if(calc_key == "%"){\r\n                                     graph.getModel().cells[param_map[temp_dto["id"]]].value\r\n                                                   = temp_dto["key_val"];//\u53d6\u51fa\u6570\u636e\r\n                                }\r\n                            }\r\n                        }\r\n                    }\r\n                })\r\n                var model = graph.getModel();\r\n                for(key_index in model.cells) {\r\n                    var cell = model.cells[key_index];\r\n                    if(typeof(cell.value) == "object"){\r\n                        cell.value ="";\r\n                    }\r\n                }\r\n                graph.refresh(); //\u5237\u65b0\u5bb9\u5668\r\n                for(key_index in model.cells){\r\n\t\t\t\t   var cell = model.cells[key_index];\r\n\t\t\t\t   if(cell.style != undefined&&\r\n\t\t\t\t      cell.style.indexOf("edgeStyle=orthogonalEdgeStyle")>-1){\r\n\t\t\t\t       lineFlow(model,graph,key_index);\r\n                   }\r\n\t\t\t\t   if(cell.attribute!="" && cell.attribute && cell.parent.geometry){\r\n                       var x = cell.parent.geometry.x;\r\n                       var y = cell.parent.geometry.y;\r\n                       var ifr = document.createElement("iframe");\r\n                      // var ifr= document.getElementById("ifr_t");\r\n                       ifr.id="ifr"+Math.floor(Math.random()*100000+1);\r\n                       ifr.style.left=x+"px";\r\n                       ifr.style.top= y+"px";\r\n                       ifr.style.width = (cell.parent.geometry.width+8)+"px";\r\n                       ifr.style.height= (cell.parent.geometry.height+8)+"px";\r\n                       ifr.style.position="absolute";\r\n                       ifr.style.backgroundColor = "black";\r\n                       ifr.src = cell.attribute;\r\n                       ifr.style.display="block";\r\n                       document.body.appendChild(ifr);\r\n                       continue;\r\n                   }\r\n                }\r\n            }else{\r\n\t\t\t    document.body.innerHTML = \'<center style="margin-top:10%;">Error loading resource files. Please check browser console.</center>\';\r\n            }\r\n        }\r\n\t\t//\u76d1\u63a7\u9879\u7279\u6548\r\n        function monitorFlow(model,graph,id,id1) {\r\n            var cell = model.getCell(id);//\u62ffxml\u4e2d\u5bf9\u8c61id\r\n            var cell1 = model.getCell(id1);//\u62ffxml\u4e2d\u5bf9\u8c61id\r\n            var color = \'\';var txtCpu = \'\';var txtNet=\'\';//\u6a21\u62df\u6307\u6807\u4e0e\u989c\u8272\r\n            var rnd = Math.random() * 4;\r\n            if (rnd > 3)\r\n            {\r\n                color = \'#f8cecc\';\r\n                txtCpu = \'CPU:100%\';\r\n                txtNet = \'\u6d41\u91cf;10M/S\';\r\n            }\r\n            else if (rnd > 2)\r\n            {\r\n                color = \'#fff2cc\';\r\n                txtCpu = \'CPU:50%\';\r\n                txtNet = \'\u6d41\u91cf;5M/S\';\r\n            }\r\n            else if (rnd > 1)\r\n            {\r\n                color = \'#d4e1f5\';\r\n                txtCpu = \'CPU:10%\';\r\n                txtNet = \'\u6d41\u91cf;1M/S\';\r\n            }\r\n            else {\r\n                color = \'#e0f5d7\';\r\n                txtCpu = \'CPU:1%\';\r\n                txtNet = \'\u6d41\u91cf;1M/S\';\r\n            }\r\n\r\n            cell.value = txtNet;\r\n            //cell1.value = txtNet;\r\n            graph.setCellStyles(mxConstants.STYLE_FILLCOLOR, \'white\', [cell]);\r\n            graph.removeCellOverlays(cell);\r\n\r\n            graph.setCellStyles(mxConstants.STYLE_FILLCOLOR, color, [cell]);\r\n            graph.addCellOverlay(cell, createOverlay(graph.warningImage, \'State: \'+color));\r\n\r\n        }\r\n\t\t//\u7ebf\u6761\u6d41\u52a8\u7279\u6548\r\n\t\tfunction lineFlow(model,graph,id) {\r\n            var e2 =  model.getCell(id);//\u62ffxml\u4e2d\u5bf9\u8c61id\r\n            var state = graph.view.getState(e2);\r\n            if(state !=undefined){\r\n                state.shape.node.getElementsByTagName(\'path\')[0].removeAttribute(\'visibility\');\r\n                state.shape.node.getElementsByTagName(\'path\')[0].setAttribute(\'stroke-width\', \'6\');\r\n                state.shape.node.getElementsByTagName(\'path\')[0].setAttribute(\'stroke\', \'lightGray\');\r\n                state.shape.node.getElementsByTagName(\'path\')[1].setAttribute(\'class\', \'flow\');            }\r\n            }\r\n\r\n\t\t//\u8b66\u544a\u56fe\u6807\u95ea\u70c1\u7279\u6548\r\n        function createOverlay(image, tooltip)\r\n\t\t{\r\n\t\t\tvar overlay = new mxCellOverlay(image, tooltip);\r\n\t\t\toverlay.addListener(mxEvent.CLICK, function(sender, evt)\r\n\t\t\t{\r\n\t\t\t\tmxUtils.alert(tooltip + \'\\nLast update: \' + new Date());\r\n\t\t\t});\r\n\t\t\treturn overlay;\r\n\t\t};\r\n\t\tfunction getNewline(val) {\r\n            var str = new String(val);\r\n            //\u5b58\u5728\u6362\u884c\u7b26\u5c31\u76f4\u63a5\u8fd4\u56de\r\n            if(str.indexOf("\\n") != -1){\r\n                return val;\r\n            }\r\n            var bytesCount = 0;\r\n            var s="";\r\n            for (var i = 0 ,n = str.length; i < n; i++) {\r\n                var c = str.charCodeAt(i);\r\n                //\u7edf\u8ba1\u5b57\u7b26\u4e32\u7684\u5b57\u7b26\u957f\u5ea6\r\n                if ((c >= 0x0001 && c <= 0x007e) || (0xff60<=c && c<=0xff9f)) {\r\n                    bytesCount += 1;\r\n                } else {\r\n                    bytesCount += 2;\r\n                }\r\n                //\u6362\u884c\r\n                s += str.charAt(i);\r\n                if(bytesCount>=22){\r\n                    s = s + \'\\n\';\r\n                    //\u91cd\u7f6e\r\n                    bytesCount=0;\r\n                }\r\n            }\r\n            return s;\r\n        }\r\n\r\n\t</script>\r\n<!-- Page passes the container and control to the main function -->\r\n<body onload="main(document.getElementById(\'graphContainer\'));">\r\n\t<!-- Acts as a container for the graph -->\r\n\t<div id="graphContainer" style="overflow:hidden;position:relative;width:861px;height:1100px;cursor:default;">\r\n\t</div>\r\n    <iframe id="ifr_t" style="display:none" src="" width="450" height="320" frameborder="0"></iframe>\r\n   <br>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "24": 1, "25": 21, "26": 21, "27": 22, "28": 22, "29": 24, "30": 24, "31": 25, "32": 25, "33": 26, "34": 26, "35": 27, "36": 27, "37": 28, "38": 28, "39": 29, "40": 29, "41": 30, "42": 30, "43": 31, "44": 31, "45": 39, "46": 39, "47": 61, "48": 61, "49": 107, "50": 107, "56": 50}, "uri": "/monitor_scene/page_query_xml_show.html", "filename": "D:/Users/X230/lanhusaas/framework/templates/monitor_scene/page_query_xml_show.html"}
__M_END_METADATA
"""
