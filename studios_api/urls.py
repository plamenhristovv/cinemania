from django.urls import path
from .views import (
    StudioListCreateView, 
    StudioRetrieveUpdateDestroyView,
    StudioListView,
    StudioDetailView
)

app_name = 'studios'

urlpatterns = [
    path('api/', StudioListCreateView.as_view(), name='studio-api-list'),
    path('api/<int:pk>/', StudioRetrieveUpdateDestroyView.as_view(), name='studio-api-detail'),
    

    path('', StudioListView.as_view(), name='list'),
    path('<int:pk>/', StudioDetailView.as_view(), name='details'),
]
