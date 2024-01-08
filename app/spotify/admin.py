from django.contrib import admin

from .models import Artist
from .models import Album
from .models import Track
from .models import ListenLog
from .models import Genre


class ArtistAdmin(admin.ModelAdmin):
    pass


class AlbumAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


class ListenLogAdmin(admin.ModelAdmin):
    pass


class TrackAdmin(admin.ModelAdmin):
    pass


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(ListenLog, ListenLogAdmin)
admin.site.register(Track, TrackAdmin)
