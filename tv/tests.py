from django.test import TestCase, Client


class MyAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    
    def test_tv_popular(self):
        response = self.client.get('/api/tv/popular')
        self.assertEqual(response.status_code, 200)

    def test_tv_top_rated(self):
        response = self.client.get('/api/tv/toprated')
        self.assertEqual(response.status_code, 200)

    def test_tv_details(self):
        response = self.client.get('/api/tv/details')
        self.assertEqual(response.status_code, 200)

    def test_tv_credit(self):
        response = self.client.get('/api/tv/credits')
        self.assertEqual(response.status_code, 200)

    def test_tv_recommendations(self):
        response = self.client.get('/api/tv/recommendations')
        self.assertEqual(response.status_code, 200)

    def test_tv_similar(self):
        response = self.client.get('/api/tv/similar')
        self.assertEqual(response.status_code, 200)

    def test_tv_videos(self):
        response = self.client.get('/api/tv/videos')
        self.assertEqual(response.status_code, 200)


    def test_tv_providers(self):
        response = self.client.get('/api/tv/providers')
        self.assertEqual(response.status_code, 200)

    
    def test_tv_season_details(self):
        response = self.client.get('/api/tv/season/details')
        self.assertEqual(response.status_code, 200)

    def test_tv_season_videos(self):
        response = self.client.get('/api/tv/season/videos')
        self.assertEqual(response.status_code, 200)

    def test_tv_episode_details(self):
        response = self.client.get('/api/tv/episode/details')
        self.assertEqual(response.status_code, 200)