from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import base64
import requests
import os
from pathlib import Path
from wxapp.models import Tips
import random
from wxapp.yolov5.detect import run
from wxapp.style_code.predict import style
import cv2
import time
from wxapp.Mask_RCNN.detect import detect


def getphoto(request):
    print('classify===================================================')
    data = json.loads(request.body)
    dirid = data.get('id')
    img_base64 = data.get('img_base64')
    img = base64.b64decode(img_base64)
    #response = requests.get('http://47.94.2.45:8000/classify',params={'img_base64':123}).json()
    #print(response)
    filepath = '/home/zouce/furniturewx/wxapp/static/classify/img' + dirid
    if not os.path.exists(filepath):
        JsonResponse({'result':'error'})
    print('classify1============================================================')
    imglist = os.listdir(filepath)
    pid = len(imglist)
    img_url = filepath + '/p' + str(pid) +'.jpg'
    with open(img_url,'wb') as f:
        f.write(img)
    return JsonResponse({'result':'success','name':'classify'})


def tips(request):
    numlist = random.sample([0,1,2,3,4,5,6,7,8,9,10,11],5)
    numlist.sort()
    data = []
    for i in numlist:
        tips = Tips.objects.get(tipsid=i)
        data.append({
            'photo': tips.photo,
            'tips': tips.tips
        })
    return JsonResponse({'result':'success','data':data})


def getid(request):
    print('getid====================================')
    filepath = '/home/zouce/furniturewx/wxapp/static/classify'
    filelist = os.listdir(filepath)
    filelist.sort()
    newid = len(filelist)
    dirpath = filepath+'/img'+str(newid)
    os.mkdir(dirpath)
    return JsonResponse({'result':'success','id':str(newid)})


def getresult(request):
    time.sleep(2)
    print('getresut=============================================')
    data = json.loads(request.body)
    imgid = data.get('id')
    print(imgid)
    imgfile = '/home/zouce/furniturewx/wxapp/static/classify/img' + imgid
    imglist = os.listdir(imgfile)
    res_data = []
    print(len(imglist))
    for imgname in imglist:
        imgmsg = {}
        imgpath = imgfile + '/' + imgname
        imgmsg['imgpath'] = 'http://82.156.84.122:8000/static/classify/img' + imgid + '/' + imgname
        img = cv2.imread(imgpath)
        imgmsg['width'] = img.shape[1]
        imgmsg['height'] = img.shape[0]
        imgclass = run(imgpath)
        if len(imgclass) == 0:
            imgmsg['imgclass'] = 0
        else:
            imgmsg['imgclass'] = int(imgclass[0][5])
        imgstyle = style(imgpath)
        imgmsg['imgstyle'] = imgstyle
        #mask = [{'class':'shelf','p':0.916887,'position':[137,76,296,321]},{'class':'drawer','p':0.90571535,'position':[140,166,171,263]}]
        #imgmsg['mask'] = mask
        imgmsg['mask'] = detect(imgpath,imgmsg['imgclass'])
        #imgmsg['mask']
        #response = requests.get('http://82.156.91.202:8000/maskrcnn',{'imgid':imgid, 'imgname':imgname, 'imgclass': imgmsg['imgclass']}).json()
        #imgmsg['mask'] = response['mask']
        res_data.append(imgmsg)
        print(imgmsg)
    print(res_data)
    return JsonResponse({'result':'success','data':res_data})

