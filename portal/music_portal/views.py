import os

from django.conf import settings
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404

from portal.music_portal.models import Artist, Music, Genre, Video


class HomePage(TemplateView):
    template_name = 'music_portal/home.html'

    def get_context_data(self, **kwargs):
        genre_id = self.request.GET.get('genre_id')
        musician_id = self.request.GET.get('musician_id')
        filter = None

        music_list = Music.objects.all()
        if genre_id:
            music_list = music_list.filter(genre_id=genre_id)
            filter = Genre.objects.get(id=genre_id).name
        if musician_id:
            music_list = music_list.filter(artist_id=musician_id)
            filter = Artist.objects.get(id=musician_id).nick_name

        context = super().get_context_data(**kwargs)
        context['music_list'] = music_list
        context['genres'] = Genre.objects.all()
        context['filter'] = filter

        artists = set()
        for music in Music.objects.all():
            artists.add(music.artist)

        context['musicians'] = artists

        for artist in artists:
            artist.music_count = Music.objects.filter(artist=artist).count()

        return context


class VideosList(ListView):
    template_name = 'music_portal/videos.html'
    model = Video

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.filter(is_active=True)
        return context


def download(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    file_path = os.path.join(settings.MEDIA_ROOT, music.audio.url)[1:]
    print(file_path)
    print(os.path.exists('media/audio/Akku_arman.mp3'))

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        print('not exist')
    raise Http404
