from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
class Image(models.Model):
    name = models.CharField(max_length=200)
    image = image = models.ImageField(upload_to="book/%Y/%m/%d")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    sale_price = models.IntegerField()
    rating = models.SmallIntegerField(max_length=5)
    count_reviews = models.IntegerField()
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        
class Gender(models.TextChoices):
    MEN = "Мужской"
    WOMEN = "Женский"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=Gender, blank=True, max_length=20)
    
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    house = models.CharField(max_length=100, blank=True)
    apartment_number = models.CharField(max_length=100, blank=True)
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        