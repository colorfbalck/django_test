# -*- coding: utf-8 -*-
# @Time    : 2023-02-08 09:59
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : run.py 
# @Software: PyCharm
from make_qywx_msg import Send
from send_qywx_msg import SendMsgQYWX

bugs = SendMsgQYWX().get_bug_project()
print(bugs)
# send_bug = Send().BugFormatProjectid(bugs)

