from django.core.exceptions import ValidationError
def validate_description_length(value):
    if value and len(value) < 10:
        raise ValidationError('Please enter a description that is at least 10 characters long.')