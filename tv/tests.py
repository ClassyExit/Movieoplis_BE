from django.test import TestCase, Client


class MyAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    
    def test_tv_popular(self):
        response = self.client.get('/api/tv/popular')
        self.assertEqual(response.status_code, 200)


    def test_tv_details(self):
        response = self.client.get('/api/tv/details')
        self.assertEqual(response.status_code, 200)

    
    
    def test_tv_season_details(self):
        response = self.client.get('/api/tv/season/details')
        self.assertEqual(response.status_code, 200)

    

    def test_tv_episode_details(self):
        response = self.client.get('/api/tv/episode/details')
        self.assertEqual(response.status_code, 200)