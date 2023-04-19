"""demo_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="Lemon APi接口文档",
        default_version="v1",
        description="这是一个美轮美奂的接口文档",
        terms_of_service="http://api.keyou.site",
        contact=openapi.Contact(email="keyou100@qq.com"),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    # permission_classes=(permission.AlloAny,)
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.projects.urls')),
    path('doc/', include_docs_urls('Tz测试平台接口文档', description="这是一个美轮美奂的测试平台")),
    # path('api/', include('rest_framework.urls'))
    # re_path(r'swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_time)),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schem-')
    path('user/', include('apps.user.urls')),
    path('interfaces/', include('apps.interfaces.urls')),
    path('envs/', include('apps.envs.urls')),
    path('zentao/', include('apps.zentao.urls'))

]