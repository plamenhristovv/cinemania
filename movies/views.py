from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from movies.models import Movie
from movies.forms import MovieCreateForm, MovieUpdateForm, SearchMovieForm


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movies_list.html'
    context_object_name = 'movies'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchMovieForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            if query:
                queryset = queryset.filter(title__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchMovieForm(self.request.GET)
        context['page_title'] = 'Browse Movies'
        return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'
    slug_url_kwarg = 'slug'


class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieCreateForm
    template_name = 'movies/movie_add.html'
    success_url = reverse_lazy('movies:list')


class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieUpdateForm
    template_name = 'movies/movie_edit.html'
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        return reverse_lazy('movies:details', kwargs={'slug': self.object.slug})


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_delete.html'
    success_url = reverse_lazy('movies:list')
    slug_url_kwarg = 'slug'
