from django.db import models


# define created_at 、updated_at
class CreateUpdate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # 定义Meta,并设置abstaract为True,这样设置避免显示CreateUpdate表
    class Meta:
        abstract = True

# Create your models here.
class Person(CreateUpdate):
    #first_name,last_name,craete_at,update_at
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Order(CreateUpdate):
    # order_id,order_date,create_at,updated_at
    order_id = models.CharField(max_length=30,db_index= True)
    order_desc = models.CharField(max_length= 120)


