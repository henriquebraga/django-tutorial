from django.shortcuts import resolve_url as r
from django.test import TestCase
from mysite.polls.models import Question
from mysite.polls.tests.data import QUESTION_DATA

DETAIL_URL_ALIAS = 'polls:detail'
class PollDetailGetTest(TestCase):

    def setUp(self):
        self.obj = Question.objects.create(**QUESTION_DATA)
        self.resp = self.client.get(r('polls:detail', self.obj.pk))

    def test_get(self):
        """Must return status code 200."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must render template /question/poll_detail.form.html"""
        self.assertTemplateUsed(self.resp, 'questions/poll_detail_form.html')

    def test_context(self):
        """Context must have a question instance."""
        data = self.resp.context['question']
        self.assertIsInstance(data, Question)

    def test_data(self):
        """Must contain. the poll details."""
        contents = \
            (QUESTION_DATA['question_text'],
             self.format_date(QUESTION_DATA['pub_date'])
                )
        for content in contents:
            with self.subTest():
                self.assertContains(self.resp, content)

    def format_date(self, utc):
        """Format date to the following format: dd/mm/yyyy"""
        return utc.date().strftime('%d/%m/%Y')

class PollDetailGetInvalidContext(TestCase):

    def setUp(self):
        invalid_id = 0
        self.resp = self.client.get(r(DETAIL_URL_ALIAS, invalid_id))
    def test_get(self):
        """Must return status code 404 (Not Found)."""
        self.assertEqual(404, self.resp.status_code)

    def test_template(self):
        """Must render template 404.html"""
        self.assertTemplateUsed(self.resp, '404.html')








