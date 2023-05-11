# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 22:24
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : handle_datas.py
# @Software: PyCharm

def handle_param_type(value):
    """
    处理参数类型
    """
    if isinstance(value, int):
        param_type = 'int'
    elif isinstance(value, float):
        param_type = 'float'
    elif isinstance(value, bool):
        param_type = 'boolean'
    else:
        param_type = "string"

    return  param_type