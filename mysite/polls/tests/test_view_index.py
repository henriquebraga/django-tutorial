from django.test import TestCase
from django.shortcuts import resolve_url as r

class IndexGetTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('poll:index'))

    def test_get(self):
        """GET / must return status code 200."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """GET / must use template index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')


class IndexInvalidGet(TestCase):

    def test_not_found(self):
        """GET /invalid_url_ must return status code 404. (Not found)"""
        resp = self.client.get('/invalid_url_')
        self.assertEqual(404, resp.status_code)

    def test_template_used(self):
        """GET /invalid_url_ must use template 404.html"""
        resp = self.client.get('/invalid_url_')
        self.assertTemplateUsed(resp, '404.html')
