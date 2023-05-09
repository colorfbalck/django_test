# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 22:33
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : urls.py
# @Software: PyCharm
from rest_framework import routers
from apps.configures import views

router = routers.DefaultRouter()
router.register(r'', views.ConfiguresViewSet)
urlpatterns = [

]
urlpatterns += router.urls