from django.shortcuts import render
from django.http import HttpResponse


def order(request):
    return HttpResponse("hello world")