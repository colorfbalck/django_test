# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 23:05
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : urls.py
# @Software: PyCharm
from rest_framework import routers
from apps.envs import views

router = routers.DefaultRouter()
router.register(r'', views.EnvsViewSet)
urlpatterns = [

]
urlpatterns += router.urls
