# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 21:54
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers

from apps.configures.models import Configures
from apps.interfaces.models import Interface
from utils.vaildates import whether_existed_project_id, whether_existed_interface_id


class InterfacesAnotherSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(help_text="项目名称")
    # 项目id
    pid = serializers.IntegerField(write_only=True, validators=[whether_existed_project_id], help_text="项目ID")
    # 接口id
    iid = serializers.IntegerField(write_only=True, validators=[whether_existed_interface_id],  help_text="接口ID")

    class Meta:
        model = Interface
        fields = ('iid', 'name', 'project', 'pid')
        extra_kwars = {
            'iid': {
                "write_only": True
            },
            'name': {
                "write_only": True
            }
        }


class ConfiguresSerializer(serializers.ModelSerializer):
    """
    配置序列化器
    """
    interface = InterfacesAnotherSerializer(help_text="项目ID和接口ID")

    class Meta:
        model = Configures
        fields = ('id', 'name', 'interface', 'author', 'request')
        extra_kwars = {
            'request': {
                "write_only": True
            }
        }

    def create(self, validated_data):
        interface_dict = validated_data.pop("interface")
        validated_data['interface_id'] = interface_dict['iid']
        return Configures.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'interface' in validated_data:
            instance_dict = validated_data.pop('interface')
            validated_data['interface_id'] = instance_dict['iid']
        return super().update(instance, validated_data)
