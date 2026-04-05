from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from movies.models import Movie
from directors.models import Director
from lists.models import List

class Command(BaseCommand):
    help = 'Initializes user groups and permissions for Editors and Viewers'

    def handle(self, *args, **options):
        # 1. Define Groups
        editor_group, created = Group.objects.get_or_create(name='Editors')
        viewer_group, created = Group.objects.get_or_create(name='Viewers')

        # 2. Get Content Types
        movie_ct = ContentType.objects.get_for_model(Movie)
        director_ct = ContentType.objects.get_for_model(Director)
        list_ct = ContentType.objects.get_for_model(List)

        # 3. Setup Editors
        # Movies & Directors: Full CRUD (Add, Change, Delete)
        # Lists: All permissions
        editor_movie_perms = Permission.objects.filter(content_type=movie_ct, codename__in=['add_movie', 'change_movie', 'delete_movie', 'view_movie'])
        editor_director_perms = Permission.objects.filter(content_type=director_ct, codename__in=['add_director', 'change_director', 'delete_director', 'view_director'])
        all_list_perms = Permission.objects.filter(content_type=list_ct)

        editor_group.permissions.set(list(editor_movie_perms) + list(editor_director_perms) + list(all_list_perms))

        # 4. Setup Viewers
        # Movies & Directors: View only
        # Lists: All permissions
        viewer_movie_perms = Permission.objects.filter(content_type=movie_ct, codename='view_movie')
        viewer_director_perms = Permission.objects.filter(content_type=director_ct, codename='view_director')
        
        viewer_group.permissions.set(list(viewer_movie_perms) + list(viewer_director_perms) + list(all_list_perms))

        self.stdout.write(self.style.SUCCESS('Successfully initialized "Editors" and "Viewers" groups and permissions.'))
