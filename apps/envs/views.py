from django.shortcuts import render

# Create your views here.
from drf_yasg.openapi import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.envs.models import Evns
from apps.envs.serializer import EnvsSerializer, EnvsNameSerializer
from apps.envs.utils import handle_env


class EnvsViewSet(viewsets.ModelViewSet):
    """
    项目视图
    """
    queryset = Evns.objects.all()
    serializer_class = EnvsSerializer
    ordering_fields = ['id', 'name']

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data["results"] = handle_env(response.data["results"])

        return response

    @action(methods=["get"], detail=True)
    def names(self, request, pk=None):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == "names":
            return EnvsNameSerializer
        else:
            return EnvsSerializer
