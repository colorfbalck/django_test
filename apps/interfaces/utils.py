# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 23:54
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : utils.py
# @Software: PyCharm
import re


# from apps.configures.models import Configures
from apps.testcases.models import Testcases


def get_count_by_interface(datas):
    data_list = []
    for item in datas:
        result = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        match1 = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        item['create_time'] = result.group(1) + ' ' + result.group(2)
        item['update_time'] = match1.group(1) + ' ' + match1.group(2)
        project_id = item["project"]
        interfaces_testcases_count = Testcases.objects.filter(interface=item['id'], is_delete=False).count()
        # interfaces_configures_count = Configures.objects.filter(interface=item['id']).count()

        item["testcases"] = interfaces_testcases_count
        # item["configures"] = interfaces_configures_count

        data_list.append(item)
        data_list.append(item)
    return data_list