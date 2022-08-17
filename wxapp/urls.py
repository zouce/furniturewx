from django.urls import path
from wxapp.views import index


urlpatterns = [
    path('',index),
]
