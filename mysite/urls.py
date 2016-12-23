
from django.conf.urls import url, include
from django.contrib import admin
from mysite.polls.views import index
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^polls/', include('mysite.polls.urls', namespace='polls')),
    url(r'^admin/', admin.site.urls),
]
