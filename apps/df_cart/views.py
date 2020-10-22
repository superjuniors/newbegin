from django.shortcuts import render
from django.http import HttpResponse


def user_cart(request):
    return render(request, 'df_cart/cart.html')