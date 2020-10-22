from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def _index(request):
    return render(request, '_index/index.html')

class FlowView(View):
    def _index(request):
        return render(request, '_index/index.html')
