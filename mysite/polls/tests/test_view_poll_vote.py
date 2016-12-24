from django.test import TestCase
from django.shortcuts import resolve_url as r

class PollVoteGetTest(TestCase):

    def test_get(self):
        """GET /polls/1/vote/ must return status code 200."""
        resp = self.client.get(r('polls:vote', question_id=1))
        self.assertEqual(200, resp.status_code)
