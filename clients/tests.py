from django.test import TestCase


class TestAdminPages(TestCase):

    fixtures = ['auth', 'audiologists', 'providers']

    def setUp(self):
        assert self.client.login(username='admin', password='admin')

    def test_root(self):
        resp = self.client.get('/admin/', secure=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'ADAPT Client Management')


    def test_client_list(self):
        resp = self.client.get('/admin/clients/client/', secure=True)
        self.assertEqual(resp.status_code, 200)

    def test_client_add(self):
        resp = self.client.get('/admin/clients/client/add/', secure=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'First name')


    def test_provider_list(self):
        resp = self.client.get('/admin/clients/provider/', secure=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Meijer')

    def test_provider_add(self):
        resp = self.client.get('/admin/clients/provider/add/', secure=True)
        self.assertEqual(resp.status_code, 200)

    def test_provider_3(self):
        resp = self.client.get('/admin/clients/provider/3/', secure=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Meijer')


    def test_aud_list(self):
        resp = self.client.get('/admin/clients/audiologist/', secure=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, '2 Starkey')

    def test_aud_add(self):
        resp = self.client.get('/admin/clients/audiologist/add/', secure=True)
        self.assertEqual(resp.status_code, 200)

    def test_aud_1(self):
        resp = self.client.get('/admin/clients/audiologist/1/', secure=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'McDonalds')

