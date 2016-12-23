from django.conf.urls import url

from mysite.polls.views import detail
from . import views

urlpatterns = [
    url('(\d+)/$',detail, name='detail')
]