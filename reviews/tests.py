from django.test import TestCase, Client


class MyAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()


    def test_movie_review(self):
        response = self.client.get('/api/movie/review')
        self.assertEqual(response.status_code, 200)

    def test_tv_review(self):
        response = self.client.get('/api/tv/review')
        self.assertEqual(response.status_code, 200)