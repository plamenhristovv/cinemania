from django import forms

class SearchStudioForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search studios...'})
    )
