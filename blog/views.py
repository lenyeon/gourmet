from django.shortcuts import render
from .models import Shop

def index(request):
    shop_list = Shop.objects.all()
    return render(request, 'blog/index.html', {
        'shop_list': shop_list,
    })