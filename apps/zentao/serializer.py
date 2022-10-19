# -*- coding: utf-8 -*-
# @Time    : 2022-10-18 17:48
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : serializer.py 
# @Software: PyCharm
from rest_framework import serializers
from .models import Zentao_user_config


class ZentaoLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zentao_user_config
        fields = "__all__"
