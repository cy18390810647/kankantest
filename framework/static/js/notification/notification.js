var vue = null;
$(function(){
    var site_url = $('#siteUrl').val();
    //csrf验证
    axios.interceptors.request.use((config) => {
        config.headers['X-Requested-With'] = 'XMLHttpRequest';
        let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
        config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
        return config
    });
    //自定义上限值校验
    const upperLimitCheck= (rule, value, callback) => {
        var lv = $('#lowerValue');
        //如果当前填写了上限值
        if (value != null && value.length > 0) {
            if (parseFloat(value).toString() != "NaN" && parseFloat(value) >= 0 && parseFloat(value) <= 10000) {
                //上限值填写的标记位置true
                vue.upper_valid_status = true;
                lv.focus();
                lv.blur();
                callback();
            } else {
                callback(new Error('上限值在0~10000之间'));
            }
        //如果当前没有填写上限值
        } else {
            //上限值填写的标记位置false
            vue.upper_valid_status = false;
            lv.focus();
            lv.blur();
            callback();
        }
    };
    //自定义下限值校验
    const lowerLimitCheck = (rule, value, callback) => {
        //如果当前填写了下限值
        if (value != null && value.length > 0) {
            var uv = $('#upperValue');
            if (parseFloat(value).toString() != "NaN" && parseFloat(value) >= 0 && parseFloat(value) <= 10000) {
                //判断上限值是否小于下限值
                if(parseFloat(uv.val()) < parseFloat(value)){
                    callback(new Error('上限值不能小于下限值'));
                }else{
                    callback();
                }
            } else {
                callback(new Error('下限值在0~10000之间'));
            }
        //如果当前没有填写下限值
        } else {
            //在上限值也没有填写的情况下报错
            if(!vue.upper_valid_status){
                callback(new Error('上限值与下限值必须选择其一填写'))
            //上限值已经填写的情况下，下限值可以不填写
            }else{
                callback();
            }
        }
    };
    vue = new Vue({
        el: '#alertRuleManage',
        data: {
            //当前用户名称
            currentUser: null,
            //当前处于哪一页
            currentPage: 1,
            //上限值是否验证通过标记
            upper_valid_status: false,
            //下限值是否通过验证标记
            lower_valid_status: false,
            //当前告警规则状态：list列表,edit修改,add添加
            alertRuleTableStatus: 'list',
            //当前告警规则Table所使用的数据集
            alertRuleTableData: null,
            //当前正在添加或修改的告警规则的保存对象
            alertRuleData: {

            },
            //告警规则名称搜索
            ruleSearch: '',
            //当前有多少页
            alertRulesCount: 0,
            //告警规则表单校验
            item_ids:[],
            rules: {
                item_id: [
                    { required: true, message: '请输入监控项ID', trigger: 'blur' },
                    { pattern: /^([1-9]\d{0,2}|1000)$/, message: '监控项ID在1~1000之间', trigger: 'blur' }
                ],
                key_name: [
                    { required: true, message: '请输入告警键值', trigger: 'blur' },
                    { min: 1, max: 50, message: '告警键值长度在1~50之间', trigger: 'blur' }
                ],
                rule_name: [
                    { required: true, message: '请输入规则名称', trigger: 'blur' },
                    { min: 1, max: 50, message: '规则名称长度在1~50之间', trigger: 'blur' }
                ],
                upper_limit: [
                    { validator: upperLimitCheck, trigger: 'blur' }
                ],
                lower_limit: [
                    { validator: lowerLimitCheck, trigger: 'blur' }
                ],
                alert_title: [
                    { required: true, message: '请输入告警标题', trigger: 'blur' },
                    { min: 1, max: 100, message: '告警标题长度在1~100之间', trigger: 'blur' }
                ],
                alert_content: [
                    { required: true, message: '请输入告警内容', trigger: 'blur' },
                    { min: 1, max: 2000, message: '告警内容长度在1~2000之间', trigger: 'blur' }
                ]
            }
        },
        methods: {
            //加载所有告警规则信息--已弃用，改为分页
            loadAlertRuleInfo: function(){
                const loading = this.alertRulePopupLoading();
                //加载告警规则数据
                var url = site_url + 'notification/select_all_rules';
                axios({
                        method: 'post',
                        url: url
                }).then((res) =>{
                    this.alertRuleTableData = res.data.message;
                    loading.close();
                }).catch((res) => {
                    loading.close();
                    var msg = '告警规则数据加载失败！' + res;
                    this.alertRulePopupErrorMessage(msg);
                });
            },
            get_header_data(){
            axios.get(site_url + '/market_day/get_header/').then(function (res) {
               console.log(res)
            })
            },
            //获取当前用户名
            customProcessCurrUser: function(){
                axios({
                    method: 'post',
                    url: site_url + 'position/get_active_user',
                }).then((res) => {
                    this.currentUser=res.data.bk_username
                }).catch((res) => {
                    var msg = '当前用户信息获取失败！';
                    this.alertRulePopupErrorMessage(msg + res);
                });
            },
            //弹出错误信息
            alertRulePopupErrorMessage: function(msg) {
                this.$notify.error({
                  title: '错误',
                  message: msg
                });
            },
            //显示加载中..
            alertRulePopupLoading: function() {
                //返回加载标记，供外部关闭
                return this.$loading({
                    lock: true,
                    text: '正在拼命加载中...',
                    spinner: 'el-icon-loading',
                    background: 'rgba(0, 0, 0, 0.7)'
                });
            },
            //告警规则搜索方法
            alertRuleSearch: function(){
                this.alertRulePageChange(1);
            },
            //显示告警规则添加页面
            alertRuleAdd: function(){
                this.alertRuleTableStatus = 'add';
            },
            //告警规则数据分页获取
            alertRulePageChange: function(page){
                const loading = this.alertRulePopupLoading();
                var data = {
                    search: this.ruleSearch,
                    page: page,
                    limit: 5
                };
                axios({
                    method: 'post',
                    url: site_url + 'notification/select_rules_pagination',
                    data: data
                }).then((res) => {
                    loading.close();
                    //获取当前页的告警规则
                    this.alertRuleTableData = res.data.items;
                    //获取告警规则总页数
                    this.alertRulesCount = res.data.pages;
                    //当前页等于点击的页码
                    this.currentPage = page;
                    //如果当前的页码大于服务端的页码，则将当前页指定为服务端的页面，并获取该页的数据
                    if(page > res.data.pages){
                        this.currentPage = res.data.pages;
                    }
                }).catch((res) => {
                    loading.close();
                    var msg = '告警规则信息加载失败！';
                    this.alertRulePopupErrorMessage(msg + res);
                });
            },
            //告警规则编辑
            alertRuleEdit: function(id){
                const loading = this.alertRulePopupLoading();
                var url = site_url + 'notification/select_rule';
                var editData = {};
                editData.id = id;
                axios({
                    method: 'post',
                    url: url,
                    data: editData,
                }).then((res) =>{
                    loading.close();
                    //获取当前编辑的告警规则信息
                    this.alertRuleData = res.data;
                    //跳转到编辑告警规则页面
                    this.alertRuleTableStatus = 'edit';
                }).catch((res) => {
                    loading.close();
                    var msg = '获取告警规则数据失败！' + res;
                    this.alertRulePopupErrorMessage(msg);
                });
            },
            //告警规则删除
            alertRuleDelete: function(id){
                const loading = this.alertRulePopupLoading();
                this.$confirm('确认删除当前告警规则吗?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning',
                    center: true
                }).then(() => {
                    var url = site_url + 'notification/del_rule';
                    var delData = {};
                    delData.id = id;
                    axios({
                        method: 'post',
                        url: url,
                        data: delData,
                    }).then((res) =>{
                        loading.close();
                        //当服务端返回ok则代表告警规则删除成功
                        if('ok' == res.data.message){
                            this.alertRulePageChange(this.currentPage);
                            this.$message({
                                type: 'success',
                                message: '删除告警规则成功!'
                            });
                        //当服务端返回restrict则代表检测到有用户订阅了该告警规则，需要再次确认是否级联删除
                        }else if('restrict' == res.data.message){
                            this.$confirm('当前告警规则正在被用户使用，强制删除?', '提示', {
                                confirmButtonText: '确定',
                                cancelButtonText: '取消',
                                type: 'warning',
                                center: true
                            }).then(() => {
                                this.alertRuleForceDelete(id);
                            }).catch((res) => {
                                loading.close();
                                this.$message({
                                    type: 'info',
                                    message: '取消告警规则删除，如需继续删除，请先删除用户订阅此告警规则的记录'
                                });
                            });
                        }else{
                            var msg = '请求删除告警规则失败！';
                            this.alertRulePopupErrorMessage(msg + res.data.message);
                        }
                    }).catch((res) => {
                        loading.close();
                        var msg = '请求删除告警规则失败！';
                        this.alertRulePopupErrorMessage(msg + res);
                    });
                }).catch(() => {
                    loading.close();
                    this.$message({
                        type: 'info',
                        message: '取消告警规则删除'
                    });
                });
            },
            //强制删除告警规则
            alertRuleForceDelete: function(id){
                var url = site_url + 'notification/force_del_rule';
                var delData = {};
                delData.id = id;
                const loading = this.alertRulePopupLoading();
                axios({
                    method: 'post',
                    url: url,
                    data: delData,
                }).then((res) =>{
                    loading.close();
                    if('ok' == res.data.message){
                        //获取当前页的告警规则
                        this.alertRulePageChange(this.currentPage);
                        this.$message({
                            type: 'success',
                            message: '删除告警规则成功!'
                        });
                    }
                }).catch((res) => {
                    loading.close();
                    var msg = '删除告警规则失败！' + res;
                    this.alertRulePopupErrorMessage(msg);
                });
            },
            //保存告警规则
            alertRuleSave: function(formName){
                this.$refs[formName].validate((valid) => {
                    if (!valid) {
                        this.$message({
                            type: 'error',
                            message: '请仔细检查表单项!'
                        });
                        return false;
                    }else {
                        //添加告警规则的情况
                        if(this.alertRuleTableStatus == 'add'){
                            this.alertRuleData.create_time = this.dataToString('yyyy-MM-dd hh:mm:ss', new Date());
                            this.alertRuleData.creator = this.currentUser;
                            this.alertRuleData.edit_time = this.dataToString('yyyy-MM-dd hh:mm:ss', new Date());
                            this.alertRuleData.editor = this.currentUser;
                            if('' == this.alertRuleData.upper_limit){
                                this.alertRuleData.upper_limit = null;
                            }
                            if('' == this.alertRuleData.lower_limit){
                                this.alertRuleData.lower_limit = null;
                            }
                        //修改告警规则的情况
                        }else if(this.alertRuleTableStatus == 'edit'){
                            this.alertRuleData.edit_time = this.dataToString('yyyy-MM-dd hh:mm:ss', new Date());
                            this.alertRuleData.editor = this.currentUser;
                            if('' == this.alertRuleData.upper_limit){
                                this.alertRuleData.upper_limit = null;
                            }
                            if('' == this.alertRuleData.lower_limit){
                                this.alertRuleData.lower_limit = null;
                            }
                        }
                        const loading = this.alertRulePopupLoading();
                        var url = site_url + 'notification/add_rule';
                        axios({
                            method: 'post',
                            url: url,
                            data: this.alertRuleData,
                        }).then((res) =>{
                            loading.close();
                            if('ok' == res.data.message){
                                if(this.alertRuleTableStatus == 'edit'){
                                    //如果是修改，完成后跳转到之前的那一页
                                    this.alertRulePageChange(this.currentPage);
                                }else if(this.alertRuleTableStatus == 'add'){
                                    //如果是添加，完成后跳转到最后一页，可以看到自己添加的数据
                                    this.alertRulePageChange(res.data.total_pages);
                                }
                                this.alertRuleList();
                            }else{
                                var msg = '请求添加/修改告警规则失败！';
                                this.alertRulePopupErrorMessage(msg + res);
                            }
                        }).catch((res) => {
                            loading.close();
                            var msg = '请求添加/修改告警规则失败！';
                            this.alertRulePopupErrorMessage(msg + res);
                        });
                    }
                });
            },
            //显示告警规则清单
            alertRuleList: function(){
                this.alertRuleData = {};
                this.alertRuleTableStatus = 'list';
            },
            //Data对象根据表达式转字符串
            dataToString: function(fmt, date) {
                var o = {
                    "M+": date.getMonth() + 1,                 //月份
                    "d+": date.getDate(),                    //日
                    "h+": date.getHours(),                   //小时
                    "m+": date.getMinutes(),                 //分
                    "s+": date.getSeconds(),                 //秒
                    "q+": Math.floor((date.getMonth() + 3) / 3), //季度
                    "S": date.getMilliseconds()             //毫秒
                };
                if (/(y+)/.test(fmt))
                    fmt = fmt.replace(RegExp.$1, (date.getFullYear() + "").substr(4 - RegExp.$1.length));
                for (var k in o)
                    if (new RegExp("(" + k + ")").test(fmt))
                        fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
                return fmt;
            },
            get_all_itemName(){
                axios({
                    method:'get',
                    url:site_url + 'notification/get_all_name',
                }).then(res=> {
                    vue.item_ids=res.data.message
                }).catch(res=>{
                   vue.$alert('获取监控项名称出错！')
                });
            }
        },
        mounted(){
            //页面加载时，首先获取第一页的数据
            this.alertRulePageChange(1);
            this.get_header_data();
            //获取当前用户信息
            this.customProcessCurrUser();
            this.get_all_itemName()
        }
    });
});