from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from directors.models import Director
from directors.forms import DirectorCreateForm, DirectorUpdateForm, DirectorDeleteForm, SearchDirectorForm


class DirectorListView(ListView):
    model = Director
    template_name = 'directors/directors_list.html'
    context_object_name = 'directors'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset().annotate(movie_count=Count('movies'))
        form = SearchDirectorForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            if query:
                queryset = queryset.filter(name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchDirectorForm(self.request.GET)
        context['page_title'] = 'Browse Directors'
        return context


class DirectorDetailView(DetailView):
    model = Director
    template_name = 'directors/director_detail.html'
    context_object_name = 'director'
    pk_url_kwarg = 'pk'


class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorCreateForm
    template_name = 'directors/director_add.html'
    success_url = reverse_lazy('directors:list')


class DirectorUpdateView(UpdateView):
    model = Director
    form_class = DirectorUpdateForm
    template_name = 'directors/director_edit.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse_lazy('directors:details', kwargs={'pk': self.object.pk})


class DirectorDeleteView(DeleteView):
    model = Director
    form_class = DirectorDeleteForm
    template_name = 'directors/director_delete.html'
    success_url = reverse_lazy('directors:list')
    pk_url_kwarg = 'pk'
