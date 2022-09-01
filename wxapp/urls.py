from django.urls import path
from wxapp.views import getphoto, tips, getid, getresult


urlpatterns = [
    path('getid', getid),
    path('getphoto', getphoto),
    path('tips', tips),
    path('getresult', getresult),
]
