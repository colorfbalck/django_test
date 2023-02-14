# -*- coding: utf-8 -*-
# @Time    : 2022-12-22 17:30
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : send_qywx_msg.py 
# @Software: PyCharm
import json

import requests

from api_common import RunMain


class SendMsgQYWX:

    def __init__(self):
        self.api = RunMain().run_main

    def get_project_config(self, *args):
        """
            通过项目id查询项目推送配置信息
        """
        url = "/zentao/projectsconfig/{}".format(args[0])
        result = self.api(url=url, method="get")
        if "?" in args:
            projects_config = result["results"]
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
        else:
            return result

    def get_project_config_all(self):
        """
        查询所有项目推送消息配置
        """
        url = "?p=1&s=999&status=1"
        return self.get_project_config(url)


    def push_to_qywx(self, details): #1.待完成提交成功后对bug状态修改
        """
            推送消息至企业微信
        """
        if details:
            for project_detail in details:
                for detail in project_detail:
                    url = detail["webook"]
                    project_id = detail["project_id"]
                    content = detail['content'].replace("\\n", "\n")
                    if url:
                        bugs_data = {
                            "msgtype": "markdown",
                            "markdown": {
                                    "content": content
                                    }
                                }
                        response = requests.post(url=url, json=bugs_data, verify=False)
                        result = response.json()
                        if result["errcode"] == 0 and result["errmsg"] == "ok":
                            print(f"消息发送成功，发送地址：{url},发送内容：{content}")
                            update_project_id = {"project_id": project_id}
                            url = "/zentao/bugs/update_status/"
                            update_status_result = self.api(url=url, method="post", data=update_project_id)
                            if update_status_result["status"] == "0":
                                print("更新该项目相关bug状态操作成功")
                            else:
                                print(f"更新该项目相关bug状态操作失败:{update_status_result}")
                        else:
                            print(f"消息发送失败：{result}")
                    else:
                        print(f"消息发送失败，项目【{project_id}】：webhook地址为空")
        else:
            print("发送消息为空，结束发送！")
            return False

    def get_spell_name(self, spell):
        """
            通过拼音查询中文名称
        """
        url = "/zentao/spell/?spell={}".format(spell)
        result = self.api(url=url, method="get")
        try:
            name = result["results"][0]["name"]
            return name
        except:
            print("中文名称未找到，返回拼音：{}".format(spell))
            return spell

