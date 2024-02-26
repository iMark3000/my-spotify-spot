from rest_framework import serializers
from spotify.models import Artist
from spotify.models import Genre
from spotify.models import Album
from spotify.models import Track
from spotify.models import ListenLog
from spotify.models import TrackLog


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("__all__")


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



class TrackLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackLog
        fields = "__all__"
