# -*- coding: utf-8 -*-
# @Time    : 2022-06-17 11:19
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : make_data.py 
# @Software: PyCharm+
import ast


class MakeData:

    def __init__(self):
        pass

    def CountWeek(self, bugs):
        print(bugs[0]["bug"])
        

    # def count_bug(self):
    #     """
    #     统计bug数量
    #     :return:
    #     """
    #     bug_status = self.db_get.get_all_buglist(self.time.get_oneday_before())
    #     severity_lev1 = 0
    #     severity_lev2 = 0
    #     severity_lev3 = 0
    #     severity_lev4 = 0
    #     assignedTo = []
    #     severity_lev1_bug = []
    #     severity_lev1_bug_url = []
    #     all_bug_data = []
    #     project_id = bug_status[0]["project_id"]
    #     for i in bug_status:
    #         pr_id = i["project_id"]
    #         if pr_id != project_id:
    #             project_bug = {
    #                 "project_id": project_id,
    #                 "severity_lev1": severity_lev1,
    #                 "severity_lev2": severity_lev2,
    #                 "severity_lev3": severity_lev3,
    #                 "severity_lev4": severity_lev4,
    #                 "assignedTo": set(assignedTo),
    #                 "severity_lev1_bug": severity_lev1_bug,
    #                 "severity_lev1_bug_url": severity_lev1_bug_url
    #             }
    #             all_bug_data.append(project_bug)
    #             severity_lev1 = 0
    #             severity_lev2 = 0
    #             severity_lev3 = 0
    #             severity_lev4 = 0
    #             project_id = pr_id
    #             assignedTo = []
    #             severity_lev1_bug = []
    #             severity_lev1_bug_url = []
    #         bug = ast.literal_eval(i["bug"])
    #         bug_severity = int(bug["severity"])
    #         bug_assignedTo = bug["assignedTo"]
    #         assignedTo.append(bug_assignedTo)
    #         if bug_severity == 1:
    #             severity_lev1_bug.append(bug["title"])
    #             url = "http://chandao.idmakers.cn/zentao/bug-view-{}.html".format(bug["id"])
    #             severity_lev1_bug_url.append(url)
    #             severity_lev1 += 1
    #         elif bug_severity == 2:
    #             severity_lev2 += 1
    #         elif bug_severity == 3:
    #             severity_lev3 += 1
    #         elif bug_severity == 4:
    #             severity_lev4 += 1
    #         else:
    #             make_data_log.error("BUG严重等级统计错误")
    #     project_bug = {
    #         "project_id": project_id,
    #         "severity_lev1": severity_lev1,
    #         "severity_lev2": severity_lev2,
    #         "severity_lev3": severity_lev3,
    #         "severity_lev4": severity_lev4,
    #         "assignedTo": set(assignedTo),
    #         "severity_lev1_bug": severity_lev1_bug,
    #         "severity_lev1_bug_url": severity_lev1_bug_url
    #     }
    #     all_bug_data.append(project_bug)
    #     return all_bug_data

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




