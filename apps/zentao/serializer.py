# -*- coding: utf-8 -*-
# @Time    : 2022-10-18 17:48
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : serializer.py 
# @Software: PyCharm
from rest_framework import serializers
from .models import ZentaoUserConfig, Bug, ZentaoConfig, BugProjectConfig, BugPersonnelConfig


class ZentaoLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = ZentaoUserConfig
        fields = "__all__"


class ZentaoSidSerializer(serializers.ModelSerializer):

    class Meta:
        model = ZentaoUserConfig
        fields = ('account', 'zentaosid')


class ZentaoConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = ZentaoConfig
        fields = "__all__"


class ZentaoBugSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bug
        fields = "__all__"


class ZentaoBugProjectConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = BugProjectConfig
        fields = "__all__"


class ZentaoBugPersonnelConfigSerializer(serializers.ModelSerializer):
    """
    bug指派人信息
    """
    class Meta:
        model = BugPersonnelConfig
        fields = ('spell', 'name', "phone")
