from django.urls import path
from specific.views import *
app_name='specific'
urlpatterns=[
    path('about/',about,name='about'),
    path('hmm/',hmm,name='hmm'),
]