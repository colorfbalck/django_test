from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from apps.debugtalks.models import Debugtalks
from apps.debugtalks.serializer import DebugTalksSerializer


class DebugTalksViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):

    queryset = Debugtalks.objects.filter(is_delete=False)
    serializer_class = DebugTalksSerializer
    ordering_fields = ("id", "project_id")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data_dict = {
            "id": instance.id,
            "debugtalk": instance.debugtalk
        }
        return Response(data_dict)

