from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from learning_logs.models import Topic


# Create your views here.

def index(request):
    """定义笔记的主页"""
    return render(request,'index.html')


def article(request,year):
    content = "The year is {0}".format(year)
    return HttpResponse(content)


def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by("date_added")
    context ={"topics":topics}
    return render(request,"learning_logs/topics.html",context)