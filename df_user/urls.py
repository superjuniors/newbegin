from django.contrib import admin #导入Admin功能模块
from django.urls import path, include  #导入URL编写模块
from django.conf.urls import url, include  #导入URL编写模块
from . import views
from .views import *

app_name = 'df_user'

urlpatterns = [
    url(r'^register/$', register, name="register"),
]