# -*- coding: utf-8 -*-
# @Time    : 2022-10-19 10:20
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : urls.py 
# @Software: PyCharm
from rest_framework import routers
from apps.zentao import views

router = routers.DefaultRouter()
router.register(r'zentao', views.ZentaoAccount)
urlpatterns = [

]
urlpatterns += router.urls
