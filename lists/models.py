from django.core.validators import MinLengthValidator
from django.db import models

from django.db import models

from common.validators import validate_description_length


class List(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3, 'Enter a name for the list with at least three characters. Example: Fav')]
    )
    description = models.TextField(validators=[validate_description_length])
    movies = models.ManyToManyField('movies.Movie', related_name='lists', blank=True)

    def __str__(self):
        return self.name
