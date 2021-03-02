from django.conf.urls import url
from gytest.views import hello
urlpatterns = [
    url(r'^$',hello)
]