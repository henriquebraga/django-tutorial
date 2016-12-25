from django.utils import timezone

QUESTION_DATA = {
    "question_text": "Who am I?",
    "pub_date": timezone.now().astimezone()
}

CHOICE_DATA = {
    'choice_text': "I am Batman!",
    'votes': 3
}

