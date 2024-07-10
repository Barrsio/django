from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        
class Book(models.Model):
    name_book = models.CharField(max_length=200)
    name_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.DateField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
    