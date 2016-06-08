from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.shop_detail, name='shop_detail'),
    url(r'^(?P<shop_pk>\d+)/reviews/new/$', views.review_new, name='review_new'),
]