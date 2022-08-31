from django.urls import path
from wxapp.views import index, classify, tips, getid, getresult


urlpatterns = [
    path('',index),
    path('getid', getid),
    path('classify', classify),
    path('tips', tips),
    path('getresult', getresult),
]
