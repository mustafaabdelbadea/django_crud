from django.urls import path
from aboutus.views import  contact
urlpatterns = [
    path('',contact
         , name='aboutUs'),
]