from django.db import models
from django.contrib.auth.models import User

def some_function():
    from .models import Product  # ✅ Import inside function


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    category = models.CharField(max_length=100, null=True, blank=True)  
    brand = models.CharField(max_length=100, null=True, blank=True)  
    description = models.TextField(null=True, blank=True)  
    sku = models.CharField(max_length=50, unique=True, null=True, blank=True)  # Example
    is_active = models.BooleanField(default=True)  


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return f"Cart {self.id} - {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity 