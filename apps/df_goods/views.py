from django.shortcuts import render
from django.http import HttpResponse

#index函数主要负责首页的展示
#改为与html相连！！不使用httpresponse生成返回值，而使用render
def index(request):
    #return HttpResponse("hello world")
    return render(request, 'df_goods/index.html')

#search负责域名的查找功能，add则负责域名的添加功能。