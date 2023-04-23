# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 21:59
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : serializer.py
# @Software: PyCharm
from rest_framework import serializers
from apps.debugtalks.models import Debugtalks


class DebugTalksSerializer(serializers.ModelSerializer):
    """
        DebugTalks序列化器
    """
    project = serializers.StringRelatedField(help_text="项目名称")

    class Meta:
        model = Debugtalks
        exclude = ("is_delete", "create_time", "update_time")
        read_only_fiedls = ("name", "project")

        extra_kwargs = {
            "debugtalk": {
                'write_only': True
            }
        }


