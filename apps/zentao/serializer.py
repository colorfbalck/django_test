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

    def validate(self, attrs):
        bug_id = attrs.get("bug_id")
        if Bug.objects.filter(bug_id=bug_id).exists():
            raise serializers.ValidationError(f"BUG[{bug_id}]：已添加，已修改状态为开启")
        return attrs

    def create(self, validated_data):
        instance, created = Bug.objects.get_or_create(
            bug_id=validated_data["bug_id"],
            defaults={"project_id": validated_data["project_id"], "bug": validated_data["bug"], "status": 0},
        )
        if not created:
            instance.project_id = validated_data["project_id"]
            instance.bug = validated_data["bug"]
            instance.status = 0
            instance.save()
        else:
            instance.save()
        return instance


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
