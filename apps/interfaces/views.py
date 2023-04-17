from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from apps.interfaces.models import Interface
from apps.interfaces.serializer import InterFaceSerializer
from apps.interfaces.utils import get_count_by_interface


class InterfaceViewSet(viewsets.ModelViewSet):
    queryset = Interface.objects.all()
    serializer_class = InterFaceSerializer
    ordering_fields = ['interface_name', 'project']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas = serializer.data
            datas = get_count_by_interface(datas)
            return self.get_paginated_response(datas)

        serializer = self.get_serializer(queryset, many=True)
        datas = serializer.data
        datas = get_count_by_interface(datas)
        return self.get_paginated_response(datas)
