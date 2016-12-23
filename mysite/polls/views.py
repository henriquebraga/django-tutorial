from django.shortcuts import render, get_object_or_404

from mysite.polls.models import Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    return render(request, 'index.html', context={'questions':
                                                  latest_questions})

def detail(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'questions/poll_detail_form.html', context={'question': question})