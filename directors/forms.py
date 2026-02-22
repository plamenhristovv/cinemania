from django import forms

from directors.models import Director


class DirectorFormBasic(forms.ModelForm):
    class Meta:
        model = Director
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Christopher Nolan'}),
            "description": forms.Textarea(attrs={'placeholder': 'Brief biography of the director'}),
            "image_url": forms.URLInput(attrs={'placeholder': 'Enter an link to an image of the director'}),
        }

        error_messages = {
            'name': {
                'required': 'Please enter the director\'s name.',
            },
            'description': {
                'required': 'A brief biography of the director is needed.',
            },
            'image_url': {
                'required': 'Provide a link to the director\'s photo.',
            },
        }

class DirectorCreateForm(DirectorFormBasic):
    ...

class DirectorUpdateForm(DirectorFormBasic):
    ...

class DirectorDeleteForm(DirectorFormBasic):
    ...


class SearchDirectorForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False,
    )