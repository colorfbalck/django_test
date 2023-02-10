# -*- coding: utf-8 -*-
# @Time    : 2022-05-25 14:40
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : send_msg.py 
# @Software: PyCharm
from send_qywx_msg import SendMsgQYWX


class Send:

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
        projectcontent = []
        for project in range(len(unresolvedbugs)):
            project_id = unresolvedbugs[project]["project_id"]
            project_config = self.send.get_project_name(project_id)
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
                                       "content": content})
        return projectcontent


