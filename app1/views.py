from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from app1.forms import PersonForm
from app1.models import Person
from django.views import View

# Create your views here.
def person_detail(request,pk):
    try:
        #获取模型的id主键
        obj = Person.objects.get(pk =pk)
    except Person.DoesNotExist:
        raise Http404("Person Does Not Exist")
    return render(request,"person_detail.html",{'person':obj})



def article(request,year):
    content = "The year is {0}".format(year)

    return HttpResponse(content)


# render 进行渲染
def get_name(request):
    # 判断是post提交还是get
    if request.method =="POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            first_name =form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            return HttpResponse(first_name+" " + last_name)
        else:
            return HttpResponseRedirect("/error/")

    else:
        # 添加一个字典
        # return  HttpResponse("Nothing")
        return render(request,'name.html',{'form':PersonForm()})

# 定义视图类
class PersonFormView(View):
    form_class = PersonForm
    initial = {'key':'value'}
    template_name = 'name.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,
                      {'form':self.form_class(initial =self.initial)})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            return HttpResponse(first_name+" "+last_name)
        # 表单无效，返回表单
        return render(request,self.template_name,{'form':form})