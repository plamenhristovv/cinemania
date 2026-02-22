from django import forms

from movies.models import Movie


class MovieFormBasic(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['slug']


        widgets = {
            "title": forms.TextInput(attrs={'placeholder': 'Inception'}),
            "tagline": forms.TextInput(attrs={'placeholder': 'Your mind is the scene of the crime'}),
            "description": forms.Textarea(attrs={'placeholder': 'Description of this movie goes here'}),
            "release_year": forms.NumberInput(attrs={'placeholder': '2010'}),
            "image_url": forms.URLInput(attrs={'placeholder': 'Enter an link to an image of the movie poster'}),
            "runtime": forms.NumberInput(attrs={'placeholder': '148 minutes'}),
        }
        error_messages = {
            'title': {
                'required': 'Please enter the movie title.',
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

class MovieDeleteForm(MovieFormBasic):
    ...


class SearchMovieForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False,
    )