from django.test import TestCase, Client


class MyAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()


    def test_search(self):
        response = self.client.get('/api/search')
        self.assertEqual(response.status_code, 200)