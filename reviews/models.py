from django.db import models


class Review(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=20)
    rating = models.IntegerField()
