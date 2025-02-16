from django.test import TestCase, Client


class MyAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_movie_popular(self):
        response = self.client.get('/api/movie/popular')
        self.assertEqual(response.status_code, 200)
        
    def test_movie_details(self):
        response = self.client.get('/api/movie/details')
        self.assertEqual(response.status_code, 200)


        
    