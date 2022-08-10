from django.contrib import admin

# Register your models here.

from projects.models import Projects


class Projectsadmin(admin.ModelAdmin):
    """
    定义后台管理站点类
    指定在修改（新增）中需要显示的字段
    """
    fields = ('name', 'leader', 'tester', 'programmer', 'publish_app')

    # 指定要列出的字段
# #     list_display = ['name', 'leader', 'tester', 'publish_app']
# #
# #
# # # admin.site.register(Interface)
admin.site.register(Projects, Projectsadmin)
# admin.site.register(Person)
