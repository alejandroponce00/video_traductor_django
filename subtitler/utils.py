import os
import speech_recognition as sr
from moviepy.editor import VideoFileClip
import pysrt
from googletrans import Translator
from django.conf import settings
import subprocess
import json
from pydub import AudioSegment
from pydub.silence import split_on_silence

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
    audio = AudioSegment.from_wav(audio_path)
    chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=audio.dBFS-14)
    
    transcript = []
    current_time = 0
    
    for i, chunk in enumerate(chunks):
        chunk_path = os.path.join(settings.MEDIA_ROOT, f"chunk_{i}.wav")
        chunk.export(chunk_path, format="wav")
        
        with sr.AudioFile(chunk_path) as source:
            audio_chunk = recognizer.record(source)
            try:
                result = recognizer.recognize_google(audio_chunk, show_all=False)
                if result:
                    end_time = current_time + len(chunk) / 1000.0
                    transcript.append({
                        'text': result,
                        'start': current_time,
                        'end': end_time
                    })
                    current_time = end_time
            except sr.UnknownValueError:
                print(f"Could not understand audio in chunk {i}")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            
        os.remove(chunk_path)
    
    return transcript

def translate_text(text, dest_language='es'):
    translator = Translator()
    return translator.translate(text, dest=dest_language).text

def process_video_realtime(video_path):
    video = VideoFileClip(video_path)
    audio_path = os.path.join(settings.MEDIA_ROOT, "temp_audio.wav")
    extract_audio(video_path, audio_path)

    transcript = transcribe_audio_realtime(audio_path)
    
    subtitles = []
    for item in transcript:
        translated_text = translate_text(item['text'])
        subtitles.append({
            'start': item['start'],
            'end': item['end'],
            'text': translated_text
        })

    # Clean up temporary files
    os.remove(audio_path)

    return {
        'video_duration': video.duration,
        'subtitles': subtitles
    }