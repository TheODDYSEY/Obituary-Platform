# obituaries/urls.py
from django.urls import path
from .views import submit_obituary,view_obituaries

urlpatterns = [
    path('submit_obituary/', submit_obituary, name='submit_obituary'),
    path('view_obituaries/', view_obituaries, name='view_obituaries'),
]
