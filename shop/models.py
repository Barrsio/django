from django.db import models

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
        