from django.urls import path

from movies.views import MovieListView, MovieCreateView, MovieDetailView, MovieUpdateView, MovieDeleteView

app_name = 'movies'

urlpatterns = [
    path('', MovieListView.as_view(), name='list'),
    path('add/', MovieCreateView.as_view(), name='add'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='details'),
    path('<slug:slug>/edit/', MovieUpdateView.as_view(), name='edit'),
    path('<slug:slug>/delete/', MovieDeleteView.as_view(), name='delete'),
]
