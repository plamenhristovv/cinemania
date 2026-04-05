from django.urls import path
from .views import StudioListCreateView, StudioRetrieveUpdateDestroyView

app_name = 'studios_api'

urlpatterns = [
    path('', StudioListCreateView.as_view(), name='studio-list-create'),
    path('<int:pk>/', StudioRetrieveUpdateDestroyView.as_view(), name='studio-detail'),
]
