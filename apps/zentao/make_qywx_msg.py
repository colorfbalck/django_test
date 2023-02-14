# -*- coding: utf-8 -*-
# @Time    : 2022-05-25 14:40
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : send_msg.py 
# @Software: PyCharm
from send_qywx_msg import SendMsgQYWX


class FormatQYWX:

    def __init__(self):
        self.send = SendMsgQYWX()

    def SeverityLevelBug(self, severity_bugs):
        """
        获取到各严重等级下bug数量以人员区分
        :param severity_bugs: 以严重等级区分的bug
        :return:
        """
        qywx_bug_content = []
        for person in range(len(severity_bugs)):
            name = self.send.get_spell_name(severity_bugs[person]["assignedTo"])
            assigned_bug = \
            '''<font color=\\"comment\\">{assignedto_bug}</font>(<font color=\\"warning\\">{assignedto_bugs_total}</font>):\n'''\
                               .format(assignedto_bug=name,assignedto_bugs_total=severity_bugs[person]["assignedto_bugs_total"]),
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

    def BugFormatProjectid(self, unresolvedbugs):
        """
        格式化未关闭bug，并通过项目id进行区分
        :param unresolvedbugs:
        :return:
        """
        if unresolvedbugs:
            projectcontent = []
            for project in range(len(unresolvedbugs)):
                if unresolvedbugs[project]:
                    project_id = unresolvedbugs[project]["project_id"]
                    project_config = self.send.get_project_config(project_id)
                    project_name = project_config["project_name"]
                    qywx_webhook = project_config["qywx_webhook"]
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
                            .format(project_id=project_name, project_bugs=project_bugs,
                                    severity_lev1=severity_lev1, severity_lev1_bugs=severity_lev1_bugs,
                                    severity_lev2=severity_lev2, severity_lev2_bugs=severity_lev2_bugs,
                                    severity_lev3=severity_lev3, severity_lev3_bugs=severity_lev3_bugs,
                                    severity_lev4=severity_lev4, severity_lev4_bugs=severity_lev4_bugs,
                                    )
                        projectcontent.append({"webook": qywx_webhook,
                                               "project_id": project_id,
                                               "content": content}
                                              )
                else:
                    print("项目为空")
            return projectcontent
        else:
            print("bug数量小于0，结束格式化BUG操作！")
            return

    def BugFormatProjectids(self, unresolvedbugs):
        """
        格式化未关闭bug，并通过项目id进行区分
        :param unresolvedbugs:
        :return:
        """
        if unresolvedbugs:
            projectcontent = []
            for project in unresolvedbugs:
                if project:
                    project_id = project["project_id"]
                    project_config = self.send.get_project_config(project_id)
                    project_name = project_config["project_name"]
                    qywx_webhook = project_config["qywx_webhook"]
                    project_bugs = project["project_bug_count"]
                    severitybugs = project["bug"]
                    content_parts = []
                    for severity_bug in severitybugs:
                        severity_lev = severity_bug["severity_lev"]
                        severity_bugs = self.replace_bug(self.SeverityLevelBug(severity_bug["severity_bug"]))
                        """>一级bug：<font color=\"warning\">{severity_lev1}</font>:\n{severity_lev1_bugs}"""
                        content_parts.append(f'>{severity_lev}级bug：<font color=\"warning\">{severity_bugs}</font>')
                    content = "\n".join(content_parts)
                    if len(content) > 2000:
                        # Split content into parts of length <= 4000
                        content_parts = [content[i:i + 2000] for i in range(0, len(content), 2000)]
                    else:
                        content_parts = [content]
                    project_parts = []
                    for i, part in enumerate(content_parts):
                        if i == 0:
                            project_parts.append({"webook": qywx_webhook,
                                                  "project_id": project_id,
                                                  "content": f'<font color=\"info\">{project_name}</font>\n'
                                                             f'>未解决BUG:<font color=\"warning\">{project_bugs}</font>\n'
                                                             f'>各严重等级BUG数量:\n{part}'})
                        else:
                            project_parts.append({"webook": qywx_webhook,
                                                  "project_id": project_id,
                                                  "content": part})
                    projectcontent.extend(project_parts)
                else:
                    print("项目为空")
            return projectcontent
        else:
            print("bug数量小于0，结束格式化BUG操作！")
            return


if __name__ == '__main__':
    test = [{'project_id': 33, 'project_bug_count': 28, 'bug': [{'severity_lev': '1', 'severity_bug_count': 4, 'severity_bug': [{'assignedTo': 'zhangfan', 'assignedto_bugs_total': '', 'assignedto_bug': [{'bug_id': '3040', 'bug_title': '【IC卡办理】进入IC卡关联页面，提示硬件officeofbill占用'}]}, {'assignedTo': 'zhouzhenhua', 'assignedto_bugs_total': '', 'assignedto_bug': [{'bug_id': '3025', 'bug_title': '【出厂】车辆节点切换为出厂操作成功，该订单仍未出发货区状态；出厂后IC卡已解绑车辆，再次进厂未绑定IC卡可进入'}, {'bug_id': '3055', 'bug_title': '【排队发运】车辆进厂后，绑定订单后，审核通过该订单，车辆未进入排队状态'}, {'bug_id': '3059', 'bug_title': '【排队等待】车辆进入等待区且小于车限，未进入呼叫区，一致处于等待区'}]}]}, {'severity_lev': '2', 'severity_bug_count': 16, 'severity_bug': [{'assignedTo': 'zhangfan', 'assignedto_bugs_total': '', 'assignedto_bug': [{'bug_id': '3037', 'bug_title': '【修改IC卡】修改IC卡，修改卡编号后提交，提示访问异常'}]}, {'assignedTo': 'zhouzhenhua', 'assignedto_bugs_total': '', 'assignedto_bug': [{'bug_id': '2985', 'bug_title': '【待一次重待二次重出厂】通过已存在车牌号进行查询失败'}, {'bug_id': '3003', 'bug_title': '【车辆超时】设置车辆超时时间后，等待车辆超时，车辆未跳转且无记录'}, {'bug_id': '3006', 'bug_title': '【发货区】发货区车辆未显示，品种车辆限制数据为空'}, {'bug_id': '3012', 'bug_title': '【排队发运】切换订单状态提示异常'}, {'bug_id': '3014', 'bug_title': '【提货检斤单补打】查询功能无效'}, {'bug_id': '3016', 'bug_title': '【切换提单】切换提单，提示访问异常'}, {'bug_id': '3020', 'bug_title': '【IC卡补卡】进行换卡时，无法识别卡号'}, {'bug_id': '3028', 'bug_title': '【排队车限维护】车辆限制输入超长、小数数据，系统提示异常'}, {'bug_id': '3033', 'bug_title': '【排队优先设置】客户优先级输入小数提示异常'}, {'bug_id': '3039', 'bug_title': '【IC卡注册】IC卡编号查询无效，输入非数字字符提示异常'}, {'bug_id': '3046', 'bug_title': '【一次重】袋装提单通过袋装一次重接口，提示操作成功，状态实际未修改'}, {'bug_id': '3048', 'bug_title': '【待一次重待二次重出厂】车单分离成功后，数据未消失'}, {'bug_id': '3049', 'bug_title': '【新建提单】车辆已出厂，新建提单，提示已开其他袋装提单'}, {'bug_id': '3052', 'bug_title': '【呼叫】手动呼叫车辆，提示访问异常'}, {'bug_id': '3058', 'bug_title': '【IC卡绑定】袋装IC卡绑定散装订单车辆操作成功'}]}]}, {'severity_lev': '3', 'severity_bug_count': 8, 'severity_bug': [{'assignedTo': 'zhangfan', 'assignedto_bugs_total': '', 'assignedto_bug': [{'bug_id': '2990', 'bug_title': '【系统配置】回空车值设置(吨)为空、中文、英文字母大小写，其他符号提示接口访问异常'}]}, {'assignedTo': 'zhouzhenhua', 'assignedto_bugs_total': '', 'assignedto_bug': [{'bug_id': '2986', 'bug_title': '【待一次重待二次重出厂】进行数据查询是，日期只选择起始日期'}, {'bug_id': '2987', 'bug_title': '【待一次重待二次重出厂】进行数据查询是，日期只选择截止日期'}, {'bug_id': '3009', 'bug_title': '【排队发运】通过接口添加4辆进门车辆，未绑定订单，展示错误'}, {'bug_id': '3023', 'bug_title': '【一次重】车辆过一次重后，再次通过该节点提示信息不明确'}, {'bug_id': '3047', 'bug_title': '【待一次重待二次重出厂】已出厂车辆不显示该订单'}, {'bug_id': '3053', 'bug_title': '【车辆进出门查询】未显示出门时间，车辆状态正确标识'}, {'bug_id': '3054', 'bug_title': '【车辆黑名单】车辆黑名单修改后，未记录修改时间与修改人员'}]}]}]}]
    res = FormatQYWX().BugFormatProjectids(test)
    print(res)

