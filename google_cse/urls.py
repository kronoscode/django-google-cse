from django.urls import path
from .views import search

app_name = 'google_cse'

urlpatterns = [
    path('', search, name='search'),
]
