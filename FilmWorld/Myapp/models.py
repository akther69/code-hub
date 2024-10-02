from django.db import models

# Create your models here.
class Film(models.Model):
    title=models.CharField(max_length=100)
    year=models.IntegerField()
    genre=models.CharField(max_length=30)
    director=models.CharField(max_length=50)
    tags=models.CharField(max_length=100)
    song_count=models.IntegerField()
    language=models.CharField(max_length=30)
    is_trending=models.BooleanField()