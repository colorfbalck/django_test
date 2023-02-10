# -*- coding: utf-8 -*-
# @Time    : 2022-12-22 17:30
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : send_qywx_msg.py 
# @Software: PyCharm
import json
from api_common import RunMain

class SendMsgQYWX:

    def __init__(self):
        self.api = RunMain().run_main

    def get_project_name(self, projectid):
        """
            通过项目id查询项目推送配置信息
        """
        url = "/zentao/projectsconfig/{}".format(projectid)
        resp = self.api(url=url, method="get")
        return resp

    def get_bug_project(self):
        """
        查询所有项目推送消息配置
        """
        url = "/zentao/projectsconfig/?p=1&s=999&status=1"
        res = self.api(url=url, method="get").json()
        projects_config = res["results"]
        available_projects = []
        for i in range(len(projects_config)):
            if projects_config[i]["qywx_webhook"]:
                available_projects.append({
                    "project_id": projects_config[i]["project_id"],
                    "qywx_webhook": projects_config[i]["qywx_webhook"]
                })
            else:
                print("项目id:" + str(projects_config[i]["project_id"]) + "qywx_webhook地址为空")
        return available_projects

    def push_to_qywx(self, details):
        """1.待完成提交成功后对bug状态修改
        """
        for detail in range(len(details)):
            url = details[detail]["webook"]

            bugs_data = {
                "msgtype": "markdown",
                "markdown": {
                        "content": """%s""" % (details[detail]["content"].replace("\\n", "\n"))
                        }
                    }
            print(bugs_data)
            response = self.api(url=url, method="post", data=bugs_data).content.decode()
            result = json.loads(response)
            if result["errcode"] == 0 and result["errmsg"] == "ok":
                print("消息发送成功，发送地址：{},发送内容：{}")

    def get_spell_name(self, spell):
        """
            通过拼音查询中文名称
        """
        url = "/zentao/spell/{}".format(spell)
        result = self.api(url=url, method="get")
        try:
            return result["name"]
        except:
            print("中文名称未找到，返回拼音：{}".format(spell))
            return spell


if __name__ == '__main__':
    res = SendMsgQYWX().get_spell_name("zhuzhihao")
    print(res)
