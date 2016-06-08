from django.contrib import admin
from .models import Shop

class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']



admin.site.register(Shop, ShopAdmin)