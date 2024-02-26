from django.db import models
from django.utils.text import slugify


class Artist(models.Model):
    artist_id = models.CharField(primary_key=True)
    name = models.CharField()
    slug = models.CharField(null=True, blank=True)
    genres = models.ManyToManyField("Genre", blank=True)
    image_small = models.URLField(null=True, blank=True)
    image_medium = models.URLField(null=True, blank=True)
    image_large = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class GenreFamily(models.Model):
    name = models.CharField(unique=True)


class Genre(models.Model):
    name = models.CharField(unique=True)
    slug = models.SlugField(unique=True, blank=True)
    genre_family = models.ManyToManyField(GenreFamily, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Album(models.Model):
    album_id = models.CharField(primary_key=True)
    name = models.CharField()
    year = models.CharField()  # Char field as year can be MM/DD/YYYY or just YYYY
    artists = models.ManyToManyField(Artist)
    album_type = models.CharField()
    image_small = models.URLField(null=True)
    image_medium = models.URLField(null=True)
    image_large = models.URLField(null=True)

    def get_artists_names(self):
        artist_names = [artist.name for artist in self.artists.all()]
        return ", ".join(artist_names)


    def __str__(self):
        return f"{self.name} by {self.get_artists_names()}"


class Track(models.Model):
    track_id = models.CharField(primary_key=True)
    name = models.CharField()
    duration = models.IntegerField()  # I believe duration is in MS
    artists = models.ManyToManyField(Artist)
    album = models.ManyToManyField(Album)
    # logs = models.ManyToManyField("ListenLog", through="TrackLog")

    def get_artists_names(self):
        artist_names = [artist.name for artist in self.artists.all()]
        return ", ".join(artist_names)

    def __str__(self):
        return f"{self.name} by {self.get_artists_names()}"


class ListenLog(models.Model):
    # POSIX timestamp is converted to a str in order to be a primary key
    posix_tmstmp = models.CharField(primary_key=True)
    played_at_datetime = models.DateTimeField()
    track_played = models.ForeignKey(Track, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.track_played} - {self.played_at_datetime.strftime('%m-%d-%Y %-I:%M:%S %p')}"


class TrackLog(models.Model):
    track = models.ForeignKey(Track, on_delete=models.PROTECT)
    log = models.ForeignKey(ListenLog, on_delete=models.PROTECT)
