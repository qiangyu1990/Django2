from django.contrib import admin

# Register your models here.
from app1.models import Person, Order


# 注册你的模型
class PersonAdmin(admin.ModelAdmin):
    list_display  = ("first_name", "last_name","created_at","update_at") # 显示内容
    list_filter =  ("first_name","last_name") # 过滤器
    search_fields = ("first_name","last_name") # 搜索域
    readonly_fields = ("first_name",)


admin.site.register(Person,PersonAdmin)