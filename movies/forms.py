from django import forms

from common.mixins import DisableFormFieldsMixin
from movies.models import Movie


class MovieFormBasic(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['slug']


        widgets = {
            "title": forms.TextInput(attrs={'placeholder': 'Inception'}),
            "tagline": forms.TextInput(attrs={'placeholder': 'Your mind is the scene of the crime'}),
            "description": forms.Textarea(attrs={'placeholder': 'Description of this movie goes here'}),
        }
        error_messages = {
            'title': {
                'required': 'The movie title is required.',
            },
            'release_year': {
                'required': 'Please enter the release year.',
            },
            'genre': {
                'required': 'Please select a genre for the movie.',
            },
            'image_url': {
                'required': 'An image URL for the movie poster is required.',
            },
            'runtime': {
                'required': 'Please enter the movie\'s runtime in minutes.',
            },
            'director': {
                'required': 'Please select a director for the movie.',
            },
        }

class MovieCreateForm(MovieFormBasic):
    ...

class MovieUpdateForm(MovieFormBasic):
    ...

class MovieDeleteForm(DisableFormFieldsMixin, MovieFormBasic):
    ...


class SearchMovieForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False,
    )