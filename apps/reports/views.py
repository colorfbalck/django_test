import json
import os.path
import re
from datetime import datetime

from django.http import StreamingHttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.encoding import escape_uri_path
from drf_yasg.openapi import Response
from rest_framework import response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from apps.reports.models import Reports
from apps.reports.serizlizer import ReportsSerializer
from apps.reports.utils import format_output, get_file_contents
from demo_dj import settings


class ReportsViewSet(ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer

    def perform_destroy(self, instance):
        instance.is_delets = True
        instance.save()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data["results"] = format_output(response.data["results"])

        return response

    @action(detail=True)
    def download(self, request, pk=None):
        instance = self.get_object()
        html = instance.html
        name = instance.name
        mtch = re.match(r'(.*_)\d+', name)
        if mtch:
            mtch = mtch.group(1)
            # 创建报告路径
            report_filename = mtch + datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S') + '.html'
        else:
            report_filename = name
        # report_dir = os.path.join(settings.REPORTS_DIR, )
        # report_path = os.path.join(report_dir, mtch)
        report_path = os.path.join(settings.REPORTS_DIR, report_filename)
        # 将报告保存到reports目录下
        with open(report_path, 'w+', encoding='utf-8') as one_file:
            one_file.write(html)
        response = StreamingHttpResponse(get_file_contents(report_path))
        report_path_final = escape_uri_path(report_filename)
        response["Content-Type"] = "application/octet-stream"
        response["Content-Disposition"] = "attachment;filename*=UTF-8''{}".format(report_path_final)
        return response

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        datas = serializer.data
        try:
            datas["summary"] = json.loads(datas["summary"], encoding='utf-8')
        except Exception as e:
            pass
        return Response(datas)
