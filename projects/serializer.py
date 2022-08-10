# -*- coding: utf-8 -*-
# @Time    : 2022/7/13 21:51
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : serializer.py
# @Software: PyCharm
from rest_framework import serializers
from projects.models import Projects
from projects.models import Interface
# 1.继承Serializer类或者子类
from rest_framework.validators import UniqueValidator


def is_uninuqe_project_name(name):
    if '项目' not in name:
        raise serializers.ValidationError('项目名称中必须包含”项目”')


class ProjectSerializer(serializers.Serializer):
    """
    创建项目序列化器类
    """
    # 1.序列化器中定义德 类属性字段往往与模型类字段一一对应
    # 2.lable选项相当于verbose_name， help_text
    # 3.定义的序列化器字段，默认即可以进行序列化输出，也可以进行反序列化输入
    # 4.read_only=True，指定该字段只能进行序列化输出
    # 5.write_only=True，指定该字段只进行反序列化输入，但不进行序列化输出
    # 6.需要输出那些字段，那么在序列化器中就定义那些字段
    id = serializers.IntegerField(label="ID", read_only=True)
    # write_only = True, 指定改字段只进行反序列化输入，但不进行序列化输出
    name = serializers.CharField(label="项目名称", max_length=200, help_text="项目名称",
                                 validators=[UniqueValidator(queryset=Projects.objects.all(), message="项目名称重复"),
                                             is_uninuqe_project_name])
    leader = serializers.CharField(label="负责人", max_length=50, help_text="负责人")
    tester = serializers.CharField(label="测试人员", max_length=50, help_text="测试人员")
    programmer = serializers.CharField(label="开发人员", max_length=50, help_text="开发人员")
    publish_app = serializers.CharField(label="应用名称", max_length=100, help_text="应用名称")
    # allow_null 相当于模型类中的null、allow_blank相当于模型类中blank
    desc = serializers.CharField(label="简要描述", help_text="简要描述", allow_blank=True, allow_null=True, default="TEST")

    # 单字段校验
    # 字段校验器的顺序
    # 字段定义时的限制（包含validators列表条目从左到右进行校验）-> 单字段的校验(validate_字段) -> 多字段联合校验（validate）
    # 单字段的校验器，validate_字段名称
    def validate_name(self, value):
        if not value.endswith('项目'):
            raise serializers.ValidationError('项目名称必须以“项目”结尾')
        return value

    def validate(self, attrs):
        if "icon" not in attrs['tester'] and 'icon' not in attrs['leader']:
            raise serializers.ValidationError('icon必须是项目负责人或者测试人员')
        return attrs

    def create(self, validated_data):
        return Projects.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.leader = validated_data['leader']
        instance.tester = validated_data['tester']
        instance.programmer = validated_data['programmer']
        instance.publish_app = validated_data['publish_app']
        instance.desc = validated_data['desc']
        instance.save()
        return instance


class ProjectModelSerializer(serializers.ModelSerializer):
    # 修改字段属性后，覆盖
    name = serializers.CharField(label="项目名称", max_length=200, help_text="项目名称",
                                 validators=[UniqueValidator(queryset=Projects.objects.all(), message="项目名称重复"),
                                             is_uninuqe_project_name])

    class Meta:
        """
        1.指定参考哪一类型来创建
        2.指定为模型类型的那些字段来生成序列化器
        3.自动创建create 和update
        """
        model = Projects
        fields = "__all__"
        # 自定义需要的字段类型
        # fields = ('id', 'name', 'leader', 'tester', 'programmer')
        # 排除不需要的的字段
        # exclude = ('publish_app', 'desc')
        # 修改字段属性
        # extra_kwargs = {
        #     'leader': {
        #         'write_only': True,
        #         'error_messages': {'max_length': '最大长度不能超过50个字节'}
        #     }
        # }

#


class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ("id", "name")


class InterfaceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface
        fields = ("id", 'interface_name', "tester", "leader")


class InterfaceByProjectIdSerializer(serializers.ModelSerializer):
    interfaces_set = InterfaceNameSerializer(read_only=True, many=True)

    class Meta:
        model = Projects
        fields = ("id", 'interfaces_set')
