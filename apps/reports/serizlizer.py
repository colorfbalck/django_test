# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 22:30
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : serizlizer.py
# @Software: PyCharm
from datetime import datetime

from rest_framework import serializers

from apps.reports.models import Reports


class ReportsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reports
        exclude = ("update_time", "is_delete")

        extra_kwargs = {
            "html": {
                'write_only': True
            }
        }

    def create(self, validated_data):
        report_name = validated_data["name"]
        validated_data["name"] = report_name + "_" + datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        report = Reports.objects.create(**validated_data)
        return report

