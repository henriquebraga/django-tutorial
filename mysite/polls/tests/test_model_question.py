from django.test import TestCase
from django.db import models
from .data import QUESTION
from datetime import timedelta
from mysite.polls.models import Question


class QuestionModelTest(TestCase):

    def setUp(self):
        self.obj = Question(**QUESTION)
        self.obj.save()

    def test_is_model(self):
        """Question must be a model instance."""
        question, expected = type(self.obj), type(models.Model)
        self.assertIsInstance(question, expected)

    def test_create(self):
        """One question must exists."""
        self.assertTrue(Question.objects.exists())

    def test_str(self):
        """str built-in method must return choice text field."""
        expected = self.obj.question_text
        self.assertEquals(expected, str(self.obj))

    def test_was_published_recently(self):
        """Published recently must be true"""
        self.assertTrue(self.obj.published_recently())

    def test_was_not_published_recently(self):
        """Published recently must be false"""
        self.obj.pub_date = self.obj.pub_date - timedelta(days=2)
        self.assertFalse(self.obj.published_recently())





