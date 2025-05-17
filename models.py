from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    picture=models.ImageField(upload_to='image/')
    detail=models.CharField(max_length=255)
    picstar=models.ImageField(upload_to='image/')
    typeofcoffee=models.CharField(max_length=20, blank=True)
    quantity=models.IntegerField(blank=True)

#cart
from django.contrib.auth.models import User
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)