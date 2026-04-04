from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=True)
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = UserModel
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            user.profile.bio = self.cleaned_data.get('bio')
            user.profile.save()
        return user
