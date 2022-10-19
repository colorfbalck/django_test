# -*- coding: utf-8 -*-
# @Time    : 2022/6/23 23:18
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path, include
from rest_framework import routers
from apps.projects import views
# from projects.views import index
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'projects', views.ProjectViewSet)
# 1.创建SimpleRouter路由对象
# router = routers.SimpleRouter()
router = routers.DefaultRouter()
# 2.注册路由
# 第一个参数prefix为路由前缀，一般提那就为应用名即可
# 第二参数viewset为是视图集，不要加as_view()
router.register(r'projects', views.ProjectViewSet)
urlpatterns = [
    # 函数视图
    # path('', index),
    # 类视图
    # path('', views.IndexView.as_view()),
    # path('<int:pk>/', views.IndexView.as_view())
    # int为路径参数类型转换器
    # ：左边为转换器，右边为参数别名
    # int，slug，uuid
    # path('projects/', views.ProjectList.as_view()),
    # path('projects/<int:pk>', views.ProjectsDetail.as_view())


    # path('projects/names/', views.ProjectViewSet.as_view({
    #     "get": "names",
    # }), name='projects-names'),
    #
    # path('projects/<int:pk>/interfaces/', views.ProjectViewSet.as_view({
    #     "get": "interfaces",
    # }), name='interfaces')

    # 3.将自动生成的路由添加到列表（urlpatterns）中
    # path('', include(router.urls))
]
urlpatterns += router.urls
