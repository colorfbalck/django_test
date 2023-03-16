# -*- coding: utf-8 -*-
# @Time    : 2023-02-08 09:59
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : run.py 
# @Software: PyCharm
from get_bugs import GetBUG
from send_qywx_msg import SendMsgQYWX

all_bug = GetBUG().get_unresolvedbugs_all()
format_res = GetBUG().get_qywxbugs_all(all_bug)
qywx_response = SendMsgQYWX().push_to_qywx(format_res)

