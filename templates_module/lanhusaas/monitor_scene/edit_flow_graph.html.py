# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1559179065.43
_enable_loop = True
_template_filename = 'C:/Users/X230/PycharmProjects/LanhuSaas/framework/templates/monitor_scene/edit_flow_graph.html'
_template_uri = './monitor_scene/edit_flow_graph.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!--[if IE]><meta http-equiv="X-UA-Compatible" content="IE=5,IE=9" ><![endif]-->\r\n<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <title>Grapheditor</title>\r\n\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\r\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">\r\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/styles/grapheditor.css">\r\n\t<script type="text/javascript">\r\n\t\t// Parses URL parameters. Supported parameters are:\r\n\t\t// - lang=xy: Specifies the language of the user interface.\r\n\t\t// - touch=1: Enables a touch-style user interface.\r\n\t\t// - storage=local: Enables HTML5 local storage.\r\n\t\t// - chrome=0: Chromeless mode.\r\n\t\tvar urlParams = (function(url)\r\n\t\t{\r\n\t\t\tvar result = new Object();\r\n\t\t\tvar idx = url.lastIndexOf(\'?\');\r\n\t\t\tif (idx > 0)\r\n\t\t\t{\r\n\t\t\t\tvar params = url.substring(idx + 1).split(\'&\');\r\n\r\n\t\t\t\tfor (var i = 0; i < params.length; i++)\r\n\t\t\t\t{\r\n\t\t\t\t\tidx = params[i].indexOf(\'=\');\r\n\t\t\t\t\tif (idx > 0)\r\n\t\t\t\t\t{\r\n\t\t\t\t\t\tresult[params[i].substring(0, idx)] = params[i].substring(idx + 1);\r\n\t\t\t\t\t}\r\n\t\t\t\t}\r\n\t\t\t}\r\n\t\t\treturn result;\r\n\t\t})(window.location.href);\r\n\t\t// Default resources are included in grapheditor resources\r\n\t\tmxLoadResources = false;\r\n\t\tvar static_url = "')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'";\r\n\t</script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Init.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/deflate/pako.min.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/deflate/base64.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/jscolor/jscolor.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/sanitizer/sanitizer.min.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/../../../src/js/mxClient.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/EditorUi.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Editor.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Sidebar.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Graph.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Format.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Shapes.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Actions.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Menus.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Toolbar.js"></script>\r\n\t<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/js/Dialogs.js"></script>\r\n    <script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/jquery/jquery-3.1.1.min.js"></script>\r\n    <script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/vue.development.js"></script>\r\n    <script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/element-2.4.11/index.js"></script>\r\n    <script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/axios.min.js"></script>\r\n    <script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/csrftoken.js"></script>\r\n</head>\r\n<style>\r\n    .m_i{\r\n        position:absolute;\r\n        margin:auto;\r\n        left:0;\r\n        right:0;\r\n        top:0;\r\n        bottom:0;\r\n        width:650px;\r\n        height:548px;\r\n        z-index:10006;\r\n        background: white;\r\n        border: solid 0.5px gray;\r\n    }\r\n</style>\r\n<body class="geEditor">\r\n    <iframe id="openMonitorItem" class="m_i" width="100%" height="100%" src="')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_item/select_monitor_item/" style="display:none;"></iframe>\r\n\t<script type="text/javascript">\r\n        //csrf\u9a8c\u8bc1\r\n        axios.interceptors.request.use((config) => {\r\n            config.headers[\'X-Requested-With\'] = \'XMLHttpRequest\';\r\n            let regex = /.*csrftoken=([^;.]*).*$/; // \u7528\u4e8e\u4ececookie\u4e2d\u5339\u914d csrftoken\u503c\r\n            config.headers[\'X-CSRFToken\'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];\r\n            return config\r\n        });\r\n        function save_scene_design(name,xml){\r\n            this.myXml = xml;\r\n            axios({\r\n                method: \'post\',\r\n                url: SAVE_URL,\r\n                data: {\r\n                    filename: name,\r\n                    xml: xml\r\n                },\r\n            }).then(function (res) {\r\n                if(res.status == 200){\r\n                    if(res.data.id == \'1\'){\r\n                        // \u4fdd\u5b58\u6210\u529f\u7ed9\u7236\u9875\u9762\u7684\u7f13\u5b58\u91cd\u65b0\u8d4b\u503c\r\n                        window.opener.vm.scene_edit.scene_content =this.myXml;\r\n                        mxUtils.alert("\u573a\u666f\u4fdd\u5b58\u6210\u529f\uff01");\r\n                    }else if(res.data.id != "0"){\r\n                        mxUtils.alert("\u573a\u666f\u540d\u79f0"+"\'"+res.data.id+"\'"+"\u91cd\u590d\uff0c\u8bf7\u91cd\u65b0\u7f16\u8f91\u540e\u518d\u4fdd\u5b58");\r\n                    }else{\r\n                        mxUtils.alert("\u573a\u666f\u540d\u79f0\u4e0d\u5339\u914d\uff0c\u573a\u666f\u6ca1\u6709\u4fdd\u5b58\uff01");\r\n                    }\r\n                }\r\n            })\r\n        }\r\n        // \u6839\u636e\u573a\u666fid \u83b7\u53d6\u53ef\u7f16\u8f91\u573a\u666f\u7684XML\u6587\u6863\uff0c\u751f\u6210\u7f16\u8f91\u6d41\u7a0b\r\n        this.item_id = null;\r\n        this.myXml = null;\r\n        let myNameInput = null;\r\n        let myNames = null;\r\n        let myTexts = null;\r\n        let myValues = null;\r\n        let myForm = null;\r\n        let myAddRemoveButton = null;\r\n        let myEditor = null;\r\n        let myEditorUi = null;\r\n        //\u4fdd\u5b58\u7f16\u6392\u573a\u666f\u7684\u670d\u52a1\u5730\u5740\r\n        window.SAVE_URL = "')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_scene/save/";\r\n        //\u6253\u5f00\u573a\u666f\u9009\u62e9\u5668\uff0c\u9009\u62e9\u8981\u7f16\u8f91\u7684\u573a\u666f\r\n        window.OPEN_FORM = "')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_scene/open/";\r\n        //\u52a0\u8f7d\u53ef\u7f16\u8f91\u7684\u573a\u666f\r\n        window.OPEN_URL = "')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'monitor_scene/open_scene_design/";\r\n        //\u5f39\u51fa\u9009\u62e9\u76d1\u63a7\u9879\u7a97\u53e3\r\n        function open_monitoy_item(nameInput,names,texts,value,form,addRemoveButton){\r\n            $("#openMonitorItem").show();\r\n            myNameInput = nameInput;\r\n            myNames = names;\r\n            myTexts = texts;\r\n            myValues = value;\r\n            myForm = form;\r\n            myAddRemoveButton = addRemoveButton;\r\n        }\r\n\r\n        //lxchun\u5c06\u6d41\u7a0b\u8bbe\u8ba1\u5668\u4e2d\u7684\u5c5e\u6027\u4e0e\u5177\u4f53\u76d1\u63a7\u9879\u5efa\u7acb\u5173\u8054\r\n        function relation_monitor_item_id(item_id,monitor_name){\r\n            //\u76d1\u63a7\u9879\u4e0d\u5141\u8bb8\u91cd\u590d\u5173\u8054\r\n            /*\r\n            if(map.get(item_id)){\r\n                mxUtils.alert("\u76d1\u63a7\u9879"+"\'"+monitor_name+"\'"+"\u5728\u5f53\u524d\u573a\u666f\u4e2d\u5df2\u88ab\u4f7f\u7528\uff0c\u8bf7\u91cd\u65b0\u5173\u8054");\r\n                return false;\r\n            }\r\n            map.set(item_id,monitor_name);*/\r\n            myNameInput.value = "item_id";\r\n            let name = myNameInput.value\r\n            this.item_id = item_id;\r\n            //myNameInput.style.cssText = "display:block;";\r\n            if (name.length > 0 && name != \'label\' && name != \'placeholders\' && name.indexOf(\':\') < 0)\r\n            {\r\n                try\r\n                {\r\n                    var idx = mxUtils.indexOf(myNames, name);\r\n                    if (idx >= 0 && myTexts[idx] != null)\r\n                    {\r\n                        myTexts[idx].value = this.item_id;\r\n                        myTexts[idx].focus();\r\n                    }\r\n                    else\r\n                    {\r\n                        // Checks if the name is valid\r\n                        var clone = myValues.cloneNode(false);\r\n                        clone.setAttribute(name, \'\');\r\n                        if (idx >= 0)\r\n                        {\r\n                            myNames.splice(idx, 1);\r\n                            myTexts.splice(idx, 1);\r\n                        }\r\n                        myNames.push(name);\r\n                        var text = myForm.addTextarea(name + \':\', \'\', 2);\r\n                        text.style.width = \'100%\';\r\n                        myTexts.push(text);\r\n                        text.value = this.item_id;\r\n                        myAddRemoveButton(text, name);\r\n                        text.focus();\r\n                    }\r\n                    myValues.setAttribute("label",monitor_name);\r\n                    myNameInput.value = \'\';\r\n                }\r\n                catch (e)\r\n                {\r\n                    mxUtils.alert(e);\r\n                }\r\n            }\r\n        }\r\n\t\t// Extends EditorUi to update I/O action states based on availability of backend\r\n        //\u521d\u59cb\u5316\u52a0\u8f7d\u7f16\u8f91\u5668\r\n\t\t(function()\r\n\t\t{\r\n\t\t\tvar editorUiInit = EditorUi.prototype.init;\r\n\t\t\t\r\n\t\t\tEditorUi.prototype.init = function()\r\n\t\t\t{\r\n\t\t\t\teditorUiInit.apply(this, arguments);\r\n\t\t\t\tthis.actions.get(\'export\').setEnabled(false);\r\n\r\n\t\t\t\t// Updates action states which require a backend\r\n\t\t\t\tif (!Editor.useLocalStorage)\r\n\t\t\t\t{\r\n\t\t\t\t\t//mxUtils.post(OPEN_URL, \'\', mxUtils.bind(this, function(req)\r\n\t\t\t\t\t//{\r\n\t\t\t\t\t\t//var enabled = req.getStatus() != 404;\r\n\t\t\t\t\t\t//this.actions.get(\'open\').setEnabled(enabled || Graph.fileSupport);\r\n\t\t\t\t\t\t//this.actions.get(\'import\').setEnabled(enabled || Graph.fileSupport);\r\n\t\t\t\t\t\t//this.actions.get(\'save\').setEnabled(enabled);\r\n\t\t\t\t\t\t//this.actions.get(\'saveAs\').setEnabled(enabled);\r\n\t\t\t\t\t\t//this.actions.get(\'export\').setEnabled(enabled);\r\n\t\t\t\t\t//}));\r\n\t\t\t\t}\r\n\t\t\t};\r\n\r\n\t\t\t// Adds required resources (disables loading of fallback properties, this can only\r\n\t\t\t// be used if we know that all keys are defined in the language specific file)\r\n\t\t\tmxResources.loadDefaultBundle = false;\r\n\t\t\tvar bundle = \'')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u"js/mxgraph/examples/grapheditor/www/resources/grapheditor.txt';\r\n\t\t\t// Fixes possible asynchronous requests\r\n\t\t\tmxUtils.getAll([bundle, '")
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/mxgraph/examples/grapheditor/www/styles/default.xml\'], function(xhr)\r\n\t\t\t{\r\n\t\t\t\t// Adds bundle text to resources\r\n\t\t\t\tmxResources.parse(xhr[0].getText());\r\n\t\t\t\t\r\n\t\t\t\t// Configures the default graph theme\r\n\t\t\t\tvar themes = new Object();\r\n\t\t\t\tthemes[Graph.prototype.defaultThemeName] = xhr[1].getDocumentElement(); \r\n\t\t\t\tmyEditor = new Editor(urlParams[\'chrome\'] == \'0\', themes)\r\n\t\t\t\t// Main\r\n\t\t\t\tmyEditorUi = new EditorUi(myEditor);\r\n\t\t\t}, function()\r\n\t\t\t{\r\n\t\t\t\tdocument.body.innerHTML = \'<center style="margin-top:10%;">\u5bfc\u5165\u9519\u8bef\u7684\u8d44\u6e90\u6587\u4ef6.</center>\';\r\n\t\t\t});\r\n\r\n\t\t})();\r\n        var map = new Map();\r\n        window.onload = function(){\r\n\r\n            let xml = null;\r\n            let fileName = null;\r\n            if(window.opener.vm){\r\n                //\u7f16\u8f91\u573a\u666f\r\n                if(window.opener.vm.scene.scene_name == ""){\r\n                    xml = window.opener.vm.scene_edit.scene_content;\r\n                    fileName = window.opener.vm.scene_edit.scene_name;\r\n                }else{\r\n                    //\u65b0\u589e\u573a\u666f\r\n                    fileName = window.opener.vm.scene.scene_name;\r\n                }\r\n                fileName = window.opener.vm.scene.scene_name || window.opener.vm.scene_edit.scene_name;\r\n                myEditor.setFilename(fileName);\r\n            }\r\n            if(xml){\r\n                replaceUpdateXml(xml,fileName);\r\n            }\r\n        }\r\n        //\u5728\u7f16\u8f91\u5668\u52a0\u8f7d\u573a\u666f\r\n        function replaceUpdateXml(xml,fileName){\r\n            // \u8fd9\u6bb5\u4ee3\u7801\u5f88\u91cd\u8981\uff0c\u521d\u59cb\u52a0\u8f7d\u573a\u666f\r\n\t\t\tmyEditorUi.editor.graph.model.beginUpdate();\r\n\t\t\ttry\r\n\t\t\t{\r\n\t\t\t    //\u8bbe\u7f6e\u573a\u666f\u7684\u540d\u79f0\r\n\t\t\t    myEditor.setFilename(fileName);\r\n\t\t\t\tmyEditorUi.editor.setGraphXml(mxUtils.parseXml(xml).documentElement);\r\n\t\t\t\t// LATER: Why is hideDialog between begin-/endUpdate faster?\r\n\t\t\t\tmyEditorUi.hideDialog();\r\n\t\t\t}\r\n\t\t\tcatch (e)\r\n\t\t\t{\r\n\t\t\t\terror = e;\r\n\t\t\t}\r\n\t\t\tfinally\r\n\t\t\t{\r\n\t\t\t\tmyEditorUi.editor.graph.model.endUpdate();\r\n\t\t\t}\r\n        }\r\n\t</script>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "23": 1, "24": 8, "25": 8, "26": 36, "27": 36, "28": 38, "29": 38, "30": 39, "31": 39, "32": 40, "33": 40, "34": 41, "35": 41, "36": 42, "37": 42, "38": 43, "39": 43, "40": 44, "41": 44, "42": 45, "43": 45, "44": 46, "45": 46, "46": 47, "47": 47, "48": 48, "49": 48, "50": 49, "51": 49, "52": 50, "53": 50, "54": 51, "55": 51, "56": 52, "57": 52, "58": 53, "59": 53, "60": 54, "61": 54, "62": 55, "63": 55, "64": 56, "65": 56, "66": 57, "67": 57, "68": 58, "69": 58, "70": 76, "71": 76, "72": 120, "73": 120, "74": 122, "75": 122, "76": 124, "77": 124, "78": 215, "79": 215, "80": 217, "81": 217, "87": 81}, "uri": "./monitor_scene/edit_flow_graph.html", "filename": "C:/Users/X230/PycharmProjects/LanhuSaas/framework/templates/monitor_scene/edit_flow_graph.html"}
__M_END_METADATA
"""
