from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import User, Video
from .serializer import UserSerializer, VideoSerializer
import cv2
from django.http import StreamingHttpResponse
import threading


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer



class VideoStreamer:
    def __init__(self, video_path):
        self.video = cv2.VideoCapture(video_path)
        self.lock = threading.Lock()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        if not success:
            return None
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            return None
        return buffer.tobytes()

def generate_frames(video_streamer):
    while True:
        frame_bytes = video_streamer.get_frame()
        if frame_bytes is None:
            break
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

def video_stream(request):
    video_path = 'D:\riverflow.mp4'  # Replace with actual video path
    video_streamer = VideoStreamer(video_path)

    def generate():
        for frame in generate_frames(video_streamer):
            yield frame

    return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')