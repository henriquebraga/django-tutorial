from django.test import TestCase
from mysite.polls.admin import QuestionModelAdmin, ChoiceInline, Choice


class QuestionModelAdminTest(TestCase):

    def test_list_display(self):
        """List display must contain the following fields: question_text, pub_date """
        expected = ('question_text', 'pub_date')
        self.assertSequenceEqual(expected, QuestionModelAdmin.list_display)

    def test_search_fields(self):
        """Search fields must contain: ('question_text', 'pub_date')"""
        expected = ('question_text', 'pub_date')
        self.assertSequenceEqual(expected, QuestionModelAdmin.search_fields)

    def test_choice_inline(self):
        """Inline must be a ChoiceInline instance."""
        self.assertIsInstance(ChoiceInline, type(QuestionModelAdmin.inlines[0]))

class ChoiceInlineTest(TestCase):

    def test_is_choice(self):
        """'model' class attribute must be a Choice instance type."""
        self.assertIsInstance(Choice, type(ChoiceInline.model))

