# -*- coding: utf-8 -*-
# @Time    : 2023-02-10 11:32
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : api_common.py 
# @Software: PyCharm
import requests
host = "http://127.0.0.1:8000"


class RunMain:

    def __init__(self):
        pass

    def run_main(self, method, url, *args):
        result = None
        url = "http://127.0.0.1:8000" + url
        print("请求方式:{}，请求url：{}，请求数据{}".format(method, url, args))
        if method == "get" or method == "GET":
            result = self.get(url, args)
        elif method == "post" or method == "POST":
            result = self.post(url, data=args)
        elif method == "delete" or method == "DELETE":
            result = self.delete(url, args)
        else:
            print("请求方式错误：{}".format(method))
        return result

    def get(self, url,  args):
        try:
            result = requests.get(url=url, params=args, timeout=3).json()
            return result
        except requests.exceptions.ConnectTimeout:
            print("请求服务器超时，请检查连接：GET:{}".format(url))
            return False

    def post(self, url, data):
        try:
            result = requests.post(url=url, json=data, timeout=3).json()
            return result
        except requests.exceptions.ConnectTimeout:
            print("请求服务器超时，请检查连接：POST:{}".format(url))
            return False

    def delete(self, url, data):
        try:
            result = requests.delete(url=url, json=data).json()
            return result
        except requests.exceptions.ConnectTimeout:
            print("请求服务器超时，请检查连接：delete:{}".format(url))
            return False
