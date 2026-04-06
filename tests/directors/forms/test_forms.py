from django.test import TestCase
from directors.forms import DirectorFormBasic, SearchDirectorForm

class DirectorFormTests(TestCase):
    def test_director_form_basic_valid_data(self):
        # Arrange
        form_data = {
            'name': 'Christopher Nolan',
            'description': 'A visionary director known for Inception and Interstellar.',
            'image_url': 'http://example.com/nolan.jpg'
        }
        
        # Act
        form = DirectorFormBasic(data=form_data)
        
        # Assert
        self.assertTrue(form.is_valid())

    def test_director_form_basic_missing_required_fields(self):
        # Arrange
        form_data = {}
        
        # Act
        form = DirectorFormBasic(data=form_data)
        
        # Assert
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('description', form.errors)
        self.assertIn('image_url', form.errors)
        
        # Verify custom error messages
        self.assertEqual(form.errors['name'][0], "Please enter the director's name.")
        self.assertEqual(form.errors['description'][0], "A brief biography of the director is needed.")
        self.assertEqual(form.errors['image_url'][0], "Provide a link to the director's photo.")

    def test_director_form_basic_name_too_short(self):
        # Arrange
        form_data = {
            'name': 'Ed', # Model validator MinLengthValidator(3)
            'description': 'Long enough description for validation.',
            'image_url': 'http://example.com/image.jpg'
        }
        
        # Act
        form = DirectorFormBasic(data=form_data)
        
        # Assert
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_director_form_basic_description_too_short(self):
        # Arrange
        form_data = {
            'name': 'Nolan',
            'description': 'Short', # Custom validator < 10 characters
            'image_url': 'http://example.com/image.jpg'
        }
        
        # Act
        form = DirectorFormBasic(data=form_data)
        
        # Assert
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors)

class SearchDirectorFormTests(TestCase):
    def test_search_form_valid_data(self):
        # Arrange
        form_data = {'query': 'Nolan'}
        
        # Act
        form = SearchDirectorForm(data=form_data)
        
        # Assert
        self.assertTrue(form.is_valid())

    def test_search_form_empty_data_is_valid(self):
        # Arrange
        form_data = {'query': ''}
        
        # Act
        form = SearchDirectorForm(data=form_data)
        
        # Assert
        self.assertTrue(form.is_valid()) # required=False
