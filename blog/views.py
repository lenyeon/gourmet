from django.shortcuts import get_object_or_404, redirect, render
from .models import Shop
from .forms import ReviewForm

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

def review_new(request, shop_pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('blog:shop_detail', shop_pk)
    else:
        form = ReviewForm()
    return render(request, 'blog/review_form.html', {
        'form': form,
    })