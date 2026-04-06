from django.test import TestCase
from django.core.exceptions import ValidationError
from model_bakery import baker
from directors.models import Director

class DirectorModelTests(TestCase):
    def test_str_method_returns_name(self):

        name = "Christopher Nolan"
        director = baker.make(Director, name=name)


        self.assertEqual(str(director), name)

    def test_name_max_length(self):

        director = baker.make(Director)
        max_length = director._meta.get_field('name').max_length


        self.assertEqual(max_length, 100)

    def test_name_min_length_validator_raises_error(self):

        director = Director(
            name="Ed", # Less than 3 characters
            description="A very long description for testing purposes.",
            image_url="http://example.com/image.jpg"
        )


        with self.assertRaises(ValidationError):
            director.full_clean()

    def test_description_min_length_validator_raises_error(self):

        director = Director(
            name="Nolan",
            description="Short", # Less than 10 characters
            image_url="http://example.com/image.jpg"
        )


        with self.assertRaises(ValidationError):
            director.full_clean()

    def test_successful_creation(self):

        director = baker.make(Director, name="Christopher Nolan", description="A great director with a long description.")


        self.assertEqual(Director.objects.count(), 1)
        self.assertEqual(director.name, "Christopher Nolan")
