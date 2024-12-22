from django.test import TestCase, Client


class MyAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_movie_genre(self):
        response = self.client.get('/api/movie/genre')
        self.assertEqual(response.status_code, 200)


    def test_tv_genre(self):
        response = self.client.get('/api/tv/genre')
        self.assertEqual(response.status_code, 200)