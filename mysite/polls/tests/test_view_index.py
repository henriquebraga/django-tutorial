from django.test import TestCase
from django.shortcuts import resolve_url as r

from mysite.polls.models import Question
from mysite.polls.tests.data import QUESTION_DATA


class IndexGetTest(TestCase):

    def setUp(self):
        self.obj = Question.objects.create(**QUESTION_DATA)
        self.resp = self.client.get(r('index'))

    def test_get(self):
        """GET / must return status code 200."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """GET / must use template index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_html(self):
        """HTML must contain one <ul> and the number of questions represented
        by <li>."""
        content = (('<ul', 1),
                ('<li', Question.objects.count()))

        for tag, count in content:
            with self.subTest():
                self.assertContains(self.resp, tag, count)

    def test_link(self):
        """
           HTML must contain link containing the absolute URL.
           E.g: /polls/1/detail/
        """
        expected = 'href="{0}"'.format(self.obj.get_absolute_url())
        self.assertContains(self.resp, expected)

class IndexInvalidGet(TestCase):

    def setUp(self):
        self.resp = self.client.get('/invalid_url_')

    def test_not_found(self):
        """GET /invalid_url_ must return status code 404. (Not found)"""
        self.assertEqual(404, self.resp.status_code)

    def test_template(self):
        """GET /invalid_url_ must use template 404.html"""
        self.assertTemplateUsed(self.resp, '404.html')


