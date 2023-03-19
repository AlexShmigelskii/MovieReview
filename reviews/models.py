from django.db import models


class Review(models.Model):
    text = models.TextField()
    sentiment = models.BooleanField()
    rating = models.IntegerField()
