# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 22:58
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : urls.py
# @Software: PyCharm
from rest_framework import routers
from apps.reports import views

router = routers.DefaultRouter()
router.register(r'', views.ReportsViewSet)
urlpatterns = [

]
urlpatterns += router.urls
