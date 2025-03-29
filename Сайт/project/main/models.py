from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Student(models.Model):
    Initials = models.CharField(max_length = 50)
    Age = models.CharField(max_length = 50)
    Speciality = models.CharField(max_length = 50)
    Clas = models.CharField(max_length = 50)


    def __str__(self):
        return self.Initials
    
    class Meta:
        verbose_name = 'Ученики'
        verbose_name_plural ='Ученики'
   

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title