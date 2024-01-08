from rest_framework.decorators import api_view
from rest_framework.response import Response
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

"""
class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveDestroyAPIView):
    pass
"""

# Artist Endpoints


@api_view(['GET'])
def artistList(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def artistDetail(request, artist_id):
    artists = Artist.objects.get(pk=artist_id)
    serializer = ArtistSerializer(artists, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def artistCreate(request):
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
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
    return Response(serializer.data)


@api_view(['GET'])
def genreList(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def genreDetail(request, pk):
    genres = Genre.objects.get(pk=pk)
    serializer = GenreSerializer(genres, many=False)
    return Response(serializer.data)

# Album Endpoints

@api_view(['GET'])
def albumDetail(request, album_id):
    albums = Album.objects.get(pk=album_id)
    serializer = AlbumSerializer(albums, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def albumCreate(request):
    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def albumList(request):
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)

# Track Endpoints

@api_view(['GET'])
def trackDetail(request, track_id):
    tracks = Track.objects.get(pk=track_id)
    serializer = TrackSerializer(tracks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def trackCreate(request):
    serializer = TrackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def trackList(request):
    tracks = Track.objects.all()
    serializer = TrackSerializer(tracks, many=True)
    return Response(serializer.data)
