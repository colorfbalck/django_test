# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 21:57
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : urls.py
# @Software: PyCharm
from rest_framework import routers
from apps.debugtalks import views

router = routers.DefaultRouter()
router.register(r'', views.DebugTalksViewSet)
urlpatterns = [

]
urlpatterns += router.urls
