from django.shortcuts import get_object_or_404, render
from .models import Shop

def index(request):
    shop_list = Shop.objects.all()
    return render(request, 'blog/index.html', {
        'shop_list': shop_list,
    })

def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'blog/shop_detail.html', {
        'shop': shop,
    })
