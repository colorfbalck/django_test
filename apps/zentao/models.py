
from django.db import models
from utils.base_models import BaseModel


class ZentaoConfig(BaseModel):
    url = models.CharField(verbose_name="禅道登录地址", max_length=500, help_text="禅道登录地址")

    class Meta:
        db_table = "zentao_url_config"
        verbose_name = "禅道登录地址配置信息"
        verbose_name_plural = verbose_name


class ZentaoUserConfig(BaseModel):
    account = models.CharField(verbose_name="账号", max_length=50, help_text="账号")
    password = models.CharField(verbose_name="密码", max_length=50, help_text="密码")
    zentaosid = models.CharField(verbose_name="ZentaoSid", max_length=200, help_text="ZentaoSid", default="")
    enable = models.IntegerField(verbose_name="是否启用", help_text="是否启用", default=0)

    class Meta:
        db_table = "zentao_login_user_config"
        verbose_name = "登录禅道账号相关配置信息"
        verbose_name_plural = verbose_name


class BugProjectConfig(BaseModel):
    project_id = models.CharField(verbose_name="项目ID", primary_key=True, max_length=50, help_text="项目ID")
    project_name = models.CharField(verbose_name="项目名称", max_length=100, help_text="项目名称")
    qywx_webhook = models.CharField(verbose_name="企业微信webhook推送地址", max_length=500,
                                    help_text="企业微信webhook推送地址", blank=True)
    status = models.CharField(verbose_name="是否推送状态", max_length=10, help_text="推送状态")

    class Meta:
        db_table = "zentao_project_config"
        verbose_name = "禅道项目推送消息相关配置"
        verbose_name_plural = verbose_name


class Bug(models.Model):
    bug_id = models.IntegerField(verbose_name="缺陷ID", help_text="缺陷ID")
    project_id = models.IntegerField(verbose_name="项目ID", help_text="项目ID")
    bug = models.JSONField(verbose_name="缺陷原始信息", help_text="缺陷原始信息")
    status = models.CharField(verbose_name="是否解决", max_length=10, help_text="是否解决")

    class Meta:
        db_table = "zentao_bug"
        verbose_name = "禅道保存的未解决BUG"
        verbose_name_plural = verbose_name


class BugPersonnelConfig(BaseModel):
    spell = models.CharField(verbose_name="拼音", primary_key=True, max_length=50, help_text="拼音")
    name = models.CharField(verbose_name="姓名", max_length=50, help_text="姓名")
    phone = models.CharField(verbose_name="手机号", max_length=50, help_text="手机号")

    class Meta:
        db_table = "zentao_personnel_spell"
        verbose_name = "人员信息拼音对照"
        verbose_name_plural = verbose_name

