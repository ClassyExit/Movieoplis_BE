from django.test import TestCase, Client


class MyAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()


    def test_trending(self):
        response = self.client.get('/api/trending')
        self.assertEqual(response.status_code, 200)