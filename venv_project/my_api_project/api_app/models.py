from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    email=models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=12)
    city = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.subject}"