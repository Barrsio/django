from django.db import models

# Create your models here.


        
class Course(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        
class Student(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
    