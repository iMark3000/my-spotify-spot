from django.shortcuts import render
from .models import Artist, Album, Genre

from django.http import HttpResponse, Http404


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def artists(request):
    artists = Artist.objects.order_by("name")
    artists = ", ".join([a.name for a in artists])
    return HttpResponse(f"Hello, world. Here are the artists: {artists}.")


def artist_profile(request, name):
    try:
        artist = Artist.objects.get(slug=name)
        albums = Album.objects.filter(artist__id=artist.id)
        genres = artist.genre.all()
    except Artist.DoesNotExist:
        raise Http404(f"{name} not found in catalog")

    context = {
        "artist": artist,
        "albums": albums,
        "genres": [genre.name for genre in genres]
    }
    return render(request, "spotify/artist_profile.html", context=context)
