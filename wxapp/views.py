from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import base64
import requests
import os
from pathlib import Path


def index(request):
    return render(request, "web.html")

def classify(request):

    data = json.loads(request.body)
    img_base64 = data.get('img_base64')
    img = base64.b64decode(img_base64)
    img_url = os.path.join('/home/zouce/furniturewx/static/','classify/test1.jpg')
    with open(img_url,'wb') as f:
        f.write(img)
    #print(request.body)
    #print(data)
    #print(data.get('img'))
    print(1)
    params = {
            'img_base64': img_base64,
            # 'test': 111,
        }
    response = requests.get('http://furnitureclassify.free.idcfengye.com',params=params).json()
    print(response['result'])
    return JsonResponse({'result':'success','name':'classify'})

def tips(request):
    return JsonResponse({'result':'success','name':'tips'})
