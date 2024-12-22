from django.test import TestCase, Client


class MyAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()


    def test_search_movie(self):
        response = self.client.get('/api/search/movie')
        self.assertEqual(response.status_code, 200)

    def test_search_tv(self):
        response = self.client.get('/api/search/tv')
        self.assertEqual(response.status_code, 200)

    def test_search_multi(self):
        response = self.client.get('/api/search/multi')
        self.assertEqual(response.status_code, 200)