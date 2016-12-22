from django.test import TestCase
from django.db import models
from .POLL_REGISTRIES import QUESTION

from mysite.polls.models import Question


class QuestionModelTest(TestCase):

    def setUp(self):
        self.obj = Question(**QUESTION)
        self.obj.save()


    def test_is_model(self):
        """Question must be a model instance."""
        question = type(Question())
        expected = type(models.Model)
        self.assertIsInstance(question, expected)

    def test_create(self):

        self.assertTrue(Question.objects.exists())

    def test_str(self):
        """str built-in method must return choice text field."""
        expected = self.obj.question_text
        self.assertEquals(expected, str(self.obj))


