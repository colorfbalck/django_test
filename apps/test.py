# -*- coding: utf-8 -*-
# @Time    : 2022-10-27 17:00
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : test.py 
# @Software: PyCharm
a = ['维度/指标', '维度', '维度', '维度', '维度', '维度', '维度', '维度', '维度', '维度', '维度', '指标', '指标', '指标', '指标', '指标', '指标', '指标', '指标', '指标', '指标', '指标', '', '', '', '']
b = ['id', '月份', '组织名称', '基地名称', '岗位编码', '岗位名称', '岗位类型', '岗位大类', '岗位类别', '部门名称', '职务级别', '实际出勤人数', '应出勤工时\n（个人）', '应出勤工时\n（合计）', '应出勤人数', '应出勤天数', '实际出勤工时\n（考勤确认）', '实际出勤率', '缺卡天数', '工时负荷度', '加班率', '加班时长', 'sql', 'ads_query_result', 'check_result', '备注']


def Find(find_list, x):
    new_index = []
    for i, item in enumerate(find_list):
        if item == x:
            new_index.append(i)
    return new_index


def GetVaule(value_list, find_list):
    Vaule = []
    for i in find_list:
        Vaule.append(value_list[i])
    return Vaule


find_res = Find(a, "指标")
value_res = GetVaule(b, find_res)
print(find_res)
print(value_res)


