# -*- coding: utf-8 -*-
# @Time    : 2022-12-22 17:30
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : send_qywx_msg.py 
# @Software: PyCharm
import requests


class SendMsgQYWX:
    def __init__(self, ip, port):
        self.ip = ip
        self.prot = port

    def get_project_name(self, projectid):
        url = "http://{ip}:{port}/zentao/bugprojectsconfig/{projectid}".format(ip=self.ip, port=self.prot,
                                                                               projectid=projectid)
        resp = requests.get(url=url).json()
        project_name = resp["project_name"]
        return project_name

# def send_qywx_markdown(self):
#     """发送BUG提醒消息，未配置webhook不发送，消息发送成功后修改状态为1,"""
#     data = self.make_qywx_markdown()
#     send_success = 0
#     send_fail = 0
#     send_cancel = 0
#     send_total = len(data)
#     for i in range(len(data)):
#         bug_id = data[ i ][ "bug_id" ]
#         bug_project_id = data[ i ][ "project_id" ]
#         bug_data = data[ i ][ "bug_data" ]
#         bug_data_mobile_list = data[ i ][ "bug_data_mobile_list" ]
#         bug_data_mobile_list_phone = bug_data_mobile_list[ "text" ][ "mentioned_mobile_list" ]
#         webhook_url = self.db_get.project_webhook(bug_project_id)
#         if webhook_url[ 0 ][ "status" ] == 1 and webhook_url[ 0 ][ "qywx_webhook" ]:
#             res = requests.post(url=webhook_url[ 0 ][ "qywx_webhook" ], json=bug_data, verify=False).content.decode()
#             result = json.loads(res)
#             if result[ "errcode" ] == 0 and result[ "errmsg" ] == "ok":
#                 send_log.info("消息发送成功，发送地址：{},发送内容：{}".format(webhook_url[ 0 ][ "qywx_webhook" ], bug_data))
#                 send_success += 1
#                 if bug_data_mobile_list_phone is not None and len(bug_data_mobile_list_phone) > 2:
#                     bug_data_mobile_list = ast.literal_eval(str(bug_data_mobile_list).replace('"', ""))
#                     res_two = requests.post(url=webhook_url[ 0 ][ "qywx_webhook" ], json=bug_data_mobile_list,
#                                             verify=False).content.decode()
#                     res_two = json.loads(res_two)
#                     send_log.info("发送text文本{},请求结果：{}".format(bug_data_mobile_list, res_two))
#                     if res_two[ "errcode" ] == 0 and res_two[ "errmsg" ] == "ok":
#                         send_log.info("@成功：{},指派：{}".format(webhook_url[ 0 ][ "qywx_webhook" ],
#                                                             bug_data_mobile_list))
#                     else:
#                         send_log.info("@失败，成员：{},地址：{}".format(webhook_url[ 0 ][ "qywx_webhook" ],
#                                                                bug_data_mobile_list))
#                 else:
#                 self.db_post.update(self.time.get_datetime(), bug_id)
#             else:
#                 send_fail += 1
#         else:
#             send_cancel += 1
#     send_log.info("总共：{}条BUG提醒信息，成功发送：{}条,未发送{}条，发送失败{}条".format(send_total,
#                                                                  send_success, send_cancel, send_fail))


if __name__ == '__main__':
    SendMsg("127.0.0.1", "8000").get_project_name(19)
