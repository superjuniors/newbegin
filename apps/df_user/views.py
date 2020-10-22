from django.shortcuts import render

# Create your views here.
def register(request):

    context = {
        'title': '用户注册',
    }
    return render(request, 'df_user/base.html')
