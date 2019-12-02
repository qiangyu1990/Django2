from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # 返回某个反馈
    # return HttpResponse("Hello Kelly yu")

    return render(request,'home.html')

# 对文字进行计算
def count(request):
    content = request.GET['text']
    tot_cnt = len(content)
    word_dict = {}
    for word in content:
        if word not in word_dict:
            word_dict[word] =1
        else:
            word_dict[word]+=1
    sort_word = sorted(word_dict.items(),key= lambda x:x[1],reverse=True)
    return render(request, 'count.html',{'wordcnt':tot_cnt,'text':content,'sort_word':sort_word})