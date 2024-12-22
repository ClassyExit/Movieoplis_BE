from django.test import TestCase, Client


class MyAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    
    def test_getCollections(self):
        response = self.client.get('/api/search/collections')
        self.assertEqual(response.status_code, 200)
