from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=1000, blank=False)
    authors = ArrayField(models.CharField(max_length=2000), blank=True, null=True)
    publishedDate = models.CharField(max_length=100,null=True)
    categories = ArrayField(models.CharField(max_length=2000), blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    ratings_count = models.FloatField(blank=True, null=True)
    thumbnail = models.URLField(null=True, blank=True,default=None)
