import logging
from typing import Union

from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from spotify.models import Artist
from spotify.models import Genre
from spotify.models import Album
from spotify.models import Track
from spotify.models import ListenLog
from .serializers import ArtistSerializer
from .serializers import GenreSerializer
from .serializers import AlbumSerializer
from .serializers import TrackSerializer
from .serializers import ListenLogSerializer
from .serializers import TrackLogSerializer

logger = logging.getLogger(__name__)

# Artist Endpoints

@api_view(['GET'])
def artistList(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def artistDetail(request, artist_id):
    try:
        artists = Artist.objects.get(pk=artist_id)
        serializer = ArtistSerializer(artists, many=False)
        return Response(serializer.data)
    except Artist.DoesNotExist:
        return Response(
            {'message': 'Object not found'}, 
            status=status.HTTP_404_NOT_FOUND
            )


@api_view(['POST'])
def artistCreate(request):
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)


@api_view(['GET'])
def artistList(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

# Genre Endpoints

@api_view(['POST'])
def genreCreate(request):
    serializer = GenreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    logger.info(f"Error creating genre: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def genreList(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def genreDetail(request, pk):
    try:
        genres = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genres, many=False)
        return Response(serializer.data)
    except Genre.DoesNotExist:
        return Response(
            {'message': 'Object not found'}, 
            status=status.HTTP_404_NOT_FOUND
            )


@api_view(['GET'])
def genreDetailSlug(request, name):
    try:
        genres = Genre.objects.get(slug=name)
        serializer = GenreSerializer(genres, many=False)
        return Response(serializer.data)
    except Genre.DoesNotExist:
        return Response(
            {'message': 'Object not found'}, 
            status=status.HTTP_404_NOT_FOUND
            )


# Album Endpoints

@api_view(['GET'])
def albumDetail(request, album_id):
    try:
        albums = Album.objects.get(pk=album_id)
        serializer = AlbumSerializer(albums, many=False)
        return Response(serializer.data)
    except Album.DoesNotExist:
        return Response(
            {'message': 'Object not found'}, 
            status=status.HTTP_404_NOT_FOUND
            )

@api_view(['POST'])
def albumCreate(request):
    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
        print(request.data)
    return Response(serializer.data)


@api_view(['GET'])
def albumList(request):
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)

# Track Endpoints

@api_view(['GET'])
def trackDetail(request, track_id):
    try:
        tracks = Track.objects.get(pk=track_id)
        serializer = TrackSerializer(tracks, many=False)
        return Response(serializer.data)
    except Track.DoesNotExist:
        return Response(
            {'message': 'Object not found'}, 
            status=status.HTTP_404_NOT_FOUND
            )


@api_view(['POST'])
def trackCreate(request):
    serializer = TrackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)


@api_view(['GET'])
def trackList(request):
    tracks = Track.objects.all()
    serializer = TrackSerializer(tracks, many=True)
    return Response(serializer.data)

# ListenLog Endpoint

@api_view(['GET'])
def listenLogDetail(request, posix_tmstmp):
    try:
        listen_event = ListenLog.objects.get(pk=posix_tmstmp)
        serializer = ListenLogSerializer(listen_event, many=False)
        return Response(serializer.data)
    except ListenLog.DoesNotExist:
        return Response(
            {'message': 'Object not found'}, 
            status=status.HTTP_404_NOT_FOUND
            )


@api_view(['POST'])
def listenLogCreate(request):
    serializer = ListenLogSerializer(data=request.data)
    data = {}
    # data["track_played"] = request.data["fields"]["track"]
    # data["log"] = request.data["pk"]
    # _create_track_log(data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)


def _create_track_log(data):
    serializer = TrackLogSerializer(data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)



@api_view(['GET'])
def listenLogList(request):
    listen_events = ListenLog.objects.all()
    serializer = ListenLogSerializer(listen_events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def artistListenLogsMonth(request, month: str, year: str):
    artist_count = {}
    q = ListenLog.objects.filter(played_at_datetime__year=year).filter(played_at_datetime__month=month)
    for log in q:
        for artist in log.track.artists.all():
            if artist.artist_id not in artist_count:
                artist_count[artist.artist_id] = {"name": artist.name, "count": 1}
            else:
                artist_count[artist.artist_id]["count"]  += 1
    artist_count = sorted(artist_count.items(), reverse=True, key = lambda x: x[1]["count"])
    return HttpResponse(artist_count)


@api_view(['GET'])
def trackListenLogsMonth(request, month: str, year: str):
    track_count = {}
    q = ListenLog.objects.filter(played_at_datetime__year=year).filter(played_at_datetime__month=month)
    for log in q:
        if log.track.track_id not in track_count:
            track_count[log.track.track_id] = {"name": log.track.name, "count": 1}
        else:
            track_count[log.track.track_id]["count"]  += 1
    track_count = sorted(track_count.items(), reverse=True, key = lambda x: x[1]["count"])
    return HttpResponse(track_count)



@api_view(['GET'])
def artistListenLogsYear(request, month: str, year: str):
    artist_count = {}
    q = ListenLog.objects.filter(played_at_datetime__year=year)
    for log in q:
        for artist in log.track.artists.all():
            if artist.artist_id not in artist_count:
                artist_count[artist.artist_id] = {"name": artist.name, "count": 1}
            else:
                artist_count[artist.artist_id]["count"]  += 1
    artist_count = sorted(artist_count.items(), reverse=True, key = lambda x: x[1]["count"])
    return HttpResponse(artist_count)


@api_view(['GET'])
def trackListenLogsYear(request, year: str):
    track_count = {}
    q = ListenLog.objects.filter(played_at_datetime__year=year)
    for log in q:
        if log.track.track_id not in track_count:
            track_count[log.track.track_id] = {"name": log.track.name, "count": 1}
        else:
            track_count[log.track.track_id]["count"]  += 1
    track_count = sorted(track_count.items(), reverse=True, key = lambda x: x[1]["count"])
    return HttpResponse(track_count)


def artistLogDetails(request, artist_id: str):
    artist = Artist.object.get(pk=artist_id)
    q = ListenLog.objects.filter()

@api_view(['GET'])
def trackListenLogsAllTime(request):
    pass


@api_view(['GET'])
def artistListenLogsAllTime(request):
    pass


@api_view(['GET'])
def artistListenLogs(request, artist_id: str, year: Union[None, str]=None, month: Union[None, str]=None):
    artist = Artist.objects.get(pk=artist_id)
    if year is None:
        logs = ListenLog.objects.filter(track_played__artists=artist)
    elif year is not None:
        if month is not None:
            logs = ListenLog.objects.filter(track_played__artists=artist).filter(played_at_datetime__year=year).filter(played_at_datetime__month=month)
        else:
            logs = ListenLog.objects.filter(track_played__artists=artist).filter(played_at_datetime__year=year)
    logs = list(logs.values())
    return JsonResponse(logs, safe=False)

