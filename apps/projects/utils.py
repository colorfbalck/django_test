# -*- coding: utf-8 -*-
# @Time    : 2023/3/31 23:48
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : utils.py
# @Software: PyCharm
import re

from django.db.models import Count
from ..interfaces.models import Interface
# from ..testsuits.models import TestSuits



def get_count_by_project(datas):
    data_list = []
    for item in datas:
        match = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        match1 = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        item['create_time'] = match.group(1) + ' ' + match.group(2)
        item['update_time'] = match1.group(1) + ' ' + match1.group(2)

        project_id = item["id"]
        # Interfaces.objects.filter(project_id=project_id, is_delete=False).count()
        interfaces_testcases_objects = Interface.objects.values('id').annotate(testcase=Count('testcases')).\
            filter(project_id=project_id, is_delete=False)
        interfaces_count = interfaces_testcases_objects.count()
        testcase_count = 0
        for one_dict in interfaces_testcases_objects:
            testcase_count += one_dict['testcase']

        interfaces_configures_objects = Interface.objects.values("id").annotate(configures=Count('configures')).\
            filter(project_id=project_id, is_delete=False)
        configures_count = 0
        for one_dict in interfaces_configures_objects:
            configures_count += one_dict['configures']

        testsuits_count = TestSuits.objects.filter(project_id=project_id, is_delete=False).count()

        item["interfaces"] = interfaces_count
        item["testcase"] = testcase_count
        item["configures"] = configures_count
        item["testsuits"] = testsuits_count

        data_list.append(item)

    return data_list
