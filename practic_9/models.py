from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="book/%Y/%m/%d")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"


class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"