import hashlib
import json

from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin

from apps.zentao.models import ZentaoUserConfig as zentaousermodels, Bug
from apps.zentao.models import ZentaoConfig as zentaoconfigmodels
from apps.zentao.models import BugProjectConfig

from apps.zentao.serializer import ZentaoLoginSerializer as zentaologinser
from apps.zentao.serializer import ZentaoConfigSerializer as zentaoser
from apps.zentao.serializer import ZentaoSidSerializer
from apps.zentao.serializer import ZentaoBugSerializer
from apps.zentao.serializer import ZentaoBugProjectConfigSerializer
from apps.zentao.login import ChanDao
from apps.zentao.save_bug import GetBugList
from apps.zentao.make_data import MakeData


class ZentaoAccount(viewsets.ModelViewSet, mixins.CreateModelMixin):
    queryset = zentaousermodels.objects.all()
    serializer_class = zentaologinser


class AccountValidateView(APIView):
    def get(self, request, account):
        data_dict = {
            "account": account,
            "count": zentaousermodels.objects.filter(account=account).count()
        }
        return Response(data_dict)


class ZentaoConfig(viewsets.ModelViewSet):
    queryset = zentaoconfigmodels.objects.all()
    serializer_class = zentaoser


class ZentaoLogin(APIView):
    """
    通过调用禅道登录接口，生成有效zentaosid，存入配置并返回。
    """
    def post(self, request):
        queryset = zentaoconfigmodels.objects.all()
        serializer_class = zentaoser(instance=queryset, many=True)
        urls = serializer_class.data
        url = urls[0]["url"]
        data = request.data
        res = ChanDao(url).login_chandao(data)
        if "zentaosid" in res:
            ser2 = zentaousermodels.objects.filter(account=data["account"])
            if ser2:
                ser2.update(zentaosid=res["zentaosid"], enable=1)
                return Response(res)
            else:
                ser2.create(zentaosid=res["zentaosid"], enable=1)
                return Response(res)
        else:
            ser2 = zentaousermodels.objects.filter(account=data["account"])
            ser2.update(enable=0)
            return Response(res)


class ZentaoBug(APIView):
    """
        获取未关闭BUG，并存入数据库
    """
    def get(self, request):
        queryset = zentaousermodels.objects.filter(enable=1)
        serializer_class = ZentaoSidSerializer(instance=queryset, many=True)
        zensid = serializer_class.data[0]["zentaosid"]
        res = GetBugList(zensid).add_all_bug()
        for bug in range(len(res)):
            bugs = {
                'project_id': res[bug]['product'],
                'bug_id': res[bug]['id'],
                'bug': res[bug],
                'isread': 0
                }
            serializer = ZentaoBugSerializer(data=bugs)
            try:
                serializer.is_valid(raise_exception=True)
            except Exception:
                return Response(serializer.errors)
            serializer.save()
        return Response("2")


class ZentaoBugProjectsConfig(viewsets.ModelViewSet):
    """
    bug推送配置
    """
    queryset = BugProjectConfig.objects.all()
    serializer_class = ZentaoBugProjectConfigSerializer


class ZentaoBugListView(viewsets.ModelViewSet):
    """
    查询所有bug
    """
    queryset = Bug.objects.all()
    serializer_class = ZentaoBugSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        res = MakeData().CountWeek(serializer.data)
        return Response(res)





