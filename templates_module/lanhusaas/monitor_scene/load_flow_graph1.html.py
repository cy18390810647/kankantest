# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1558607282.605
_enable_loop = True
_template_filename = 'C:/Users/X230/PycharmProjects/LanhuSaas/framework/templates/monitor_scene/load_flow_graph1.html'
_template_uri = './monitor_scene/load_flow_graph1.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!--[if IE]><meta http-equiv="X-UA-Compatible" content="IE=5,IE=9" ><![endif]-->\r\n<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <title>\u590d\u6742\u793a\u4f8b</title>\r\n\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\r\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">\r\n    <style type="text/css">\r\n\t\t.flow {\r\n\t\t  stroke-dasharray: 8;\r\n\t\t  animation: dash 0.5s linear;\r\n\t\t  animation-iteration-count: infinite;\r\n\t\t}\r\n\t\t@keyframes dash {\r\n\t\t  to {\r\n\t\t    stroke-dashoffset: -16;\r\n\t\t  }\r\n\t\t}\r\n\t</style>\r\n\t<script type="text/javascript">\r\n\t\tvar static_url = ')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u';\r\n\t</script>\r\n\t<script type="text/javascript" src="')
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
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Shapes.js"></script>\r\n</head>\r\n\t<script type="text/javascript">\r\n\t\t// Extends EditorUi to update I/O action states based on availability of backend\r\n\t\tfunction main(container){\r\n\t\t\tvar graph = new mxGraph(container);\r\n\t\t\tgraph.setTooltips(true);\r\n\t\t\tgraph.setEnabled(false);\r\n\t\t\tmxUtils.get(\'')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/styles/Drawing2.xml\', function(xhr)\r\n\t\t\t{\r\n\t\t\t\tvar xml = xhr.getText();\r\n\t\t\t\tvar doc = mxUtils.parseXml(xml);\r\n\t\t\t\tvar codec = new mxCodec(doc);\r\n\t\t\t\ttry{//\u5c06xml\u4e2d\u7684\u8282\u70b9\u8f6c\u6362\u6210svg\uff0c\u5728\u6d4f\u89c8\u5668\u6e32\u67d3\r\n\t\t\t\t    codec.decode(doc.documentElement, graph.getModel());\r\n                }catch (e) {\r\n                    \r\n                }\r\n                //\u4ee5\u4e0b\u9762\u7279\u6548\r\n\t\t\t\tvar model = graph.getModel();\r\n                setInterval(function(){\r\n                    model.beginUpdate();\r\n                    monitorFlow(model,graph,\'4\',\'5\');monitorFlow(model,graph,\'8\',\'9\');\r\n                    monitorFlow(model,graph,\'16\',\'17\');monitorFlow(model,graph,\'18\',\'19\');\r\n                    monitorFlow(model,graph,\'20\',\'21\');monitorFlow(model,graph,\'22\',\'23\');\r\n                    monitorFlow(model,graph,\'24\',\'25\');monitorFlow(model,graph,\'41\',\'42\');\r\n                    monitorFlow(model,graph,\'29\',\'40\');monitorFlow(model,graph,\'37\',\'38\');\r\n                   model.endUpdate();\r\n                } ,3000);\r\n\r\n                   lineFlow(model,graph,\'10\');lineFlow(model,graph,\'11\');\r\n\t\t\t\t   lineFlow(model,graph,\'26\');lineFlow(model,graph,\'27\');\r\n\t\t\t\t   lineFlow(model,graph,\'29\');lineFlow(model,graph,\'30\');\r\n\t\t\t\t   lineFlow(model,graph,\'31\');lineFlow(model,graph,\'32\');\r\n\t\t\t\t   lineFlow(model,graph,\'33\');lineFlow(model,graph,\'34\');\r\n\t\t\t\t   lineFlow(model,graph,\'35\');lineFlow(model,graph,\'36\');\r\n\t\t\t\t   lineFlow(model,graph,\'47\');lineFlow(model,graph,\'48\');\r\n\t\t\t\t   lineFlow(model,graph,\'44\');\r\n\t\t\t\t   for(key_index in model.cells){\r\n\t\t\t\t       var cell = model.cells[key_index];\r\n\t\t\t\t       if(cell.attribute!=""\r\n                          &&cell.attribute!=undefined){\r\n                           var x = cell.geometry.x;\r\n                           var y = cell.geometry.y;\r\n                           var ifr= document.getElementById("ifr_t");\r\n                           ifr.src = cell.attribute;\r\n                           ifr.style.position="absolute";\r\n                           ifr.style.left=x+"px";\r\n                           ifr.style.top= y+"px";\r\n                           ifr.style.display="block";\r\n                           break;\r\n                       }\r\n                   }\r\n\t\t\t\t  // cell = model.getCell(\'49\')\r\n\r\n                  // cell.attribute\r\n\t\t\t}, function()\r\n\t\t\t{\r\n\t\t\t\tdocument.body.innerHTML = \'<center style="margin-top:10%;">Error loading resource files. Please check browser console.</center>\';\r\n\t\t\t});\r\n\t\t}\r\n\t\t//\u76d1\u63a7\u9879\u7279\u6548\r\n        function monitorFlow(model,graph,id,id1) {\r\n            var cell = model.getCell(id);//\u62ffxml\u4e2d\u5bf9\u8c61id\r\n            var cell1 = model.getCell(id1);//\u62ffxml\u4e2d\u5bf9\u8c61id\r\n            var color = \'\';var txtCpu = \'\';var txtNet=\'\';//\u6a21\u62df\u6307\u6807\u4e0e\u989c\u8272\r\n            var rnd = Math.random() * 4;\r\n            if (rnd > 3)\r\n            {\r\n                color = \'#f8cecc\';\r\n                txtCpu = \'CPU:100%\';\r\n                txtNet = \'\u6d41\u91cf;10M/S\';\r\n            }\r\n            else if (rnd > 2)\r\n            {\r\n                color = \'#fff2cc\';\r\n                txtCpu = \'CPU:50%\';\r\n                txtNet = \'\u6d41\u91cf;5M/S\';\r\n            }\r\n            else if (rnd > 1)\r\n            {\r\n                color = \'#d4e1f5\';\r\n                txtCpu = \'CPU:10%\';\r\n                txtNet = \'\u6d41\u91cf;1M/S\';\r\n            }\r\n            else {\r\n                color = \'#e0f5d7\';\r\n                txtCpu = \'CPU:1%\';\r\n                txtNet = \'\u6d41\u91cf;1M/S\';\r\n            }\r\n\r\n            cell.value = txtNet;\r\n            //cell1.value = txtNet;\r\n            graph.setCellStyles(mxConstants.STYLE_FILLCOLOR, \'white\', [cell]);\r\n            graph.removeCellOverlays(cell);\r\n\r\n            graph.setCellStyles(mxConstants.STYLE_FILLCOLOR, color, [cell]);\r\n            graph.addCellOverlay(cell, createOverlay(graph.warningImage, \'State: \'+color));\r\n\r\n        }\r\n\t\t//\u7ebf\u6761\u6d41\u52a8\u7279\u6548\r\n\t\tfunction lineFlow(model,graph,id) {\r\n            var e2 =  model.getCell(id);//\u62ffxml\u4e2d\u5bf9\u8c61id\r\n            var state = graph.view.getState(e2);\r\n            state.shape.node.getElementsByTagName(\'path\')[0].removeAttribute(\'visibility\');\r\n            state.shape.node.getElementsByTagName(\'path\')[0].setAttribute(\'stroke-width\', \'6\');\r\n            state.shape.node.getElementsByTagName(\'path\')[0].setAttribute(\'stroke\', \'lightGray\');\r\n            state.shape.node.getElementsByTagName(\'path\')[1].setAttribute(\'class\', \'flow\');\r\n        }\r\n\r\n\t\t//\u8b66\u544a\u56fe\u6807\u95ea\u70c1\u7279\u6548\r\n        function createOverlay(image, tooltip)\r\n\t\t{\r\n\t\t\tvar overlay = new mxCellOverlay(image, tooltip);\r\n\t\t\toverlay.addListener(mxEvent.CLICK, function(sender, evt)\r\n\t\t\t{\r\n\t\t\t\tmxUtils.alert(tooltip + \'\\nLast update: \' + new Date());\r\n\t\t\t});\r\n\t\t\treturn overlay;\r\n\t\t};\r\n\t</script>\r\n<!-- Page passes the container and control to the main function -->\r\n<body onload="main(document.getElementById(\'graphContainer\'));">\r\n <!-- Acts as a container for the graph -->\r\n\t<div id="graphContainer" style="overflow:hidden;position:relative;width:1100px;height:886px;cursor:default;">\r\n\t</div>\r\n     <iframe id="ifr_t" style="display:none" src="" width="450" height="300" frameborder="0"></iframe>\r\n\t<br>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 26, "33": 27, "34": 27, "35": 28, "36": 28, "37": 29, "38": 29, "39": 37, "40": 37, "46": 40, "16": 0, "22": 1, "23": 21, "24": 21, "25": 23, "26": 23, "27": 24, "28": 24, "29": 25, "30": 25, "31": 26}, "uri": "./monitor_scene/load_flow_graph1.html", "filename": "C:/Users/X230/PycharmProjects/LanhuSaas/framework/templates/monitor_scene/load_flow_graph1.html"}
__M_END_METADATA
"""
