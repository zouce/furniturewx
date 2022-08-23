from django.urls import path
from wxapp.views import index, classify, tips


urlpatterns = [
    path('',index),
    path('classify',classify),
    path('tips',tips),
]
