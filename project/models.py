from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    size = models.ManyToManyField(Size)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    color = models.ManyToManyField(Color)
    def __str__(self):
        return self.name

class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.name
class Meta:
    unique_together = (('user', 'product'),)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()             # Оценка
    comment = models.CharField(max_length=300)

    def __str__(self):
        return f"отзыв на {self.product.name}- {self.rating}/5"


