# -*- coding: utf-8 -*-
# @Time    : 2022-05-25 14:40
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : send_msg.py 
# @Software: PyCharm


class Send:

    def SeverityLevelBug(self, severity_bugs):
        """
        获取到各严重等级下bug数量以人员区分
        :param severity_bugs: 以严重等级区分的bug
        :return:
        """
        qywx_bug_content = []
        for person in range(len(severity_bugs)):
            assigned_bug = \
            '''<font color=\\"comment\\">{assignedto_bug}</font>(<font color=\\"warning\\">{assignedto_bugs_total}</font>):\n'''\
                               .format(assignedto_bug=severity_bugs[person]["assignedTo"],
                                       assignedto_bugs_total=severity_bugs[person]["assignedto_bugs_total"]),
            qywx_bug_content += assigned_bug
            person_bug = severity_bugs[person]["assignedto_bug"]
            for bug_detail in range(len(person_bug)):
                qywx_bug = "[{bug_title}](http://chandao.idmakers.cn/zentao/bug-view-{bug_id}.html)\n"\
                    .format(bug_title=person_bug[bug_detail]["bug_title"], bug_id=person_bug[bug_detail]["bug_id"])
                qywx_bug_content.append(qywx_bug)
        return qywx_bug_content


    def replace_bug(self, bug):
        """
        为了配合企业微信消息推送markdown格式，对格式进行统一替换
        :param bug:
        :return:
        """
        return str(bug).replace("', '", "").replace("['", "").replace("']", "")


    def BugsCotent(self, unresolvedbugs):
        """
        获取未关闭的bug数据，并通过项目id进行区分
        :param unresolvedbugs:
        :return:
        """
        projectcontent = []
        for project in range(len(unresolvedbugs)):
            project_id = unresolvedbugs[project]["project_id"]
            project_bugs = unresolvedbugs[project]["project_bug_count"]
            severitybugs = unresolvedbugs[project]["bug"]
            for severity_bug in range(len(severitybugs)):
                severity_lev = severitybugs[severity_bug]["severity_lev"]
                severity_bugs = severitybugs[severity_bug]["severity_bug"]
                severity_lev1 = 0
                severity_lev2 = 0
                severity_lev3 = 0
                severity_lev4 = 0
                severity_lev1_bugs = "无"
                severity_lev2_bugs = "无"
                severity_lev3_bugs = "无"
                severity_lev4_bugs = "无"
                if severity_lev == "1":
                    severity_lev1 = severity_lev
                    severity_lev1_bugs = self.replace_bug(self.SeverityLevelBug(severity_bugs))
                elif severity_lev == "2":
                    severity_lev2 = severity_lev
                    severity_lev2_bugs = self.replace_bug(self.SeverityLevelBug(severity_bugs))
                elif severity_lev == "3":
                    severity_lev3 = severity_lev
                    severity_lev3_bugs = self.replace_bug(self.SeverityLevelBug(severity_bugs))
                elif severity_lev == "4":
                    severity_lev4 = severity_lev
                    severity_lev4_bugs = self.replace_bug(self.SeverityLevelBug(severity_bugs))
                content = '''<font color=\"info\">{project_id}</font>\n
                            >未解决BUG:<font color=\"warning\">{project_bugs}</font>\n
                            >各严重等级BUG数量:
                            >一级bug：<font color=\"warning\">{severity_lev1}</font>:\n{severity_lev1_bugs}
                            >二级bug：<font color=\"warning\">{severity_lev2}</font>:\n{severity_lev2_bugs}
                            >三级bug：<font color=\"warning\">{severity_lev3}</font>:\n{severity_lev3_bugs}
                            >四级bug：<font color=\"warning\">{severity_lev4}</font>:\n{severity_lev4_bugs}
                            ''' \
                    .format(project_id=project_id, project_bugs=project_bugs,
                            severity_lev1=severity_lev1, severity_lev1_bugs=severity_lev1_bugs,
                            severity_lev2=severity_lev2, severity_lev2_bugs=severity_lev2_bugs,
                            severity_lev3=severity_lev3, severity_lev3_bugs=severity_lev3_bugs,
                            severity_lev4=severity_lev4, severity_lev4_bugs=severity_lev4_bugs,
                            )
                projectcontent.append(content)
        return projectcontent


if __name__ == '__main__':
    s = Send()
    t = [{"project_id":"18","project_bug_count":2,"bug":[{"severity_lev":"2","severity_bug_count":2,"severity_bug":[{"assignedTo":"tianye","assignedto_bugs_total":2,"assignedto_bug":[{"bug_id":"2837","bug_title":"V-1.0.0：蜂巢APP登录首页，要求登录功能增加个防抖机制。"},{"bug_id":"2938","bug_title":"V-1.0.0：审批元应用，需求规定会签审批，如果是有多个审批人，必须所有人审批通过才算通过，目前一个人审批通过单据就通过审批了。"}]}]}]},{"project_id":"19","project_bug_count":32,"bug":[{"severity_lev":"2","severity_bug_count":10,"severity_bug":[{"assignedTo":"tianye","assignedto_bugs_total":10,"assignedto_bug":[{"bug_id":"2940","bug_title":"V-1.0.0：报表弹框中有数据的时候，会将关闭/确定功能键给挤出弹框。"},{"bug_id":"2946","bug_title":"V-1.0.0：3D工厂后台设置→dcs设置界面，选择【篦冷机】页面后，无限点击节点的添加功能键会导致页面结构错乱。"},{"bug_id":"2947","bug_title":"V-1.0.0：3D工厂后台设置→dcs设置界面，在【篦冷机】页面联系点击【添加节点】功能键，无限新增无名称节点。"},{"bug_id":"2948","bug_title":"V-1.0.0：3D工厂后台设置→dcs设置界面，在【篦冷机】页面添加标记点弹框。标记点数量无限制。当标记点数量较大时客户端会崩溃。"},{"bug_id":"2949","bug_title":"V-1.0.0：3D工厂，左边视频窗口点击全屏无任何反应(无遮挡)。"}]},{"assignedTo":"zhangfan","assignedto_bugs_total":10,"assignedto_bug":[{"bug_id":"2927","bug_title":"V-1.0.0：右侧报表全屏，点击新增新增数据弹出新增数据弹框，填写好所有信息点击确定表单提交失败，报SQL错误。"},{"bug_id":"2928","bug_title":"V-1.0.0：在右侧报表全屏界面，手动添加报表后新增报表未展示。取消全屏后报表正常展示出来。"},{"bug_id":"4390","bug_title":"【生成大数据】生产大数据（一二线）总计21个节点共494个传感器，其中165个传感器实时数据值为0，109个历史数据值为0"},{"bug_id":"4391","bug_title":"【视频监控】视频监控22未显示"},{"bug_id":"4392","bug_title":"【VR视图】VR视图里面，传感器无数据时，显示实时数据空白页面"}]}]},{"severity_lev":"3","severity_bug_count":22,"severity_bug":[{"assignedTo":"zhangfan","assignedto_bugs_total":22,"assignedto_bug":[{"bug_id":"3839","bug_title":"【生产大数据】水泥库(一线)，设备详情查看历史数据，选择2月10-3月10，提示网络异常。"},{"bug_id":"3841","bug_title":"【生产大数据】首页中点击流程查看详情状态都显示为0，点击某一项数据查看状态相关显示不为0。"},{"bug_id":"3842","bug_title":"【生产大数据】单一设备描述数据为0，但是点击查看详情，数据不为0。"},{"bug_id":"3843","bug_title":"【生产大数据】某一流程中存在多页设备时，滑动到第二页打开设备查看，页面又默认显示到第一页的设备。"},{"bug_id":"3870","bug_title":"【生产大数据】回转窑(二线)，高温风机前轴承Y向震动，图表和文字描述数据不一样，见图。"},{"bug_id":"3873","bug_title":"【生产大数据】蓖麻床2段篦床压力显示为m。"},{"bug_id":"3881","bug_title":"【生产大数据】页面操作点击的过程中，出现页面报错的情况，偶现问题，见图，"},{"bug_id":"3883","bug_title":"【生产大数据】原料粉磨（二线），2号磨头进风口压力图表与描述数据不一致，见图。"},{"bug_id":"3890","bug_title":"【生产大数据】原料粉磨，电动百叶阀加载失败，见图。"},{"bug_id":"4000","bug_title":"【视频监控】视频监控首页点击下方的环节，提示“请输入视频url”"},{"bug_id":"4003","bug_title":"【搜索】选择搜索类型，查询的数据有误。"},{"bug_id":"4004","bug_title":"首页输入报表数据类型，点击搜索，未搜索出数据。"},{"bug_id":"4009","bug_title":"【生产大数据】回转窑一线，窑主电机，窑主电机速度反馈，窑主传动电机电流都是显示温度单位。"},{"bug_id":"4012","bug_title":"【生产大数据】原料粉磨（二线），1号磨头冷风阀门电动执行器阀门数据显示为‘1.861’，其他反馈数据都带%。"},{"bug_id":"4013","bug_title":"【生产大数据】原料粉磨（二线），排风机电机，设备列表和设备详情显示的设备数量不同。"},{"bug_id":"4014","bug_title":"【生产大数据】原料粉磨（二线），3号提升机主机，电流显示为0A，图表显示36A。"},{"bug_id":"4018","bug_title":"【3D大数据】回转窑一线-窑主电机，传动电机电流显示为温度。"},{"bug_id":"4019","bug_title":"【生产大数据】生产窑一线-窑头引风机，引风机振动数据无单位。"},{"bug_id":"4020","bug_title":"【生产大数据】回转窑一线-布袋收尘进口，展示数据无单位。"},{"bug_id":"4021","bug_title":"【生产大数据】原料粉磨（一线），页面下设备列表向右滑动时，无法滑动到最后一个设备。"},{"bug_id":"4022","bug_title":"【3D--设置】原料粉磨（一线）部分设备点击打开数据展示信息如图所示。"},{"bug_id":"4023","bug_title":"【生产大数据】石膏混合材破碎和输送--带式输送机，42.05带式输送机电流未显示单位。"}]}]}]},{"project_id":"20","project_bug_count":59,"bug":[{"severity_lev":"1","severity_bug_count":18,"severity_bug":[{"assignedTo":"gaoyaqin","assignedto_bugs_total":18,"assignedto_bug":[{"bug_id":"586","bug_title":"V3-【我查收的】-【移动】移动界面新增文件夹时点击确定按钮无反应"},{"bug_id":"590","bug_title":"V3-【文件传阅】进入文件传阅时显示提示信息‘接口成功数据异常’提示信息"},{"bug_id":"593","bug_title":"V3-所有二级页面无法进入"}]},{"assignedTo":"lizhi","assignedto_bugs_total":18,"assignedto_bug":[{"bug_id":"225","bug_title":"V1-[个人中心]首页文案错误，姓名写成了性名"},{"bug_id":"238","bug_title":"V1-[个人中心]系统设置中的所有功能点击无反应"},{"bug_id":"239","bug_title":"V1-[个人中心]个人中心首页UI布局不美观"},{"bug_id":"243","bug_title":"V1-[数据中心]点击首页‘搜索’按钮跳转页面错误"},{"bug_id":"244","bug_title":"V1-[数据中心]首页“设置”按钮点击无反应"},{"bug_id":"245","bug_title":"V1-[数据中心]点击首页顶部的“编辑”按钮无反应"},{"bug_id":"344","bug_title":"V2-[数据中心]不能退出数据魔方页面"},{"bug_id":"345","bug_title":"V2-[数据中心] 数据 分析未完成功能"},{"bug_id":"420","bug_title":"报表偏好设置未实现"},{"bug_id":"588","bug_title":"V3-【数据魔方】/【数据可视化】页面内容为空"},{"bug_id":"592","bug_title":"V3-【数据中心】部分添加报表按钮点击无反应"}]},{"assignedTo":"zhangxiaoqiong","assignedto_bugs_total":18,"assignedto_bug":[{"bug_id":"567","bug_title":"V3-文件包预览时文件时无文件显示"},{"bug_id":"578","bug_title":"V3-【云盘管理】-【分享文件】分享文件成功后无提示信息，并且接收人【消息中心】-【提醒】中无提醒信息（云盘也未接收到分享的文件）"},{"bug_id":"595","bug_title":"V3-【我分享的】删除列表内容删除失败并且无提示信息"},{"bug_id":"601","bug_title":"V3-【发起传阅】通过云盘添加文件，接口改变未更新"}]}]},{"severity_lev":"2","severity_bug_count":12,"severity_bug":[{"assignedTo":"","assignedto_bugs_total":12,"assignedto_bug":[{"bug_id":"599","bug_title":"V3-【云盘管理】切换界面时列表显示的数据错误"}]},{"assignedTo":"gaoyaqin","assignedto_bugs_total":12,"assignedto_bug":[{"bug_id":"330","bug_title":"V2-注册界面中点击手机号底部上滑纯字母键盘"},{"bug_id":"332","bug_title":"V2-注册界面中的职位文本框点击时底部上滑字母键盘与需求不一致"},{"bug_id":"334","bug_title":"V2-注册界面输入键盘遮挡密码文本框"},{"bug_id":"557","bug_title":"V3-tab上应用图标未显示"},{"bug_id":"582","bug_title":"V3-【文件传阅】发起传阅成功后，【我发起的】列表中未显示该信息（原生未回调）"}]},{"assignedTo":"lizhi","assignedto_bugs_total":12,"assignedto_bug":[{"bug_id":"589","bug_title":"V3-【偏好设置】数据中心首页展示的数据与偏好设置中设置的不一致"},{"bug_id":"591","bug_title":"V3-【数据中心】首页部分图表为空（无数据时隐藏）"}]},{"assignedTo":"zhangxiaoqiong","assignedto_bugs_total":12,"assignedto_bug":[{"bug_id":"577","bug_title":"【云盘管理】-【分享文件】分享人是通过组织机构进行选择的，请参照原型图（文件传阅选择传阅人时存在同样问题）"},{"bug_id":"602","bug_title":"V3-【文件传阅】-【我发起的】撤回消息成功后页面未刷新并且无提示信息"},{"bug_id":"608","bug_title":"V3-【云盘管理】/【文件传阅】搜索条件与搜索结果不匹配"},{"bug_id":"610","bug_title":"V3-【云盘管理】删除【我分享的】/【我查收的】列表信息时【云盘】列表中的信息也会被删除（退出重新进入首次操作删除不会出现这种状况）"}]}]},{"severity_lev":"3","severity_bug_count":28,"severity_bug":[{"assignedTo":"gaoyaqin","assignedto_bugs_total":28,"assignedto_bug":[{"bug_id":"333","bug_title":"V2-注册界面有上滑键盘时再点击部门文本框上滑键盘未收回"},{"bug_id":"335","bug_title":"V2-输入非法手机号注册时提交注册信息提示信息已存在号码"},{"bug_id":"336","bug_title":"V2-注册界面手机号字段未做限制"},{"bug_id":"337","bug_title":"V2-注册界面未满足约束条件"},{"bug_id":"338","bug_title":"V2-注册成功后无提示信息"},{"bug_id":"339","bug_title":"V2-注册失败时显示的提示信息错误"},{"bug_id":"340","bug_title":"V2-点击注册界面的‘返回登录’界面时字体无变化"},{"bug_id":"341","bug_title":"V2-打开掌阅APP时无启动页"},{"bug_id":"342","bug_title":"V2-登录界面中的立即注册按钮点击时无点击效果"},{"bug_id":"343","bug_title":"验证登录成功后下次进入系统是否自动登录"},{"bug_id":"548","bug_title":"tab栏图标应以图标加文字方式展示"},{"bug_id":"561","bug_title":"V3-切换元应用时会闪现登录界面背景图"}]},{"assignedTo":"lizhi","assignedto_bugs_total":28,"assignedto_bug":[{"bug_id":"237","bug_title":"V1-[个人中心]点击帮助文档进入个人主页"},{"bug_id":"240","bug_title":"V1-[个人中心]首页中不可点击选择的字段标识可点击选择"},{"bug_id":"373","bug_title":"数据中心接口调整"},{"bug_id":"374","bug_title":"数据中心界面调整"},{"bug_id":"375","bug_title":"在iOS中数据可视化不能退出"},{"bug_id":"528","bug_title":"数据中心-获取报表类别接口错误"},{"bug_id":"547","bug_title":"tab栏的所有图标重叠"},{"bug_id":"549","bug_title":"所有界面字体与设计文件字体一致"},{"bug_id":"551","bug_title":"文件传阅界面问题"},{"bug_id":"552","bug_title":"消息中心页面调整"},{"bug_id":"553","bug_title":"发起文件传阅"},{"bug_id":"554","bug_title":"文件传阅-搜索框与返回按键间距过大"},{"bug_id":"555","bug_title":"公告-发起公告页面问题"},{"bug_id":"568","bug_title":"云盘管理-操作按钮显示问题"},{"bug_id":"571","bug_title":"云盘管理-添加文件夹弹窗"},{"bug_id":"573","bug_title":"搜索界面问题"}]}]},{"severity_lev":"4","severity_bug_count":1,"severity_bug":[{"assignedTo":"gaoyaqin","assignedto_bugs_total":1,"assignedto_bug":[{"bug_id":"246","bug_title":"V1-tab上选中的元应用和未选中元应用图标状态与需求不一致"}]}]}]},{"project_id":"22","project_bug_count":7,"bug":[{"severity_lev":"1","severity_bug_count":4,"severity_bug":[{"assignedTo":"lizhi","assignedto_bugs_total":4,"assignedto_bug":[{"bug_id":"346","bug_title":"V1-[数据中心后台] 数据管理-删除数据关系不成功"},{"bug_id":"351","bug_title":"V1-[数据中心后台] 数据管理删除功能需要对接接口"},{"bug_id":"367","bug_title":"V1-[数据中心] 看板编辑出现404"},{"bug_id":"372","bug_title":"看板编辑-背景添加成功后刷新页面就不见了"}]}]},{"severity_lev":"3","severity_bug_count":3,"severity_bug":[{"assignedTo":"lizhi","assignedto_bugs_total":3,"assignedto_bug":[{"bug_id":"370","bug_title":"编辑看板时不能添加容器背景图"},{"bug_id":"371","bug_title":"看板预览没显示实时数据"},{"bug_id":"379","bug_title":"三线生产日统计、典型生产成本产考没数据显示"}]}]}]},{"project_id":"26","project_bug_count":1,"bug":[{"severity_lev":"2","severity_bug_count":1,"severity_bug":[{"assignedTo":"tianye","assignedto_bugs_total":1,"assignedto_bug":[{"bug_id":"2887","bug_title":"V-1.0.0：分类界面，新增分类后，排序会变得混乱。要求排序按照时间顺序，反序排序。"}]}]}]},{"project_id":"28","project_bug_count":2,"bug":[{"severity_lev":"2","severity_bug_count":2,"severity_bug":[{"assignedTo":"tianye","assignedto_bugs_total":2,"assignedto_bug":[{"bug_id":"2959","bug_title":"V-1.0.0：审批元应用，审批中的单据在单据详情中展示状态为待审批。"}]},{"assignedTo":"zhouzhenhua","assignedto_bugs_total":2,"assignedto_bug":[{"bug_id":"2969","bug_title":"V-1.0.0：现在为待收货的单据确认收货后，无论是否发货完成单据直接变更为完成状态。需求规定，状态为收货中的单据如果发货未完成，确认收货后单据状态依然为发货中。"}]}]}]},{"project_id":"29","project_bug_count":1,"bug":[{"severity_lev":"2","severity_bug_count":1,"severity_bug":[{"assignedTo":"tianye","assignedto_bugs_total":1,"assignedto_bug":[{"bug_id":"2937","bug_title":"V-1.0.0：创建移库单后立即对货品进行盘点，盘点过后继续执行移库操作，移出会失败，提示:移出出错。"}]}]}]},{"project_id":"30","project_bug_count":3,"bug":[{"severity_lev":"2","severity_bug_count":3,"severity_bug":[{"assignedTo":"tianye","assignedto_bugs_total":3,"assignedto_bug":[{"bug_id":"2901","bug_title":"V-1.0.0：申领单据指定人代领，申领出库流程完成后，申领单状态未发生任何变更。(目前单据无法完成)"}]},{"assignedTo":"zch","assignedto_bugs_total":3,"assignedto_bug":[{"bug_id":"2900","bug_title":"V-1.0.0：申购单审核通过后点击【确认结束单据】并确定。在采购系统新增采购计划弹框-计划单据中无法查到该单据。"}]},{"assignedTo":"zhouzhenhua","assignedto_bugs_total":3,"assignedto_bug":[{"bug_id":"2902","bug_title":"V-1.0.0：申领单已经有人审批完成，但未完成审批，状态未变更为审核中。"}]}]}]},{"project_id":"33","project_bug_count":28,"bug":[{"severity_lev":"1","severity_bug_count":4,"severity_bug":[{"assignedTo":"zhangfan","assignedto_bugs_total":4,"assignedto_bug":[{"bug_id":"3040","bug_title":"【IC卡办理】进入IC卡关联页面，提示硬件officeofbill占用"}]},{"assignedTo":"zhouzhenhua","assignedto_bugs_total":4,"assignedto_bug":[{"bug_id":"3025","bug_title":"【出厂】车辆节点切换为出厂操作成功，该订单仍未出发货区状态；出厂后IC卡已解绑车辆，再次进厂未绑定IC卡可进入"},{"bug_id":"3055","bug_title":"【排队发运】车辆进厂后，绑定订单后，审核通过该订单，车辆未进入排队状态"},{"bug_id":"3059","bug_title":"【排队等待】车辆进入等待区且小于车限，未进入呼叫区，一致处于等待区"}]}]},{"severity_lev":"2","severity_bug_count":16,"severity_bug":[{"assignedTo":"zhangfan","assignedto_bugs_total":16,"assignedto_bug":[{"bug_id":"3037","bug_title":"【修改IC卡】修改IC卡，修改卡编号后提交，提示访问异常"}]},{"assignedTo":"zhouzhenhua","assignedto_bugs_total":16,"assignedto_bug":[{"bug_id":"2985","bug_title":"【待一次重待二次重出厂】通过已存在车牌号进行查询失败"},{"bug_id":"3003","bug_title":"【车辆超时】设置车辆超时时间后，等待车辆超时，车辆未跳转且无记录"},{"bug_id":"3006","bug_title":"【发货区】发货区车辆未显示，品种车辆限制数据为空"},{"bug_id":"3012","bug_title":"【排队发运】切换订单状态提示异常"},{"bug_id":"3014","bug_title":"【提货检斤单补打】查询功能无效"},{"bug_id":"3016","bug_title":"【切换提单】切换提单，提示访问异常"},{"bug_id":"3020","bug_title":"【IC卡补卡】进行换卡时，无法识别卡号"},{"bug_id":"3028","bug_title":"【排队车限维护】车辆限制输入超长、小数数据，系统提示异常"},{"bug_id":"3033","bug_title":"【排队优先设置】客户优先级输入小数提示异常"},{"bug_id":"3039","bug_title":"【IC卡注册】IC卡编号查询无效，输入非数字字符提示异常"},{"bug_id":"3046","bug_title":"【一次重】袋装提单通过袋装一次重接口，提示操作成功，状态实际未修改"},{"bug_id":"3048","bug_title":"【待一次重待二次重出厂】车单分离成功后，数据未消失"},{"bug_id":"3049","bug_title":"【新建提单】车辆已出厂，新建提单，提示已开其他袋装提单"},{"bug_id":"3052","bug_title":"【呼叫】手动呼叫车辆，提示访问异常"},{"bug_id":"3058","bug_title":"【IC卡绑定】袋装IC卡绑定散装订单车辆操作成功"}]}]},{"severity_lev":"3","severity_bug_count":8,"severity_bug":[{"assignedTo":"zhangfan","assignedto_bugs_total":8,"assignedto_bug":[{"bug_id":"2990","bug_title":"【系统配置】回空车值设置(吨)为空、中文、英文字母大小写，其他符号提示接口访问异常"}]},{"assignedTo":"zhouzhenhua","assignedto_bugs_total":8,"assignedto_bug":[{"bug_id":"2986","bug_title":"【待一次重待二次重出厂】进行数据查询是，日期只选择起始日期"},{"bug_id":"2987","bug_title":"【待一次重待二次重出厂】进行数据查询是，日期只选择截止日期"},{"bug_id":"3009","bug_title":"【排队发运】通过接口添加4辆进门车辆，未绑定订单，展示错误"},{"bug_id":"3023","bug_title":"【一次重】车辆过一次重后，再次通过该节点提示信息不明确"},{"bug_id":"3047","bug_title":"【待一次重待二次重出厂】已出厂车辆不显示该订单"},{"bug_id":"3053","bug_title":"【车辆进出门查询】未显示出门时间，车辆状态正确标识"},{"bug_id":"3054","bug_title":"【车辆黑名单】车辆黑名单修改后，未记录修改时间与修改人员"}]}]}]},{"project_id":"36","project_bug_count":1,"bug":[{"severity_lev":"3","severity_bug_count":1,"severity_bug":[{"assignedTo":"zhuzihao","assignedto_bugs_total":1,"assignedto_bug":[{"bug_id":"6888","bug_title":"【查看】查看页面，仍可执行删除调度员"}]}]}]},{"project_id":"37","project_bug_count":2,"bug":[{"severity_lev":"3","severity_bug_count":2,"severity_bug":[{"assignedTo":"zhangfan","assignedto_bugs_total":2,"assignedto_bug":[{"bug_id":"5918","bug_title":"经营大屏 原材料及生料模块 选择二线后，页面数据折线显示不全"},{"bug_id":"5919","bug_title":"【生产大屏】无法切换到年，切换月份时，未显示对应月份的产量数据"}]}]}]},{"project_id":"43","project_bug_count":1,"bug":[{"severity_lev":"3","severity_bug_count":1,"severity_bug":[{"assignedTo":"zhangfan","assignedto_bugs_total":1,"assignedto_bug":[{"bug_id":"5007","bug_title":"【视频监控】长时间播放出现崩溃的情况"}]}]}]},{"project_id":"45","project_bug_count":1,"bug":[{"severity_lev":"3","severity_bug_count":1,"severity_bug":[{"assignedTo":"zhangfan","assignedto_bugs_total":1,"assignedto_bug":[{"bug_id":"5812","bug_title":"【我的应用】【更新】更新应用时最好显示应用名称"}]}]}]},{"project_id":"47","project_bug_count":1,"bug":[{"severity_lev":"3","severity_bug_count":1,"severity_bug":[{"assignedTo":"chenzhuo","assignedto_bugs_total":1,"assignedto_bug":[{"bug_id":"5452","bug_title":"【产量】-【报表】-报表页面少一列余热发电"}]}]}]},{"project_id":"49","project_bug_count":2,"bug":[{"severity_lev":"2","severity_bug_count":1,"severity_bug":[{"assignedTo":"lilingyu","assignedto_bugs_total":1,"assignedto_bug":[{"bug_id":"5936","bug_title":"【登录】未配置账号菜单权限，仍显示了所有菜单"}]}]},{"severity_lev":"3","severity_bug_count":1,"severity_bug":[{"assignedTo":"shenchenglu","assignedto_bugs_total":1,"assignedto_bug":[{"bug_id":"6038","bug_title":"【多通道监测】选择对应的站点后，对收音机进行的打分时，报参数错误（请求参数缺失）"}]}]}]},{"project_id":"51","project_bug_count":2,"bug":[{"severity_lev":"2","severity_bug_count":2,"severity_bug":[{"assignedTo":"zhangfan","assignedto_bugs_total":2,"assignedto_bug":[{"bug_id":"5292","bug_title":"【审批设置】【列表】列表超过一页数据，未显示页面"},{"bug_id":"5293","bug_title":"【历史日志】【列表】列表超过一页数据，未显示页面"}]}]}]},{"project_id":"52","project_bug_count":1,"bug":[{"severity_lev":"3","severity_bug_count":1,"severity_bug":[{"assignedTo":"luojun","assignedto_bugs_total":1,"assignedto_bug":[{"bug_id":"6654","bug_title":"【原材料物流】-【原材料称重】，待验收状态的订单，却可以称二次重（未进行校验）"}]}]}]},{"project_id":"53","project_bug_count":5,"bug":[{"severity_lev":"3","severity_bug_count":5,"severity_bug":[{"assignedTo":"zhuzihao","assignedto_bugs_total":5,"assignedto_bug":[{"bug_id":"6884","bug_title":"【登录】用户输入错误格式的手机号或者密码时，登录的时候建议提示账号或密码错误，不要提示请输入。。。"},{"bug_id":"6891","bug_title":"【管理设置】用户列表重置密码时，弹窗未关闭的情况下，可以切换菜单"},{"bug_id":"6892","bug_title":"[pc客户端]下载页，点击下载pc端后，弹出空白页（再浏览器上可以下载）"},{"bug_id":"6893","bug_title":"【个人中心】页面的无效信息，建议先屏蔽掉（客户端版本信息，在web端可以屏蔽，pc端需要按实际版本显示出来）"},{"bug_id":"6894","bug_title":"【个人中心】右上角用户名称，未显示完整（尽量多显示几个字）"}]}]}]}]
    s.BugsCotent(t)
