from django.test import TestCase, Client


class MyAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    
    def test_discover_movie(self):
        response = self.client.get('/api/discover/movie')
        self.assertEqual(response.status_code, 200)
    
    def test_discover_tv(self):
        response = self.client.get('/api/discover/tv')
        self.assertEqual(response.status_code, 200)