from django.shortcuts import render
from django.http import HttpResponse

#index函数
#改为与html相连！！不使用httpresponse生成返回值，而使用render
def index(request):
    return HttpResponse("hello world")