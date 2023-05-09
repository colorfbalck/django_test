# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 22:09
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : vaildates.py
# @Software: PyCharm
from rest_framework import serializers

from apps.interfaces.models import Interface
from apps.projects.models import Projects


def whether_existed_project_id(value):
    """
    检查项目id是否存在
    """
    if not isinstance(value, int):
        raise serializers.ValidationError("所选项目有误！")
    elif not Projects.objects.filter(is_delete=False, id=value).exists():
        raise serializers.ValidationError("所选项目不存在")


def whether_existed_interface_id(value):
    """
    检查项目接口id是否存在
    """
    if not isinstance(value, int):
        raise serializers.ValidationError("所选接口有误！")
    elif not Interface.objects.filter(is_delete=False, id=value).exists():
        raise serializers.ValidationError("所选接口不存在")
