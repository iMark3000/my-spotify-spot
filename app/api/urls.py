from django.urls import path
from . import views

app_nane = 'api'

urlpatterns = [
    path('artist-create/', views.artistCreate, name='artist_create'),
    path('artist/<str:artist_id>', views.artistDetail, name='artist_detail'),
    path('artists/', views.artistList, name='artist_list'),
    path('genre/<int:pk>', views.genreDetail, name='genre_detail'),
    path('genre/<slug:name>', views.genreDetailSlug, name='genre_detail_slug'),
    path('genre-create/', views.genreCreate, name='genre_create'),
    path('genres/', views.genreList, name='genre_list'),
    path('album/<str:album_id>', views.albumDetail, name='album_detail'),
    path('album-create/', views.albumCreate, name='album_create'),
    path('albums/', views.albumList, name='album_list'),
    path('track/<str:track_id>', views.trackDetail, name='track_detail'),
    path('track-create/', views.trackCreate, name='track_create'),
    path('tracks/', views.trackList, name='track_list'),
    path('listen-log/<str:posix_tmstmp>', views.listenLogDetail, name='listen_log_detail'),
    path('listen-log-create/', views.listenLogCreate, name='listen_log_create'),
    path('listen-logs/', views.listenLogList, name='listen_log_list'),
    path('artist-listens-month/<str:month>/<str:year>', views.artistListenLogsMonth),
    path('track-listens-month/<str:month>/<str:year>', views.trackListenLogsMonth),
    path('artist-listens-year/<str:year>', views.artistListenLogsYear),
    path('track-listens-year/<str:year>', views.trackListenLogsYear),
    path('artist-listen-logs/<str:artist_id>/', views.artistListenLogs),
    path('artist-listen-logs/<str:artist_id>/<str:year>/', views.artistListenLogs),
    path('artist-listen-logs/<str:artist_id>/<str:year>/<str:month>', views.artistListenLogs)
]
