from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.http import HttpResponseForbidden
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegistrationForm, ProfileForm

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from movies.models import Movie


UserModel = get_user_model()

def toggle_movie_in_profile(request, movie_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    movie = get_object_or_404(Movie, id=movie_id)
    profile = request.user.profile
    
    if movie in profile.movies.all():
        profile.movies.remove(movie)
    else:
        profile.movies.add(movie)
        
    return redirect('movies:details', slug=movie.slug)

class SignUpView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        viewer_group = Group.objects.get(name='Viewers')
        self.object.groups.add(viewer_group)
        return response


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

class UserLogoutView(LogoutView):
    pass


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"{self.object.username}'s Profile"
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = UserModel
    template_name = 'accounts/profile_edit.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('accounts:details', kwargs={'pk': self.object.pk})



def profile_delete(request, pk):
    user = get_object_or_404(UserModel, pk=pk)

    if request.user.is_authenticated and request.user.pk == user.pk:
        if request.method == "POST":
            user.delete()
            return redirect("common:home")
    else:
        return HttpResponseForbidden()


    return render(request, 'accounts/profile-delete.html', {'profile': user})
