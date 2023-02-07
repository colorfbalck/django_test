# -*- coding: utf-8 -*-
# @Time    : 2022-06-17 11:19
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : make_data.py 
# @Software: PyCharm+
import pandas as pd


class MakeData:

    def __init__(self):
        pass

    def CountWeek(self, bugs):
        """
            通过pandas将数据转换数据表方式，进行转换为格式化JSON
        """
        data = pd.DataFrame(bugs)
        result = []
        for project, group in data.groupby(['project_id']):  # 通过项目ID进行分组，获取到每个项目下的缺陷数量
            project_bugs = group['project_id'].count()
            bugmsg = []
            project_bug = {"project_id": project,
                           "project_bug_count": project_bugs,
                           "bug": bugmsg
                           }
            project_DataFrame = pd.DataFrame(group["bug"].values.tolist())
            for severity, bug in project_DataFrame.groupby(["severity"]):  # 再通过缺陷严重等级，获取每个级别下缺陷数量
                severity_bug_count = bug['severity'].count()
                severity_bug = []
                severity_bugs = {"severity_lev".format(bug['severity'].values[0]): severity,
                                 "severity_bug_count": severity_bug_count,
                                 "severity_bug": severity_bug
                                 }
                for assignedTo, bug_detail in bug.groupby(["assignedTo"]):  # 再通过缺陷负责人，获取每个人的缺陷数量
                    assignedto_bugs = ""
                    assignedto_bug = []
                    assignedto_bugs_total = {"assignedTo": "{}".format(assignedTo),
                                             "assignedto_bugs_total": assignedto_bugs,
                                             "assignedto_bug": assignedto_bug
                                             }
                    for k, v in bug_detail.groupby(["id"]):  # 再通过项目id，获取每个缺陷的ID和标题
                        bng = {"bug_id": v["id"].values[0],
                               "bug_title": v["title"].values[0]
                               }
                        assignedto_bug.append(bng)
                    severity_bug.append(assignedto_bugs_total)
                bugmsg.append(severity_bugs)
            result.append(project_bug)
        return result




