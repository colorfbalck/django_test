# -*- coding:utf-8 -*-
from django.test import TestCase
# Create your tests here.
import requests

from get_bugs import GetBUG
from make_qywx_msg import FormatQYWX
from send_qywx_msg import SendMsgQYWX

url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a1967ab3-1853-45df-abb0-de06c0b94338"
bug_data = {"msgtype": "markdown",
            "markdown": {
                "content": """<font color=\"info\">商砼平台-销售系统</font>\n
                >未解决BUG:<font color=\"warning\">12</font>\n
                >各严重等级BUG数量:
                >一级bug：<font color=\"warning\">0</font>:\n
                >二级bug：<font color=\"warning\">2</font>:\n
                 <font color=\"comment\">周震华</font>(<font color=\"warning\">2</font>)\n
                    [V-1.0.0：蜂巢APP登录首页，要求登录功能增加个防抖机制。](http://chandao.idmakers.cn/zentao/bug-view-2837.html)\n
                    [V-1.0.0：审批元应用，需求规定会签审批，如果是有多个审批人，必须所有人审批通过才算通过，目前一个人审批通过单据就通过审批了。](http://chandao.idmakers.cn/zentao/bug-view-2938.html)\n
                <font color=\"comment\">罗俊</font>(<font color=\"warning\">5</font>)\n   
                    [V-1.0.0：审批元应用，需求规定会签审批，如果是有多个审批人，必须所有人审批通过才算通过，目前一个人审批通过单据就通过审批了。](http://chandao.idmakers.cn/zentao/bug-view-2938.html)\n
                    [V-1.0.0：审批元应用，需求规定会签审批，如果是有多个审批人，必须所有人审批通过才算通过，目前一个人审批通过单据就通过审批了。](http://chandao.idmakers.cn/zentao/bug-view-2938.html)\n
                    [V-1.0.0：审批元应用，需求规定会签审批，如果是有多个审批人，必须所有人审批通过才算通过，目前一个人审批通过单据就通过审批了。](http://chandao.idmakers.cn/zentao/bug-view-2938.html)\n
                    [V-1.0.0：审批元应用，需求规定会签审批，如果是有多个审批人，必须所有人审批通过才算通过，目前一个人审批通过单据就通过审批了。](http://chandao.idmakers.cn/zentao/bug-view-2938.html)\n
                    [V-1.0.0：审批元应用，需求规定会签审批，如果是有多个审批人，必须所有人审批通过才算通过，目前一个人审批通过单据就通过审批了。](http://chandao.idmakers.cn/zentao/bug-view-2938.html)\n
                    """
                }}

# res = requests.post(url=url, json=data2, verify=False).content.decode()
# print(res)


# project_on = SendMsgQYWX().get_project_config_all()
# # unresolvedbugs = GetBUG().get_unresolvedbugs(53)
# # print(unresolvedbugs)
all_bug = GetBUG().get_unresolvedbugs_all()
print(all_bug)
# res = GetBUG().get_qywxbugs_all(all_bug)
# print(res)
# qywx_response = SendMsgQYWX().push_to_qywx(res)
