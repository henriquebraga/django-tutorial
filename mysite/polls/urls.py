from django.conf.urls import url

from mysite.polls.views import detail, results, vote
from . import views

urlpatterns = [
    url(r'^(\d+)/$',detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),

]