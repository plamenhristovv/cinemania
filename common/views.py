from django.views.generic import TemplateView
from directors.models import Director
from movies.models import Movie
from lists.models import List


class HomePageView(TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directors_count'] = Director.objects.count()
        context['movies_count'] = Movie.objects.count()
        context['lists_count'] = List.objects.count()

        context['latest_movies'] = Movie.objects.all().order_by('-release_year')[:3]

        return context