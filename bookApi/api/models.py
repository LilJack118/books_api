from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=400, blank=False)
    authors = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    publishedDate = models.CharField(max_length=10,null=True)
    categories = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    ratings_count = models.FloatField(blank=True, null=True)
    thumbnail = models.URLField(null=True)
