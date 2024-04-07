from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Song

def songs_list(request):
    #songs = Song.objects.all()
    # return render(request, 'player/song_list.html', {'songs': songs})
    return render(request, 'songs_list.html')