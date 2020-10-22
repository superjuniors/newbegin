from django.shortcuts import render
from django.http import HttpResponse


def order(request):
    return render(request, 'df_order/order.html')