from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.configures.models import Configures
from apps.interfaces.models import Interface
from apps.interfaces.serializer import InterFaceSerializer
from apps.interfaces.utils import get_count_by_interface
from apps.testcases.models import Testcases


class InterfaceViewSet(viewsets.ModelViewSet):
    queryset = Interface.objects.filter(is_delete=False)
    serializer_class = InterFaceSerializer
    ordering_fields = ['name', 'id']

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    @action(methods=["get"], detail=True)
    def testcase(self, request, pk=None):
        testcase_objs = Testcases.objects.filter(interface=pk, is_delete=False)
        one_list = []
        for obj in testcase_objs:
            one_list.append({
                "id": obj.id,
                "name": obj.name
            })
        return Response(data=one_list)

    @action(methods=["get"], detail=True, url_path='configs')
    def configures(self, request, pk=None):
        configures_objs = Configures.objects.filter(interface=pk)
        one_list = []
        for obj in configures_objs:
            one_list.append({
                "id": obj.id,
                "name": obj.name
            })
        return Response(data=one_list)

    def list(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        # page = self.paginate_queryset(queryset)
        #
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     datas = serializer.data
        #     datas = get_count_by_interface(datas)
        #     return self.get_paginated_response(datas)
        #
        # serializer = self.get_serializer(queryset, many=True)
        # datas = serializer.data
        # datas = get_count_by_interface(datas)
        # return self.get_paginated_response(datas)
        response = super(InterfaceViewSet, self).list(request, *args, **kwargs)
        response.data["results"] = get_count_by_interface(response.data["results"])

        return response
