from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Shop

class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'content_size', 'created_at']

    def content_size(self, shop):
        return '%s자' % intcomma(len(shop.content))

admin.site.register(Shop, ShopAdmin)