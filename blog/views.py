from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Shop, Review
from .forms import ReviewForm
from django.contrib import messages

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

@login_required
def review_new(request, shop_pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review = form.save(commit=False)
            review.shop = get_object_or_404(Shop, pk=shop_pk)
            review.user = request.user
            review.save()
            message.success(request, '새로운댓글이등록')
            return redirect('blog:shop_detail', shop_pk)
    else:
        form = ReviewForm()
    return render(request, 'blog/review_form.html', {
        'form': form,
    })

@login_required
def review_edit(request, shop_pk, pk):
    revie = get_object_or_404(Review, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = get_object_or_404(Shop, pk=shop_pk)
            review.user = request.user
            review.save()
            message.success(request, '댓글이수정')
            return redirect('blog:shop_detail', shop_pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'blog/review_form.html', {
        'form': form,
    })