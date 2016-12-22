from django.test import TestCase
from django.db import models
from mysite.polls.models import Choice, Question
from mysite.polls.tests.POLL_REGISTRIES import QUESTION


class ChoiceModelTest(TestCase):

    def setUp(self):
        question = Question.objects.create(**QUESTION)
        self.obj = Choice(question=question, choice_text="I don't know", votes=10)
        self.obj.save()

    def test_is_model(self):
        choice = type(self.obj)
        expected = type(models.Model)
        self.assertIsInstance(choice, expected)

    def test_create(self):
        self.assertTrue(Choice.objects.exists())

    def test_str(self):
        """str built-in method must return choice text field."""
        expected = self.obj.choice_text
        self.assertEquals(expected, str(self.obj))


