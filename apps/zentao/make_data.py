# -*- coding: utf-8 -*-
# @Time    : 2022-06-17 11:19
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : make_data.py 
# @Software: PyCharm+
import ast
import pandas as pd


class MakeData:

    def __init__(self):
        pass

    def CountWeek(self, bugs):
            data = pd.DataFrame(bugs)
            result = []
            for project, group in data.groupby(['project_id']):
                project_bugs = group['project_id'].count()
                bugmsg = []
                project_bug = {"project_id": project,
                               "project_bug_count": project_bugs,
                               "bug": bugmsg}
                data = group["bug"].values.tolist()
                data2 = pd.DataFrame(data)
                for severity, bug in data2.groupby(["severity"]):
                    severity_bug_count = bug['severity'].count()
                    severity_bug = []
                    severity_bugs = {"severity_lev".format(bug['severity'].values[0]): severity,
                                     "severity_bug_count": severity_bug_count,
                                     "severity_bug": severity_bug
                                     }
                    for assignedTo, bug_detail in bug.groupby(["assignedTo"]):
                        assignedto_bugs = bug['assignedTo'].count()
                        assignedto_bug = []
                        assignedto_bugs_total = {"assignedTo": "{}".format(assignedTo),
                                                 "assignedto_bugs_total": assignedto_bugs,
                                                 "assignedto_bug": assignedto_bug
                                                 }
                        for k, v in bug_detail.groupby(["id"]):
                            bng = {"bug_id": v["id"].values[0],
                                   "bug_title": v["title"].values[0]
                                   }
                            assignedto_bug.append(bng)
                        severity_bug.append(assignedto_bugs_total)
                    bugmsg.append(severity_bugs)
                result.append(project_bug)
            return result


    # def update_to_bug_status(self):
    #     """
    #     更新bug状态
    #     :return:
    #     """
    #     data = self.count_bug()
    #     for bug in data:
    #         project_id = bug["project_id"]
    #         severity_lev1 = bug["severity_lev1"]
    #         severity_lev2 = bug["severity_lev2"]
    #         severity_lev3 = bug["severity_lev3"]
    #         severity_lev4 = bug["severity_lev4"]
    #         severity_one_bug_title = bug["severity_lev1_bug"]
    #         severity_one_bug_url = bug["severity_lev1_bug_url"]
    #         assigneds = bug["assignedTo"]
    #         assignedTo = []
    #         for personnel in assigneds:
    #             if personnel:
    #                 assigned = self.db_get.get_personnel_config(personnel)
    #                 if assigned:
    #                     assigned = assigned[0]["phone"]
    #                     assignedTo.append("{}".format(assigned))
    #                 else:
    #                     make_data_log.info("未查询到[{}]电话号码".format(personnel))
    #             else:
    #                 make_data_log.info("指派人为空，项目id：{}".format(project_id))
    #         self.db_post.update_bug_status_serverity(severity_lev1=severity_lev1, severity_lev2=severity_lev2,
    #                                                  severity_lev3=severity_lev3, severity_lev4=severity_lev4,
    #                                                  project_id=project_id, assignedto=assignedTo,
    #                                                  severity_one_bug_title=severity_one_bug_title,
    #                                                  severity_one_bug_url=severity_one_bug_url)




