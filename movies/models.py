from django.db import models

# Create your models here.
class Movies(models.Model):
    video = models.CharField(max_length=5000)  # same like models.URLField()
    title = models.CharField(max_length=50)