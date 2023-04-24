# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 22:34
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : utils.py
# @Software: PyCharm
from datetime import datetime
import re
from django.db.models import Count


def format_output(datas):
    data_list = []
    for item in datas:
        result = "Pass" if item["result"] else "Fail"

        math = re.search(r'(.*)T(.*)\..*?', item["create_time"])
        item["create_time"] = math.group(1) + "" + math.group(2)

        item["result"] = result
        data_list.append(item)

    return data_list


def get_file_contents(filename, chunk_size=512):
    with open(filename, encoding='utf-8') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break

