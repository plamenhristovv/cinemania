from django.urls import path

from lists.views import (
    ListsListView,
    ListDetailView,
    ListCreateView,
    ListUpdateView,
    ListDeleteView,
)

app_name = 'lists'

urlpatterns = [
    path('', ListsListView.as_view(), name='list'),
    path('add/', ListCreateView.as_view(), name='add'),
    path('<int:pk>/', ListDetailView.as_view(), name='details'),
    path('<int:pk>/edit/', ListUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', ListDeleteView.as_view(), name='delete'),
]