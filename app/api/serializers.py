from rest_framework import serializers
from spotify.models import Artist
from spotify.models import Genre
from spotify.models import Album
from spotify.models import Track
from spotify.models import ListenLog


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("artist_id", "name", "genre", "photo")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"


class ListenLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListenLog
        fields = "__all__"
