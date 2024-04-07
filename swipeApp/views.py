from django.shortcuts import render

# Create your views here.

from .models import Song

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'player/song_list.html', {'songs': songs})