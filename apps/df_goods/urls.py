from django.contrib import admin #导入Admin功能模块
from django.urls import path, include  #导入URL编写模块
from MyDjango import settings
from django.conf.urls import url, include  #导入URL编写模块
from . import views

app_name = 'df_goods'

urlpatterns = [
    url('^$', views.index, name="_index"),
    #导入视图index函数
    url('^index/$', views.index, name="index"),
]