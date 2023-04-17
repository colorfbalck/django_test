# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 23:54
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : serializer.py
# @Software: PyCharm
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from apps.interfaces.models import Interface


class InterFaceSerializer(serializers.ModelSerializer):
    interface_name = serializers.CharField(label='接口名称', max_length=200, min_length=6, help_text='接口名称',
                                           validators=[UniqueValidator(queryset=Interface.objects.all(),
                                                                       message='接口名称不可重复')],
                                           error_messages={'max_length': '长度不超过200个字符', 'min_length': '长度不小于6个字符'})

    class Meta:
        model = Interface
        fields = "__all__"
