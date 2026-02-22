from django.db import models

from django.db import models

from common.validators import validate_description_length


class Director(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(validators=[validate_description_length])
    image_url = models.URLField()


    def __str__(self):
        return self.name
