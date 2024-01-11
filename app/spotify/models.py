from django.db import models
from django.utils.text import slugify

ALBUM_TYPES = [
    ("SINGLE", "Single"),
    ("COMPILATION", "Compilation"),
    ("ALBUM", "Album"),
]

DAYS_OF_THE_WEEK = [
    (6, "Sunday"),
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
]

MONTHS = [
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December"),
]


class Artist(models.Model):
    artist_id = models.CharField(primary_key=True)
    name = models.CharField()
    slug = models.CharField(null=True, blank=True)
    genre = models.ManyToManyField("Genre")
    photo = models.URLField(null=True, blank=True)  # Replace with ImageField?

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Album(models.Model):
    album_id = models.CharField(primary_key=True)
    name = models.CharField()
    year = models.CharField()  # Char field as year can be MM/DD/YYYY or just YYYY
    artist = models.ManyToManyField(Artist)
    album_type = models.CharField(max_length=11, choices=ALBUM_TYPES)

    def __str__(self):
        return self.name


class Track(models.Model):
    track_id = models.CharField(primary_key=True)
    name = models.CharField()
    duration = models.IntegerField()  # I believe duration is in MS
    artist = models.ManyToManyField(Artist)
    album = models.ManyToManyField(Album)

    def __str__(self):
        return self.name


class ListenLog(models.Model):
    # POSIX timestamp is converted to a str in order to be a primary key
    played_at_posix_timestamp = models.CharField(primary_key=True)
    played_at_datetime = models.DateTimeField()
    played_at_month = models.IntegerField(choices=MONTHS)
    played_at_dow = models.CharField(choices=DAYS_OF_THE_WEEK)
    played_at_hour = models.IntegerField()  # 24 Hour
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.track.artist.name} - {self.track} - {self.played_at_posix_timestamp}"
