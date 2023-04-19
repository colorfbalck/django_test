# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 23:01
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : utils.py
# @Software: PyCharm

import re

from .models import Evns


def handle_env(datas):
    datas_list = []
    for item in datas:
        # 将creat_time 进行格式化
        match = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        item['create_time'] = match.group(1) + ' ' + match.group(2)
        datas_list.append(item)
    return datas_list
