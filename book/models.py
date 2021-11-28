from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    volume = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    total_page = models.IntegerField(default=0)
    publisher = models.CharField(max_length=200)
    published_date = models.DateTimeField('date published')

