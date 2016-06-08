from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.TextField()
    address = models.TextField()
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


