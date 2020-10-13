from django.shortcuts import render
from django.http import HttpResponse

def _index(request):
    return HttpResponse("hello world")