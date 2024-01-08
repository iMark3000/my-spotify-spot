from django.urls import path
from . import views

app_nane = 'api'

urlpatterns = [
    path('artists/<str:artist_id>', views.artistDetail, name='artist_detail'),
    path('artists/create/', views.artistCreate, name='artist_create'),
    path('artists/', views.artistList, name='artist_list'),
    path('genres/<int:pk>', views.genreDetail, name='genre_create'),
    path('genres/create/', views.genreCreate, name='genre_create'),
    path('genres/', views.genreList, name='genre_list'),
    path('album/<str:album_id>', views.albumDetail, name='album_detail'),
    path('album/create/', views.albumCreate, name='album_create'),
    path('albums/', views.albumList, name='album_list'),
    path('tracks/<str:track_id>', views.trackDetail, name='track_detail'),
    path('tracks/create/', views.trackCreate, name='track_create'),
    path('tracks/', views.trackList, name='track_list'),

    # Track detail
    # Track create
    # Track list
    # ListenLog query by date since
    # ListenLog query by date range
    # ListenLog query by year
    # ListenLog query by month
    # ListenLog query by hour
    # ListenLog detail
    # ListenLog create
    # ListenLog list
]