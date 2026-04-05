from rest_framework import serializers

from .models import Studio
from movies.models import Movie

class HybridMovieField(serializers.PrimaryKeyRelatedField):

    def to_internal_value(self, data):
        if isinstance(data, dict):
            title = data.get('title')
            year = data.get('release_year')
            try:
                return Movie.objects.get(title=title, release_year=year)
            except Movie.DoesNotExist:
                raise serializers.ValidationError(f"Movie '{title}' ({year}) not found.")
            except Movie.MultipleObjectsReturned:
                raise serializers.ValidationError(f"Multiple movies found for '{title}' ({year}).")

        return super().to_internal_value(data)

class StudioSerializer(serializers.ModelSerializer):
    movies = HybridMovieField(
        many=True,
        queryset=Movie.objects.all()
    )

    class Meta:
        model = Studio
        fields = ['id', 'name', 'movies']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['movies'] = [
            {
                "title": movie.title,
                "release_year": movie.release_year
            } for movie in instance.movies.all()
        ]
        return representation


