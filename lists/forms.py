from django import forms

from common.mixins import DisableFormFieldsMixin
from lists.models import List
from movies.models import Movie


class ListFormBasic(forms.ModelForm):
    movies = forms.MultipleChoiceField()


    class Meta:
        model = List
        fields = ['name', 'description']

        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'My Top 10 Movies'}),
            "description": forms.Textarea(attrs={'placeholder': 'A curated list of my favorite films'}),
        }

        error_messages = {
            'name': {
                'required': 'Please enter a name for the list.',
            },
            'description': {
                'required': 'A description for the list is needed.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['movies'].queryset = Movie.objects.all()

class ListCreateForm(ListFormBasic):
    pass

class ListUpdateForm(ListFormBasic):
    pass

class ListDeleteForm(DisableFormFieldsMixin, ListFormBasic):
    ...


class SearchListForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False,
    )
