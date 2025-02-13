from django.test import TestCase, Client


class MyAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_genre(self):
        response = self.client.get('/api/genres')
        self.assertEqual(response.status_code, 200)


