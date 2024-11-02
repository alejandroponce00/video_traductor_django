import os
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .forms import VideoForm
from .utils import process_video_realtime  # Actualizamos la importación

def home(request):
    form = VideoForm()
    return render(request, 'subtitler/home.html', {'form': form})

def process_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            result = process_video_realtime(video.file.path)  # Actualizamos la llamada a la función
            return JsonResponse(result)
    return render(request, 'subtitler/home.html', {'form': VideoForm()})