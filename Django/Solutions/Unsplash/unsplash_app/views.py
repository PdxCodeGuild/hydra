from django.shortcuts import render, redirect
from .models import GetImages, Board
import requests
from decouple import config
from django.contrib import messages
import os
import requests
import uuid

##Rest----
from .serializers import BoardSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
##Rest----

@api_view(['GET'])
def image_list(request, format=None):
    """
    Get a list of products or create a product .
    """
    if request.method == 'GET':
        pics = Board.objects.all()
        serializer = BoardSerializer(pics, many=True)
        return Response(serializer.data)

def get_images(request):
    SECRET_KEY = config('SECRET_KEY')
    url = f'https://api.unsplash.com/photos/?client_id={SECRET_KEY}'
    url_get = requests.get(url)
    data = url_get.json()
    all_img = GetImages.objects.all()
    # clears the temp database from existing images
    if all_img:
        all_img.delete()
    for pics in data:
        url = pics['urls']['thumb'] + '.jpg'
        page = requests.get(url)
        f_ext = os.path.splitext(url)[-1]
        name = str(uuid.uuid4())
        f_name = name + 'img{}'.format(f_ext)
        with open(os.path.join('media/images',f_name), 'wb') as f:
            f.write(page.content)
        GetImages.objects.create(
            my_image = f_name,
            full=pics['urls']['full'], thumb=pics['urls']['thumb'], download=pics['links']['download'])

    pics = GetImages.objects.all()
    context = {
        "pics": pics
    }
    return render(request, 'pages/imageList.html', context)


def add_pictures(request, id):
    pics = GetImages.objects.all()
    if request.method == 'GET':
        return render(request, 'pages/imageList.html', {'pics': pics})
    elif request.method == "POST":
        pic_to_board = GetImages.objects.filter(id=id)
        url = GetImages.objects.get(id=id).thumb
        Board.objects.create(full= pic_to_board[0].full, thumb = pic_to_board[0].thumb, download = pic_to_board[0].download )
        messages.success(request, 'Photo saved in your board')
        return render(request, 'pages/imageList.html', {'pics': pics})

def my_board(request):
    my_board = Board.objects.all()
    context = {
        "my_board": my_board
    }
    return render(request, 'pages/board.html', context)

def delete(request, id):
    img = Board.objects.get(id=id)
    img.delete()
    return redirect('board')
    