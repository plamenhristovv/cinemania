from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegistrationForm

class SignUpView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
