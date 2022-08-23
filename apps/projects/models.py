from django.db import models

# Create your models here.


# 1.每一个应用下的数据库模型类，需要在当前应用下的models.py文件中定义
# 2.一个数据模型相当于一个数据表（Table）
# 3.一个数据模型类需要继承Model或者Model的子类
from utils.base_models import BaseModel


class Person(models.Model):
    """创建Person类
    4.定义的一个类属性，就相当于数据库表中的一个字段
    5.默认会创建一个自动低增的id主键
    6.默认创建的数据库名为应用名小写——数据库模型类小写
    7.max_length为字段的最大长度
    8.unique参数用于设置当前字段是否唯一，默认unique=False 可重复
    9.verbose_name 用于设置字段注释
    10.help_text 主要用于api文档中的中文名称
    11.null设置数据库中此字段允许为空
    12.blank 用于设置前端可以不传递
    13. default 默认值设置
    """
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)


# class Projects(models.Model):
#     """
#     创建Project模型类型
#     """
#     name = models.CharField(verbose_name="项目名称", max_length=200, unique=True, help_text="项目名称")
#     leader = models.CharField(verbose_name="负责人", max_length=50, help_text="负责人")
#     tester = models.CharField(verbose_name="测试人员", max_length=50, help_text="测试人员")
#     programmer = models.CharField(verbose_name="开发人员", max_length=50)
#     publish_app = models.CharField(verbose_name="应用名称", max_length=100, help_text="应用名称")
#     desc = models.TextField(verbose_name="简要描述", help_text="简要描述", blank=True, null=True, default="TEST")
#     # models.ImageField(choices=["test", "test23"])
#
#     # 定义子类Meta，用于设置当前数据库模型的元数据信息
#     class Meta:
#         db_table = "tbl_projects"
#         # 会在admin站点中，显示一个更人性化的表名
#         verbose_name = "项目"
#         verbose_name_plural = "项目"
#
#     def __str__(self):
#         return self.name

class Projects(BaseModel):
    id = models.AutoField(verbose_name="id主键", primary_key=True, help_text="id主键")
    name = models.CharField(verbose_name="项目名称", max_length=200, unique=True, help_text="项目名称")
    leader = models.CharField(verbose_name="负责人", max_length=50, help_text="负责人")
    tester = models.CharField(verbose_name="测试人员", max_length=50, help_text="测试人员")
    programmer = models.CharField(verbose_name="开发人员", max_length=50)
    publish_app = models.CharField(verbose_name="应用名称", max_length=100, help_text="应用名称")
    desc = models.TextField(verbose_name="简要描述", help_text="简要描述", blank=True, null=True, default="TEST")

    # 定义子类Meta，用于设置当前数据库模型的元数据信息
    class Meta:
        db_table = "tbl_projects"
        verbose_name = "项目"
        verbose_name_plural = "项目"

    def __str__(self):
        return self.name

# 一个项目中有多个接口
# 那么需要在”多“的一侧创建外键
# 项目表为父表（”一”），接口表（“多”）为子表
class Interface(models.Model):
    """

    """
    interface_name = models.CharField(verbose_name="接口名称", max_length=200, unique=True, help_text="项目名称")
    leader = models.CharField(verbose_name="负责人", max_length=50, help_text="负责人")
    tester = models.CharField(verbose_name="测试人员", max_length=50, help_text="测试人员")
    # 第一个参数为关联的模型路径（应用名.模型表）或者模型类
    # 第二个参数设置的是，当父表删除之后，改字段的处理方式
    # CASCADE -->子表也会被删除
    # SET_NULL -->当前外键值会被设置为None
    # PROJECT -->会报错
    # SET_DEFAULT -->设置默认值， 同时需要指定默认值， null=True
    project = models.ForeignKey('Projects', on_delete=models.CASCADE, verbose_name="所属项目", help_text='所属项目')

    # 定义子类Meta，用于设置当前数据库模型的元数据信息
    class Meta:
        db_table = "tbl_interface"
        # 会在admin站点中，显示一个更人性化的表名
        verbose_name = "接口测试"
        verbose_name_plural = "接口测试"
