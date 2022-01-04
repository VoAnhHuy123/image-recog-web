from django.db import reset_queries
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
import requests


def index(request):
    form = ImageForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # print(request.FILES['images'])
            initial_obj = form.save(commit=False)
            print(initial_obj.image.url)
            
            # print()
            form.save()
            tag = image_recognition(initial_obj.image.url)
            context['tag'] = tag
    return render(request, 'upload_image.html', context)

def image_recognition(path):
    api_key = 'acc_acde9fb5a9ce20f'
    api_secret = '4ada93befe8c78b69b30c05486906312'
    path = '.' + path
    response = requests.post(
        'https://api.imagga.com/v2/tags',
        auth=(api_key, api_secret),
        files={'image': open(path, 'rb')})
    return response.json()['result']['tags'][0]