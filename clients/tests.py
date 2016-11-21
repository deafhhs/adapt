from django.test import TestCase


class TestPages(TestCase):

    fixtures = ['auth', 'audiologists', 'clients', 'providers', 'settings']

    def setUp(self):
        assert self.client.login(username='admin', password='admin')

    def test_admin_root(self):
        resp = self.client.get('/admin/', secure=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'ADAPT Client Management')

    def test_admin_root_requires_login(self):
        self.client.logout()
        resp = self.client.get('/admin/', secure=True)
        self.assertEqual(resp.status_code, 302)


    def test_client_list(self):
        resp = self.client.get('/admin/clients/client/', secure=True)
        self.assertEqual(resp.status_code, 200)

    def test_client_add(self):
        resp = self.client.get('/admin/clients/client/add/', secure=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'First name')

    def test_client_1(self):
        resp = self.client.get('/admin/clients/client/1/change/', secure=True)
        self.assertEqual(resp.status_code, 200)


    def test_provider_list(self):
        resp = self.client.get('/admin/clients/provider/', secure=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Meijer')

    def test_provider_add(self):
        resp = self.client.get('/admin/clients/provider/add/', secure=True)
        self.assertEqual(resp.status_code, 200)

    def test_provider_3(self):
        resp = self.client.get('/admin/clients/provider/3/change/', secure=True)
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
        resp = self.client.get('/admin/clients/audiologist/1/change/', secure=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'McDonalds')


    def test_log_list(self):
        resp = self.client.get('/admin/clients/meetinglog/', secure=True)
        self.assertEqual(resp.status_code, 200)

    def test_log_add(self):
        resp = self.client.get('/admin/clients/meetinglog/add/', secure=True)
        self.assertEqual(resp.status_code, 200)


    def test_reports(self):
        resp = self.client.get('/reports/', secure=True)
        self.assertEqual(resp.status_code, 200)

    def test_reports_requires_login(self):
        self.client.logout()
        resp = self.client.get('/reports/', secure=True)
        self.assertEqual(resp.status_code, 302)


    def test_settings(self):
        resp = self.client.get('/admin/clients/settings/', secure=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Income')
