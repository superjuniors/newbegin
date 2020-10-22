from django.contrib import admin #导入Admin功能模块
from django.urls import path, include  #导入URL编写模块
from django.conf.urls import url, include  #导入URL编写模块
from . import views
from apps._index.views import FlowView

app_name = '_index'

urlpatterns = [
    path('', views._index,name="_index"),
    path('/flow/', FlowView.as_view(), name="flow"),


]