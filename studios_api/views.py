from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import ListView, DetailView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Studio
from .serializers import StudioSerializer
from .forms import SearchStudioForm



class StudioListView(LoginRequiredMixin, ListView):
    model = Studio
    template_name = 'studios/studio_list.html'
    context_object_name = 'studios'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('movies').annotate(movie_count=Count('movies'))
        form = SearchStudioForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            if query:
                queryset = queryset.filter(name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchStudioForm(self.request.GET)
        context['page_title'] = 'Movie Studios'
        return context

class StudioDetailView(LoginRequiredMixin, DetailView):
    model = Studio
    template_name = 'studios/studio_detail.html'
    context_object_name = 'studio'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('movies')



class StudioListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

class StudioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
