# -*- coding: utf-8 -*-
# @Time    : 2023-02-10 10:34
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : get_bugs.py 
# @Software: PyCharm
import json
import requests

from send_qywx_msg import SendMsgQYWX
from make_data import MakeData
from make_qywx_msg import FormatQYWX

host = "http://127.0.0.1:8000"


class GetBUG:

    def __init__(self):
        self.format_qywx = FormatQYWX()
        self.format_json = MakeData()

    def get_unresolvedbug(self, project_id, status=0):
        """
            获取指定项目未关闭BUG
        """
        url = host + "/zentao/bugs/?p=1&s=999&project_id={project_id}&status={status}"\
            .format(project_id=project_id, status=status)
        res = requests.get(url=url).json()
        unresolvebugs = res["results"]
        if unresolvebugs:
            format_bugs = self.format_json.CountWeek(unresolvebugs)
            return format_bugs
        else:
            print("项目id:【{}】待发送bug为0".format(project_id))

    def get_unresolvedbugs_all(self):
        """
            查询所有未关闭BUG，并行格式为json类型
        """
        project_on = SendMsgQYWX().get_project_config_all()
        all_project_config = project_on["results"]
        all_format_bug = []
        for i in range(0, len(all_project_config)):
            format_bug = self.get_unresolvedbug(all_project_config[i]["project_id"])
            if format_bug != None:
                all_format_bug.append(format_bug)
        return all_format_bug

    def get_qywxbugs_all(self, unresolvedbugs):
        """
            将bug格式为企业微信消息支持类型
        """
        if unresolvedbugs:
            project_msg = []
            for project_unresolvebug in unresolvedbugs:
                qywx_msg = self.format_qywx.BugFormatProjectids(project_unresolvebug)
                project_msg.append(qywx_msg)
            return project_msg
        else:
            print("待格式化bug为空")


if __name__ == '__main__':
    print(GetBUG().get_unresolvedbugs_all())
