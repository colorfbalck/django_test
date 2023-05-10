import json

from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from apps.configures.models import Configures
from apps.configures.serializers import ConfiguresSerializer


class ConfiguresViewSet(ModelViewSet):
    queryset = Configures.objects.filter(is_delete=False)
    serializer_class = ConfiguresSerializer
    permission_classes = (permissions.IsAuthenticated)
    ordering_fields = ('id', 'name')

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()  #逻辑删除

    def retrieve(self, request, *args, **kwargs):
        config_obj = self.get_object()
        config_request = json.loads(config_obj.request, encoding='utf-8')
        config_headers = config_request['config']['request']['headers']
