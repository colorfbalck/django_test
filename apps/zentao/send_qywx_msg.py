# -*- coding: utf-8 -*-
# @Time    : 2022-12-22 17:30
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : send_qywx_msg.py 
# @Software: PyCharm
import json
import requests
host = "http://127.0.0.1:8000"


class SendMsgQYWX:

    def get_project_name(self, projectid):
        url = host+"/zentao/bugprojectsconfig/{projectid}".format(projectid=projectid)
        resp = requests.get(url=url).json()
        return resp

    def get_bug_project(self):
        """
        查询所有项目推送消息配置
        """
        url = host+"/zentao/bugs/"
        resp = requests.get(url=url).json()
        send_bug = []
        for i in range(len(resp)):
            project_id_data = self.get_project_name(resp[i]["project_id"])
            project_id_status = project_id_data["status"]
            project_id_webhook_url = project_id_data["qywx_webhook"]
            if project_id_status == "1" and project_id_webhook_url:
                bugdist = resp[i]
                bugdist["project_id_webhook_url"] = project_id_webhook_url
                send_bug.append(resp[i])
            elif project_id_status == "0":
                print("项目id:" + str(resp[i]["project_id"]), "推送状态未开启")
            else:
                print("项目id:" + str(resp[i]["project_id"]), "状态错误：" + project_id_status)
        return send_bug

    def push_to_qywx(self, url, details):
        for detail in range(len(details)):
            bugs_data = {
                "msgtype": "markdown",
                "markdown": {
                        "content": """%s""" % (details[detail].replace("\\n", "\n"))
                        }
                    }
            res = requests.post(url=url, json=bugs_data, verify=False).content.decode()
            result = json.loads(res)
            if result["errcode"] == 0 and result["errmsg"] == "ok":
                print("消息发送成功，发送地址：{},发送内容：{}")


