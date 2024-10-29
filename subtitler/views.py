import os
from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
from .forms import VideoForm
from .utils import process_uploaded_video

def home(request):
    form = VideoForm()
    return render(request, 'subtitler/home.html', {'form': form})

def process_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            output_path = process_uploaded_video(video.file.path)
            return FileResponse(open(output_path, 'rb'), as_attachment=True, filename='video_subtitulado.mp4')
    return render(request, 'subtitler/home.html', {'form': VideoForm()})