from django.urls import path

from directors.views import DirectorListView,DirectorDetailView,DirectorCreateView,DirectorUpdateView,DirectorDeleteView


app_name = 'directors'

urlpatterns = [
    path('', DirectorListView.as_view(), name='list'),
    path('add/', DirectorCreateView.as_view(), name='add'),
    path('<int:pk>/', DirectorDetailView.as_view(), name='details'),
    path('<int:pk>/edit/', DirectorUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', DirectorDeleteView.as_view(), name='delete'),
]
