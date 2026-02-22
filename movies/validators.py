from django.core.exceptions import ValidationError
from django.utils.timezone import now

def validate_runtime_positive(value):
    if value <= 0:
        raise ValidationError('Runtime must be a positive number of minutes.')


def validate_release_year(value):
    if value < 1888:
        raise ValidationError("Movies didn't exist before 1888, please enter a valid release date.")

    if value > now().year +5:
        raise ValidationError("Release date cannot be in the far future, please enter a valid release date.")