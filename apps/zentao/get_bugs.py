# -*- coding: utf-8 -*-
# @Time    : 2023-02-10 10:34
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : get_bugs.py 
# @Software: PyCharm
import json
import requests

from make_data import MakeData

host = "http://127.0.0.1:8000"


class GetBUG:

    def __init__(self):
        pass

    def get_unresolvedbugs(self, project_id, status=0):
        url = host + "/zentao/bugs/?p=1&s=999&project_id={project_id}&status={status}"\
            .format(project_id=project_id, status=status)
        res = requests.get(url=url).json()
        unresolvebugs = res["results"]
        if unresolvebugs:
            format_bugs = MakeData().CountWeek(unresolvebugs)
            return format_bugs
        else:
            print("项目id:【{}】待发送bug为0".format(project_id))
            return False

