
from django.db import models
from utils.base_models import BaseModel


class ZentaoConfig(BaseModel):
    url = models.CharField(verbose_name="禅道登录地址", max_length=500, help_text="禅道登录地址")

    class Meta:
        db_table = "tbl_zentao_config"
        verbose_name = "禅道配置信息"
        verbose_name_plural = verbose_name


class ZentaoUserConfig(BaseModel):
    account = models.CharField(verbose_name="账号", max_length=50, help_text="账号")
    password = models.CharField(verbose_name="密码", max_length=50, help_text="密码")
    zentaosid = models.CharField(verbose_name="ZentaoSid", max_length=200, help_text="ZentaoSid", default="")
    enable = models.IntegerField(verbose_name="是否启用", help_text="是否启用", default=0)

    class Meta:
        db_table = "tbl_zentao_user_config"
        verbose_name = "禅道用户配置信息"
        verbose_name_plural = verbose_name


class BugProjectConfig(BaseModel):
    project_id = models.CharField(verbose_name="项目ID", primary_key=True, max_length=50, help_text="项目ID")
    project_name = models.CharField(verbose_name="项目名称", max_length=100, help_text="项目名称")
    qywx_webhook = models.CharField(verbose_name="企业微信webhook推送地址", max_length=500,
                                    help_text="企业微信webhook推送地址", blank=True)
    status = models.CharField(verbose_name="是否推送状态", max_length=10, help_text="推送状态")

    class Meta:
        db_table = "tbl_zentao_bug_config"
        verbose_name = "bug推送配置"
        verbose_name_plural = verbose_name


class Bug(BaseModel):
    id = models.AutoField(verbose_name="ID主键", primary_key=True, help_text="ID主键")
    project_id = models.ForeignKey(to='BugProjectConfig', on_delete=models.CASCADE, to_field="project_id",
                                   verbose_name="所属项目ID", help_text="所属项目ID")
    bug_id = models.IntegerField(verbose_name="缺陷id", help_text="缺陷id")
    bug = models.JSONField(verbose_name="缺陷原始信息", help_text="缺陷原始信息")
    isread = models.CharField(verbose_name="是否读取", max_length=10, help_text="是否读取")

    class Meta:
        db_table = "tbl_zentao_bug"
        verbose_name = "BUG原始信息"
        verbose_name_plural = verbose_name


class BugStatus(BaseModel):
    id = models.AutoField(verbose_name="id主键", primary_key=True, help_text="id主键")
    project_id = models.ForeignKey(to='BugProjectConfig', on_delete=models.CASCADE, to_field="project_id",
                                   verbose_name="所属项目ID", help_text="所属项目ID", blank=True)
    unresolved_bug = models.CharField(verbose_name="未解决BUG", max_length=20, help_text="未解决BUG")
    toclosed_bug = models.CharField(verbose_name="待关闭BUG", max_length=20, help_text="待关闭BUG")
    send_status = models.CharField(verbose_name="发送状态", max_length=10, help_text="发送状态")
    send_time = models.DateTimeField(verbose_name="发送时间", help_text="发送时间")
    query_time = models.DateTimeField(verbose_name="查询时间", help_text="查询时间")
    account = models.CharField(verbose_name="操作用户", max_length=50, help_text="操作用户")
    severity_one = models.IntegerField(verbose_name="严重等级-一级", help_text="严重等级-一级")
    severity_two = models.IntegerField(verbose_name="严重等级-二级",  help_text="严重等级-二级")
    severity_three = models.IntegerField(verbose_name="严重等级-三级", help_text="严重等级-三级")
    severity_four = models.IntegerField(verbose_name="严重等级-四级", help_text="严重等级-四级")
    assignedTo = models.CharField(verbose_name="指派人", max_length=20, help_text="指派人")
    severity_one_title = models.CharField(verbose_name="严重等级一级BUG标题", max_length=500, help_text="严重等级一级BUG标题")
    severity_one_url = models.CharField(verbose_name="严重等级一级BUGURL", max_length=500, help_text="严重等级一级BUGURL")

    class Meta:
        db_table = "tbl_zentao_bug_status"
        verbose_name = "BUG状态信息"
        verbose_name_plural = verbose_name


class BugPersonnelConfig(BaseModel):
    id = models.AutoField(verbose_name="ID主键", primary_key=True, help_text="ID主键")
    spell = models.CharField(verbose_name="拼音", max_length=50, help_text="拼音")
    name = models.CharField(verbose_name="姓名", max_length=50, help_text="姓名")
    phone = models.CharField(verbose_name="手机号", max_length=50, help_text="手机号")

    class Meta:
        db_table = "tbl_zentao_bug_personnel_config"
        verbose_name = "BUG状态信息"
        verbose_name_plural = verbose_name

