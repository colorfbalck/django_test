# -*- coding: utf-8 -*-
# @Time    : 2022/8/9 21:34
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
import views
urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', views.RegisterView.as_view()),

]
