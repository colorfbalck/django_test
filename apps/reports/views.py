import os.path
import re

from django.http import StreamingHttpResponse
from django.shortcuts import render

# Create your views here.
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

        report_dir = os.path.join(settings.BASE_DIR)
        report_path = os.path.join(report_dir, mtch)
        response = StreamingHttpResponse(get_file_contents(report_path))
        response["Content-Type"] = "application/octet-stream"
        response["Content-Disposition"] = "attachment;filename*=UTF-8".format(name)
        return response

