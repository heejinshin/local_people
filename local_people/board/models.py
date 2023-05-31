from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    contents = models.TextField()
    wdate = models.DateTimeField()
    hit = models.IntegerField()


