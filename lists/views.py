from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from common.mixins import CheckUserIsOwner
from lists.models import List
from lists.forms import ListCreateForm, ListUpdateForm, ListDeleteForm, SearchListForm
from django.db.models import Count

from movies.models import Movie


class ListsListView(LoginRequiredMixin, ListView):
    model = List
    template_name = 'lists/lists_list.html'
    context_object_name = 'lists'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user).prefetch_related('movies').annotate(movie_count=Count('movies'))
        form = SearchListForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            if query:
                queryset = queryset.filter(name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchListForm(self.request.GET)
        context['page_title'] = 'My Lists'
        return context


class ListDetailView(LoginRequiredMixin, CheckUserIsOwner, DetailView):
    model = List
    template_name = 'lists/list_detail.html'
    context_object_name = 'list_obj'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('movies')


class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    form_class = ListCreateForm
    template_name = 'lists/list_add.html'
    success_url = reverse_lazy('lists:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListUpdateView(LoginRequiredMixin, CheckUserIsOwner, UpdateView):
    model = List
    form_class = ListUpdateForm
    template_name = 'lists/list_edit.html'
    context_object_name = 'list_obj'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_movies'] = Movie.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('lists:details', kwargs={'pk': self.object.pk})


class ListDeleteView(LoginRequiredMixin, CheckUserIsOwner, DeleteView):
    model = List
    template_name = 'lists/list_delete.html'
    context_object_name = 'list_obj'
    success_url = reverse_lazy('lists:list')
    pk_url_kwarg = 'pk'
