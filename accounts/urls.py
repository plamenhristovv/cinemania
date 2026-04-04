from django.urls import path, include
from .views import (SignUpView, UserLoginView, UserLogoutView,
                    ProfileDetailView, ProfileEditView, profile_delete, toggle_movie_in_profile)

app_name = 'accounts'

authentication_patterns = [
    path('register/', SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('toggle-movie/<int:movie_id>/', toggle_movie_in_profile, name='toggle_movie'),
]


profile_patterns = [
    path('', ProfileDetailView.as_view(), name='details'),
    path('edit/', ProfileEditView.as_view(), name='edit'),
    path('delete/', profile_delete, name='delete'),
]




urlpatterns = [
    path('', include(authentication_patterns)),
    path('profile/<int:pk>/', include(profile_patterns))

]

