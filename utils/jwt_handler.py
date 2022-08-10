# -*- coding: utf-8 -*-
# @Time    : 2022/8/9 22:13
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : jwt_handler.py
# @Software: PyCharm
def jwt_response_payload_handler(token, user=None, request=None):
    """
    """
    return {
        'token': token,
        'user_id': user.id,
        'user_name': user.username,
        'user_email': user.email,
    }
