from django.test import TestCase, Client


class MyAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_movie_popular(self):
        response = self.client.get('/api/movie/popular')
        self.assertEqual(response.status_code, 200)
    
    def test_movie_upcoming(self):
        response = self.client.get('/api/movie/upcoming')
        self.assertEqual(response.status_code, 200)

    def test_movie_toprated(self):
        response = self.client.get('/api/movie/toprated')
        self.assertEqual(response.status_code, 200)

    def test_movie_nowplaying(self):
        response = self.client.get('/api/movie/nowplaying')
        self.assertEqual(response.status_code, 200)
    
    def test_movie_details(self):
        response = self.client.get('/api/movie/details')
        self.assertEqual(response.status_code, 200)

    def test_movie_recommendations(self):
        response = self.client.get('/api/movie/recommendations')
        self.assertEqual(response.status_code, 200)

    def test_movie_similar(self):
        response = self.client.get('/api/movie/similar')
        self.assertEqual(response.status_code, 200)

    def test_movie_credits(self):
        response = self.client.get('/api/movie/credits')
        self.assertEqual(response.status_code, 200)

    def test_movie_videos(self):
        response = self.client.get('/api/movie/videos')
        self.assertEqual(response.status_code, 200)

    def test_movie_providers(self):
        response = self.client.get('/api/movie/providers')
        self.assertEqual(response.status_code, 200)
        
    