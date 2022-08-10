from rest_framework.generics import CreateAPIView
from serializer import RegisterSerializer


class RegisterView(CreateAPIView):
    queryset = RegisterSerializer
