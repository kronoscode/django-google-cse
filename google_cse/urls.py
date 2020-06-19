from django.conf.urls import url
from .views import search

app_name = 'google_cse'

urlpatterns = [
    url(r'^$', search, name='search'),
]
