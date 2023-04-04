# -*- coding: utf-8 -*-
# @Time    : 2023/4/4 23:11
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path, re_path
from rest_framework import routers
from apps.interfaces import views

router = routers.DefaultRouter()
router.register(r'', views.InterfaceViewSet)
urlpatterns = [

]
urlpatterns += router.urls