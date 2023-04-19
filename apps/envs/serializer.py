# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 22:49
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : serializer.py
# @Software: PyCharm
from rest_framework import serializers
from apps.envs.models import Evns


class EnvsSerializer(serializers.ModelSerializer):
    """
        环境变量序列化器
    """

    class Meta:
        model = Evns
        fields = "id", "name", "base_url", "desc", "create_time"

        extra_kwargs = {
            "create_time": {
                'read_only': True
            }
        }


class EnvsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evns
        fields = "id", "name"
