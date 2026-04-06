from django.test import TestCase
from django.urls import reverse
from model_bakery import baker
from directors.models import Director

class DirectorListViewTests(TestCase):
    def test_list_view_status_code_and_template(self):
        response = self.client.get(reverse('directors:list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'directors/directors_list.html')

    def test_list_view_displays_directors(self):

        baker.make(Director, name="Steven Spielberg")
        baker.make(Director, name="James Cameron")
        

        response = self.client.get(reverse('directors:list'))
        

        self.assertEqual(len(response.context['directors']), 2)
        self.assertContains(response, "Steven Spielberg")
        self.assertContains(response, "James Cameron")

    def test_list_view_search_functionality(self):

        baker.make(Director, name="Christopher Nolan")
        baker.make(Director, name="Quentin Tarantino")

        response = self.client.get(reverse('directors:list'), {'query': 'Nolan'})

        self.assertEqual(len(response.context['directors']), 1)
        self.assertContains(response, "Christopher Nolan")
        self.assertNotContains(response, "Quentin Tarantino")

class DirectorDetailViewTests(TestCase):
    def test_detail_view_status_code_and_template(self):
        director = baker.make(Director)

        response = self.client.get(reverse('directors:details', kwargs={'pk': director.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'directors/director_detail.html')
        self.assertEqual(response.context['director'], director)

    def test_detail_view_404_for_non_existent_director(self):
        response = self.client.get(reverse('directors:details', kwargs={'pk': 999}))

        self.assertEqual(response.status_code, 404)

class DirectorCreateViewTests(TestCase):
    def test_create_view_get_request(self):
        response = self.client.get(reverse('directors:add'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'directors/director_add.html')

    def test_create_view_post_request_creates_director(self):
        data = {
            'name': 'Martin Scorsese',
            'description': 'One of the greatest directors in cinema history.',
            'image_url': 'http://example.com/scorsese.jpg'
        }

        response = self.client.post(reverse('directors:add'), data=data)

        self.assertEqual(response.status_code, 302) # Redirect
        self.assertRedirects(response, reverse('directors:list'))
        self.assertTrue(Director.objects.filter(name='Martin Scorsese').exists())

class DirectorUpdateViewTests(TestCase):
    def test_update_view_get_request(self):
        director = baker.make(Director)

        response = self.client.get(reverse('directors:edit', kwargs={'pk': director.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'directors/director_edit.html')

    def test_update_view_post_request_updates_director(self):
        director = baker.make(Director, name="Old Name")
        data = {
            'name': 'Updated Name',
            'description': 'Updated description that must be long enough.',
            'image_url': 'http://example.com/updated.jpg'
        }

        response = self.client.post(reverse('directors:edit', kwargs={'pk': director.pk}), data=data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('directors:details', kwargs={'pk': director.pk}))
        director.refresh_from_db()
        self.assertEqual(director.name, 'Updated Name')

class DirectorDeleteViewTests(TestCase):
    def test_delete_view_get_request(self):
        director = baker.make(Director)

        response = self.client.get(reverse('directors:delete', kwargs={'pk': director.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'directors/director_delete.html')

    def test_delete_view_post_request_deletes_director(self):
        director = baker.make(Director)

        response = self.client.post(reverse('directors:delete', kwargs={'pk': director.pk}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('directors:list'))
        self.assertFalse(Director.objects.filter(pk=director.pk).exists())
