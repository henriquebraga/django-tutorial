from django.test import TestCase
from django.db import models
from mysite.polls.models import Choice, Question
from mysite.polls.tests.data import QUESTION_DATA, CHOICE_DATA


class ChoiceModelTest(TestCase):

    def setUp(self):
        question = Question.objects.create(**QUESTION_DATA)
        self.obj = Choice(question=question, **CHOICE_DATA)
        self.obj.save()

    def test_is_model(self):
        """Choice must be a model instance."""
        choice = type(self.obj)
        expected = type(models.Model)
        self.assertIsInstance(choice, expected)

    def test_create(self):
        """Must have one question created."""
        self.assertTrue(Choice.objects.exists())

    def test_str(self):
        """str must return choice_text value"""
        expected = self.obj.choice_text
        self.assertEquals(expected, str(self.obj))


