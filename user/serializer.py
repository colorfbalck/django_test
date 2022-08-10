# -*- coding: utf-8 -*-
# @Time    : 2022/8/9 22:57
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : serializer.py
# @Software: PyCharm
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(label="确认密码", min_length=6, max_length=20, help_text="确认密码",
                                             write_only=True,
                                             error_messages={"min_length": "仅允许输入6~20位字符的确认密码",
                                                             "max_length": "仅允许输入6~20位字符的确认密码",
                                                             })
    token = serializers.CharField(label="生成token", read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'password_confirm', 'token')
        extra_kwargs = {
            'username': {
                'label': '用户名',
                'help_text': '用户名',
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许输入6~20位字符的用户名',
                    'max_length': '仅允许输入6~20位字符的用户名',
                },
            },
            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'write_only': True,
                'required': True,
            },
            'password': {
                'label': '密码',
                'help_text': '密码',
                'min_length': 6,
                'max_length': 20,
                'write_only': True,
                'error_messages': {
                    'min_length': '仅允许输入6~20位字符的密码',
                    'max_length': '仅允许输入6~20位字符的密码',
                },
            }
        }

