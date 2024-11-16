from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=90)
    password=models.CharField(max_length=90)
    def __str__(self):
        return self.name