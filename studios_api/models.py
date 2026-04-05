from django.db import models


class Studio(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField('movies.Movie',related_name='studios_api')