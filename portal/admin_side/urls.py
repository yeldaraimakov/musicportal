from django.urls import path

from portal.admin_side import views

urlpatterns = [
    path('music/', views.MusicListView.as_view(), name='music_list'),
    path('music/create/', views.MusicFormView.as_view(), name='music_create'),
    path('music/update/<int:id>', views.MusicFormView.as_view(), name='music_update'),
    path('music/delete/<int:id>', views.delete_music, name='music_delete'),

    path('musicians/', views.ArtistListView.as_view(), name='artists_list'),
    path('musicians/create/', views.ArtistFormView.as_view(), name='artist_create'),
    path('musicians/update/<int:id>', views.ArtistFormView.as_view(), name='artist_update'),
    path('musicians/delete/<int:id>', views.delete_artist, name='artist_delete'),

    path('genres/', views.GenreListView.as_view(), name='genres_list'),
    path('genres/create/', views.GenreFormView.as_view(), name='genre_create'),
    path('genres/update/<int:id>', views.GenreFormView.as_view(), name='genre_update'),
    path('genres/delete/<int:id>', views.delete_genre, name='genre_delete'),
]