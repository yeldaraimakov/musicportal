from django.urls import path

from portal.music_portal.api import views

urlpatterns = [
    path('music/', views.MusicList.as_view(), name='all_music'),
]
