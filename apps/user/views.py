from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


from . import serializer


class RegisterView(CreateAPIView):
    serializer_class = serializer.RegisterSerializer


class UsernameValidateView(APIView):
    """
    校验用户名是否存在
    """
    def get(self, request, username):
        data_dict = {
            'username': username,
            "count": User.objects.filter(username=username).count()
        }
        return Response(data_dict)


class EmaileValidateView(APIView):
    """
    校验邮箱
    """
    def get(self, request, email):
        data_dict = {
            'username': email,
            "count": User.objects.filter(email=email).count()
        }
        return Response(data_dict)
