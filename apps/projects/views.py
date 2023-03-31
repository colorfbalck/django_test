import json

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
# Create your views here.
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, generics, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from apps.projects.models import Projects
from apps.projects.utils import get_count_by_project
from utils.pagination import PageNumberPaginationManual
from apps.projects.serializer import ProjectSerializer, ProjectModelSerializer, ProjectNameSerializer, \
    InterfaceNameSerializer, InterfaceByProjectIdSerializer
# def index(request):
#     """
#     函数视图
#     :parm request: request是HttpRuquest对象，包含前端用户的所有请求信息
#     :return: 必须返回一个HttpResponse对象或者子对象
#     """
#     if request.method == 'GET':
#         #  1.使用request.GET来获取查询字符串参数
#         #  2.request.GET返回的是一个类字典对象，支持字典中的所有操作
#         #  3.查询字符参数中，如果有多个相同的key，使用request.GET获取的未最后一个值
#         #  4.使用request.GET.getlist（“name”）可以获取多个相同key的值
#         return HttpResponse("<h1>GET请求:hello，world，测开大佬们</h>")
#     elif request.method == 'POST':
#         return HttpResponse("<h1>POST请求:hello，world，测开大佬们</h>")
#     else:
#         return HttpResponse("<h1>OTHER请求:hello，world，测开大佬们</h>")


# 类视图
# class IndexView(View):
#     """
#     index 主页视图
#     """
#     def get(self, request):
#         # 创建数据
#         # 方法一
#
#         # obj_ = Projects(name='项目二', leader='icon1', programmer='海泽王2', publish_app='wljk_app', desc='描述')
#         # obj_.save()
#
#         # 方法二
#         # Projects.objects.create(name='这是牛逼的项目二', leader='tttt', programmer='海泽王3', publish_app='HHHH')
#         # pass
#         # HttpResponse第一个参数往往为响应体内容
#         # return HttpResponseHttpResponse("<h1>GET请求:hello，world，测开大佬们{}</h>".format(pk))
#         # return JsonResponse()
#
#         # 1.获取一个数据所有记录
#         # QuerySet查询集，相当于一个列表存放了每个项目的对象
#         # Projects.objects.all()
#         # data = Projects.objects.all()
#         # # print(data[0].leader)
#         # for i in data:
#         #     print(f"{type(i)}")
#         #     print(f"{i.name}")
#
#         # 获取某一个指定的记录 get()
#         # get 方法只能返回一条记录
#         # 如果返回多条记录或者查询的记录不存在会抛异常
#         # get犯法的参数通常用于主键
#         # one_project = Projects.objects.get(id=2)
#
#         # 获取某一些记录，filter()或者exclude()
#         # 使用filter返回是满足条件之后的queryset集，exclude是不满足条件的queryset集
#         # 模型类属性（字段名）__contains将包含指定字符串的所有记录返回
#         # leader__icontains 忽略大小写
#         # 将startswith以给定字符串开头的所有记录返回
#         # 将endswith以给定字符串结尾的所有记录返回
#         # 将in以给定返回字符串的所有记录返回
#         # qs = Projects.objects.filter(leader__contains='icon')
#         # qs = Projects.objects.filter(leader__icontains='icon')
#         # qs = Projects.objects.filter(leader__startswith='ic')
#         # qs = Projects.objects.filter(leader__endswith='n')
#         # qs = Projects.objects.filter(leader__in=['icon'])
#
#         # 关联查询
#         # 外键字段__从表的字段名__contains
#         # qs = Projects.objects.filter(interface__interface_name='登录')
#
#         # 比较查询
#         # __gt 大于
#         # __gte 大于等于
#         # __lt 小于
#         # __lte 小于等于
#         # qs =  Projects.objects.filter(id_gt=2)
#
#         # 逻辑关联，多个条件查询
#         # 如果给filter指定的多个条件，那么条件之间是与的关系
#         qs = Projects.objects.filter(Q(leader='icon') | Q(name__icontains="伟大"))
#
#         # 查询集的操作
#         # 查询集相当于一个列表，支持列表中的大多数操作（通过数字索引去取值，正向切片，for）
#         # 查询集是对数据库操作的一种优化
#         # 查询集会缓存结果
#         # 惰性查询
#         # 查询集还支持链式操作
#
#
#         # 更新操作
#         # 先获取到要修改的模型对象
#         # 然后修改
#         # 保存
#         # one_project = Projects.objects.get(id=1)
#         # one_project.leader = '女女'
#         # one_project.save()
#
#         # qs = Projects.objects.filter(name__contains='牛逼')
#         # one_project = qs.first()
#         # one_project.delete()
#
#         # 排序操作
#         Projects.objects.filter(id__gte=3).order_by('name')
#
#         return JsonResponse()
#
#     def post(self, request):
#         #post 请求
#         return HttpResponse("<h1>POST请求:hello，world，测开大佬们</h>")
#
#     def delete(self, request):
#         #post 请求
#         return HttpResponse("<h1>delete请求:hello，world，测开大佬们</h>")
#
#     def put(self, request):
#         #post 请求
#         return HttpResponse("<h1>put请求:hello，world，测开大佬们</h>")

class ProjectList(View):

    def get(self, request):
        # 1. 从数据库中获取所有的项目信息
        project_qs = Projects.objects.all()
        project_list = []
        for project in project_qs:
            project_list.append({
                'name': project.name,
                'leader': project.leader,
                'tester': project.tester,
                'programmer': project.programmer,
                'publish_app': project.publish_app,
                'desc': project.desc,

            })
        # JsonResponse第一个参数默认只能为dict字典，如果设为其他类型，需要将safe设置为false
        # 如果返回的是列表数据（多条数据）是，那么需要提那就many=True这个参数
        serializer = ProjectSerializer(instance=project_qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    # def post(self, request):
    #     """
    #     新增项目
    #     1.从前端获取json格式的数据，转化为Python中的类型
    #     2.为了严谨性，这里需要做各种校验
    #     # 比如：是否为json、传递的项目数据是否符合要求，有些必填项参数数据
    #     """
    #     json_data = request.body.decode('utf-8')
    #     python_data = json.loads(json_data, encoding='utf-8')
    #
    #     # 2.向数据库添加数据
    #     # new_project = Projects.objects.create(name=python_data['name'],
    #     #                                       leader=python_data['leader'],
    #     #                                       tester=python_data['tester'],
    #     #                                       programmer=python_data['programmer'],
    #     #                                       publish_app=python_data['publish_app'],
    #     #                                       desc=python_data['desc'],
    #     #                                       )
    #     project = Projects.objects.create(**python_data)
    #
    #     # 3.将模型类对象转化为字典，然后返回
    #     one_dict = {
    #             'name': project.name,
    #             'leader': project.leader,
    #             'tester': project.tester,
    #             'programmer': project.programmer,
    #             'publish_app': project.publish_app,
    #             'desc': project.desc,
    #
    #         }
    #     return JsonResponse(one_dict, safe=False)
    def post(self, request):
        """
        新增项目
        1.从前端获取json格式的数据，转化为Python中的类型
        2.为了严谨性，这里需要做各种校验
        # 比如：是否为json、传递的项目数据是否符合要求，有些必填项参数数据
        """
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')
        serializer = ProjectSerializer(data=python_data)
        # 校验前端输入数据
        # 1.调用序列化器对象的is_valid方法，开始校验前端参数
        # 如果叫校验成功，则返回True，校验失败则返回False
        # raise_exception=True， 那么校验失败后，会抛出异常
        # 当调用is_valid方法之后，才可以调用errors属性，获取校验的错误提示（字典）
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors)
        # 校验成功之后的数据，可以使用validated_data属性来获取
        # 向数据库中新增项目
         # 1.如果在创建序列化器对象的时候，只给data传参，那么调用save（）方法，
        # 实际调用的就是事实序列化器的create（）方法
        serializer.save(name='孤影', age=14)
        # 3.将模型类对象转化为字典，然后返回
        # one_dict = {
        #         'name': project.name,
        #         'leader': project.leader,
        #         'tester': project.tester,
        #         'programmer': project.programmer,
        #         'publish_app': project.publish_app,
        #         'desc': project.desc,
        #
        #     }
        # ser = ProjectSerializer(project)
        return JsonResponse(serializer.data, safe=False)


class ProjectsDetail(View):

    def get_object(self, pk):
        try:
            return Projects.objects.get(id=pk)
        except Projects.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        获取单个项目详情
        1.校验前端传递的pk（项目ID）值，类似是否正确（正整数），在数据库中是否存在
        2.获取指定pk值的项目
        3.将模型类对象转化为字典
        """
        project = self.get_object(pk)
        # 3.将模型类对象转化为字典，然后返回
        # one_dict = {
        #     'name': project.name,
        #     'leader': project.leader,
        #     'tester': project.tester,
        #     'programmer': project.programmer,
        #     'publish_app': project.publish_app,
        #     'desc': project.desc,
        #
        # }
        # 1.通过模型类对象（或查询集），传给instance可进行序列化操作
        # 2.通过序列化器ProjectSerializer对象的data属性，就可以获取转化之后的字典
        ser = ProjectSerializer(instance=project)
        return JsonResponse(ser.data)

    def put(self, request,  pk):
        project = self.get_object(pk)
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')
        serializer = ProjectSerializer(instance=project, data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors)
        # 在创建序列化器对象是，如果同给instance和data传参
        # 那么调用save()方法，会自动化调用序列化器的updatae
        # serializer.save()
        return JsonResponse(serializer.data, status=201)

    def delete(self, request, pk):
        # 1.校验前端传递的pk（项目ID）值，类型是否正确(正整数)，在数据库中是否存在等
        # 2.获取指定ID为pk的项目
        project = self.get_object(pk)
        project.delete()
        return JsonResponse(None, safe=False, status=204)


class ProjectsDetail_GenericAPIView(GenericAPIView):
    # 2.必须指定queryset和serializer_class
    # queryset用于指定需要使用的查询集
    queryset = Projects.objects.all()
    # serializer_class 指定需要使用到的序列化器
    serializer_class = ProjectModelSerializer
#     使用lookup_fied类属性，可以修改主键路由名称
    look_field = 'id'
    # GenericAPIView 提供get_object方法
    # def get_object(self, pk):
    #     try:
    #         return Projects.objects.get(id=pk)
    #     except Projects.DoesNotExist:
    #         raise Http404

    def get(self, request):
        """
        project = self.get_object(pk)
        无需自定义.get_object方法
        使用get_object方法，返回详情视图所需的模型类对象
        """
        project = self.get_object()
        # 3.将模型类对象转化为字典，然后返回
        ser = self.get_serializer(instance=project)
        # 如果前端请求中未指定Accept，那么默认返回json格式数据
        return JsonResponse(ser.data, status=200)

    def put(self, request):
        project = self.get_object()
        # json_data = request.body.decode('utf-8')
        # python_data = json.loads(json_data, encoding='utf-8')
        serializer = self.get_serializer(instance=project, data=project)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(serializer.errors)
        # 在创建序列化器对象是，如果同给instance和data传参
        # 那么调用save()方法，会自动化调用序列化器的updatae
        serializer.save()
        return JsonResponse(serializer.data, status=201)

    def delete(self, request):
        # 1.校验前端传递的pk（项目ID）值，类型是否正确(正整数)，在数据库中是否存在等
        # 2.获取指定ID为pk的项目
        project = self.get_object()
        project.delete()
        return JsonResponse(None, safe=False, status=204)


class ProjectList_GenericAPIView(GenericAPIView):
    # 1.指定查询集
    queryset = Projects.objects.all()
    # 2.指定序列化器
    serializer_class = ProjectModelSerializer
    # 3.在视图类中指定过滤引擎
    # filter_backends = [filters.OrderingFilter]
    # 4.指定需要排序的字段
    ordering_fields = ['name', 'leader']
    # 5.在类视图中指定过滤引擎
    # filter_backends = [DjangoFilterBackend]
    # 6.指定需要过滤的字段
    filterset_fields = ['name', 'leader', 'tester']
    # 7.在某个视图中指定分页类
    pagination_class = PageNumberPaginationManual

    def get(self, request):
        # 使用get_queryset获取查询集
        # project_qs = self.get_queryset()
        # 使用filter_queryset方法进行过滤
        project_qs = self.filter_queryset(self.get_queryset())
        # 使用paginate_queryset 来进行分页，然后返回分页之后的查询集
        page = self.paginate_queryset(project_qs)
        if page is not None:
            ser = self.get_serializer(instance=project_qs, many=True)
            # 可以get_paginated_response返回
            self.get_paginated_response(ser.data)
        ser = self.get_serializer(instance=project_qs, many=True)
        return Response(ser.data)


class ProjectList_mixins_ListModelMixin(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    # 1.指定查询集
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer
    # 2.指定排序对象
    # 3.指定过滤对象
    ordering_fields = ['name', 'leader']
    filterset_fields = ['name', 'leader', 'tester']

    def get(self, request, *args, **kwargs):
       return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectsDetail_mixins_RetrieveModelMixin(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                                               mixins.DestroyModelMixin, GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    def get(self, request, *args, **kwargs):
        self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)


class ProjectList_generics(generics.ListCreateAPIView):

    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    ordering_fields = ['name', 'leader']
    filterset_fields = ['name', 'leader', 'tester']


class ProjectsDetail_generics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer


# APIView
# GenericAPIView
# ViewSet不再支持get、psot、put、delet等请求方法、而只支持action动作
# 但是ViewSet中未提供get_object(),get_serializer()等方法
# 所有需要继承GenericViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    """
    项目视图
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer
    ordering_fields = ['name', 'leader']
    filterset_fields = ['name', 'leader', 'tester']
    # permission_classes = [permissions.IsAuthenticated]

    # 1.可以使用action装饰器来声明自定义的动作
    # 默认情况下，实例化方法名就是动作名
    # methods参数用于指定该动作支持的请求方法，默认为get
    # detail参数用于指定该动作要处理的是否为详情对象（url是否需要传递pk值）
    @action(methods=["get"], detail=False)
    def names(self, request):
        queryset = self.get_queryset()
        serializer = ProjectNameSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def interfaces(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = InterfaceByProjectIdSerializer(instance=instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas = serializer.data
            datas = get_count_by_project(datas)
            return self.get_paginated_response(datas)

        serializer = self.get_serializer(queryset, many=True)
        datas = serializer.data
        datas = get_count_by_project(datas)
        return self.get_paginated_response(datas)