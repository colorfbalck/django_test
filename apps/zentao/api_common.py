# -*- coding: utf-8 -*-
# @Time    : 2023-02-10 11:32
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : api_common.py 
# @Software: PyCharm
import requests


class RunMain:
    def __init__(self, host="http://127.0.0.1:8000"):
        self.session = requests.Session()
        self.host = host
        self.timeout = 20

    def run_main(self, method, url, data=None, headers=None, params=None, cookies=None):
        if headers is None:
            headers = {}
        if params is None:
            params = {}
        if cookies is None:
            cookies = {}
        url = self.host + url
        if method == "get" or method == "GET":
            return self.get(url, headers=headers, params=params, cookies=cookies)
        elif method == "post" or method == "POST":
            return self.post(url, data, headers=headers, params=params, cookies=cookies)
        elif method == "delete" or method == "DELETE":
            return self.delete(url, data, headers=headers, params=params, cookies=cookies)
        else:
            print("请求方式错误：{}".format(method))
            return False

    def get(self, url, headers=None, params=None, cookies=None):
        try:
            response = self.session.get(url=url, headers=headers, params=params, cookies=cookies,
                                        timeout=self.timeout)
            return response.json()
        except requests.exceptions.ConnectTimeout:
            print("请求服务器超时，请检查连接：GET:{}".format(url))
            return False

    def post(self, url, data=None, headers=None, params=None, cookies=None):
        try:
            response = self.session.post(url=url, json=data, headers=headers, params=params, cookies=cookies,
                                         timeout=self.timeout)
            return response.json()
        except requests.exceptions.ConnectTimeout:
            print("请求服务器超时，请检查连接：POST:{}".format(url))
            return False

    def delete(self, url, data=None, headers=None, params=None, cookies=None):
        try:
            response = self.session.delete(url=url, json=data, headers=headers, params=params, cookies=cookies,
                                           timeout=self.timeout)
            return response.json()
        except requests.exceptions.ConnectTimeout:
            print("请求服务器超时，请检查连接：DELETE:{}".format(url))
            return False
