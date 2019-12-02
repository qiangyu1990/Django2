"""定义learning_logs的URL模式"""

from django.conf.urls import url
from django.urls import path
from learning_logs import views as log
from . import views

urlpatterns =[

    # 主页
    # path('notebook',log.index,name ='index'),
    # path('articles/<int:year>', log.article),

    # Home page.
    url(r'^$', views.index, name='index'),

    # Show all topics.
    url(r'^topics/$', views.topics, name='topics'),

]