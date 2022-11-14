# -*- coding: utf-8 -*-
# @Time    : 2022-05-24 15:28
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : get_list.py 
# @Software: PyCharm
import json
import requests
import hashlib


class ChanDao:
    cookies = None
    res = requests.session()

    def __init__(self, login_url):
        self.login_url = login_url
        self.get_session()

    def encrypt_password(self, password):
        """
        登录密码加密处理
        :param password: 禅道账户密码
        :return: 加密结果
        """
        encrypt_method = hashlib.md5()  # 1.造出hash工厂，确定加密算法方式，同一种hash算法得到的长度是固定的
        encrypt_method.update(password.encode("utf-8"))  # 2.运送原材料，工厂传入的原材料都是bytes类型
        return encrypt_method.hexdigest()  # 3.产出hash值，返回加密后得密码

    def get_session(self):
        """
        判断请求是否携带sessionID，如果没有的话，重新获取禅道所需的sessionID
        :return:禅道需要的zentaosid参数
        """
        if self.cookies is None:
            url = self.login_url + 'api-getSessionID.json'
            res = self.res.get(url).content.decode('utf-8')
            res = json.loads(res)
            result = json.loads(res["data"])
            self.cookies = {"zentaosid": result["sessionID"]}
            return self.cookies
        return self.cookies

    def login_chandao(self, data):
        """
        登录禅道系统
        :param data: 账号信息
        :return:登录结果
        """
        url = self.login_url + "user-login.json"
        # pwd = cls.encrypt_password(password)
        ressult = self.res.post(url=url, data=data, cookies=self.cookies).json()
        if ressult["status"] == "success":
            return self.get_session()
        else:
            return ressult

