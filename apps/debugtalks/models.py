from django.db import models
from utils.base_models import BaseModel


class Debugtalks(BaseModel):
    id = models.AutoField(verbose_name="id主键", primary_key=True, help_text="id主键")
    name = models.CharField(verbose_name="debugtalk文件名称", max_length=50, unique=True, help_text="debugtalk文件名称")
    debugtalk = models.TextField(null=True, default='#debugtalk.py',  help_text="debugtalk文件名称")
    project = models.OneToOneField("projects.Projects", on_delete=models.CASCADE, related_name="debugtalks",
                                   help_text="所属项目")

    class Meta:
        db_table = "tb_debugtalks"
        verbose_name = "debugtalk文件名称"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
