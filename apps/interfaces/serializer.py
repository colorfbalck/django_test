# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 23:54
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : serializer.py
# @Software: PyCharm
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from apps.interfaces.models import Interface
from apps.projects.models import Projects


class InterFaceSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(help_text="项目名称")
    project_id = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), help_text="项目ID")
    # interface_name = serializers.CharField(label='接口名称', max_length=200, min_length=6, help_text='接口名称',
    #                                        validators=[UniqueValidator(queryset=Interface.objects.all(),
    #                                                                    message='接口名称不可重复')],
    #                                        error_messages={'max_length': '长度不超过200个字符', 'min_length': '长度不小于6个字符'})

    class Meta:
        model = Interface
        fields = "id", "name", "tester", "project", "project_id", "desc", "create_time"

        extra_kwargs = {
            "create_time": {
                'read_only': True
            }
        }

    def create(self, validated_data):
        project = validated_data.pop("project_id")
        validated_data["project"] = project
        interface = Interface.objects.create(**validated_data)
        return interface

    def update(self, instance, validated_data):
        if "project_id" in validated_data:
            project = validated_data.pop("project_id")
            validated_data["project"] = project

        return super().update(instance, validated_data)
