import os
import speech_recognition as sr
from moviepy.editor import VideoFileClip
import pysrt
from googletrans import Translator
from django.conf import settings
import subprocess
import json

def extract_audio(video_path, audio_path):
    command = [
        'ffmpeg',
        '-i', video_path,
        '-ab', '160k',
        '-ac', '2',
        '-ar', '44100',
        '-vn', audio_path
    ]
    subprocess.call(command)

def transcribe_audio_realtime(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        result = recognizer.recognize_google(audio, show_all=True)
        if not result:
            print("Could not understand audio")
            return None
        return result
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def translate_text(text, dest_language='es'):
    translator = Translator()
    return translator.translate(text, dest=dest_language).text

def process_video_realtime(video_path):
    video = VideoFileClip(video_path)
    audio_path = os.path.join(settings.MEDIA_ROOT, "temp_audio.wav")
    extract_audio(video_path, audio_path)

    transcript = transcribe_audio_realtime(audio_path)
    
    subtitles = []
    if transcript and isinstance(transcript, dict) and 'alternative' in transcript:
        for i, result in enumerate(transcript['alternative']):
            text = result['transcript']
            translated_text = translate_text(text)
            start_time = i * 5  # Assuming each subtitle lasts 5 seconds
            end_time = (i + 1) * 5
            subtitles.append({
                'start': start_time,
                'end': end_time,
                'text': translated_text
            })
    else:
        print("No se pudo transcribir el audio correctamente")

    # Clean up temporary files
    os.remove(audio_path)

    return {
        'video_duration': video.duration,
        'subtitles': subtitles
    }