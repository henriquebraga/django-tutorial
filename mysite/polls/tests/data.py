from django.utils import timezone

QUESTION_DATA = {
    "question_text": "Who am I?",
    "pub_date": timezone.now()
}

CHOICE_DATA = {
    'choice_text': "I'm Batman!",
    'votes': 3
}

