# -*- coding: utf-8 -*-
# @Time    : 2022-10-19 10:20
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : urls.py 
# @Software: PyCharm
from django.urls import path, re_path
from rest_framework import routers
from apps.zentao import views

router = routers.DefaultRouter()
router.register(r"config", views.ZentaoConfig)
router.register(r'bugprojectsconfig', views.ZentaoBugProjectsConfig)
router.register(r'bugs', views.ZentaoBugListView)
router.register(r'spell', views.ZentaoBugPersonnelConfig)
urlpatterns = [
    re_path(r'^(?P<account>.{3,20})/count/$', views.AccountValidateView.as_view(), name='check_account'),
    path('login/', views.ZentaoLogin.as_view(), name="zentao_login"),
    path('addbug/', views.ZentaoBug.as_view(), name="zentaobug"),
]
urlpatterns += router.urls
