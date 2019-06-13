from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView
from mutagen.mp3 import MP3

from portal.music_portal.models import Music, Artist, Genre, Video
from .forms import GenreForm, ArtistForm, MusicForm, VideoForm


@method_decorator([login_required(login_url='/django-admin/login')], name='dispatch')
class MusicListView(ListView):
    template_name = 'admin_side/music_list.html'
    model = Music

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['music_list'] = Music.objects.all()
        return context


@method_decorator([login_required(login_url='/django-admin/login')], name='dispatch')
class MusicFormView(FormView):
    form_class = MusicForm
    template_name = 'admin_side/music_form.html'

    def get_initial(self):
        initial = super(MusicFormView, self).get_initial()
        if self.kwargs.get('id'):
            initial['music'] = get_object_or_404(Music, id=self.kwargs['id'])
        return initial

    def form_valid(self, form):
        music = self.get_initial().get('music')
        if music:
            # update music
            form.instance = get_object_or_404(Music, id=music.id)
            new_artist = Artist.objects.get(id=form.data.get('artist'))

            if new_artist != music.artist:
                music.artist.music_count -= 1
                music.artist.save()
                new_artist.music_count += 1
                new_artist.save()

            music.update(form.data)
        else:
            # create music
            form.save(commit=True)
        return redirect(reverse('music_list'))

    def get_context_data(self, **kwargs):
        if self.kwargs.get('id'):
            kwargs['music'] = get_object_or_404(Music, id=self.kwargs['id'])
        return super().get_context_data(**kwargs)


@login_required(login_url='/django-admin/login')
def delete_music(request, id):
    music = get_object_or_404(Music, id=id)
    music.artist.music_count -= 1
    music.artist.save()
    music.delete()
    return redirect(reverse('music_list'))


@method_decorator([login_required(login_url='/django-admin/login')], name='dispatch')
class ArtistListView(ListView):
    template_name = 'admin_side/artists_list.html'
    model = Artist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['musicians'] = Artist.objects.all()
        print(context['musicians'])
        return context


@method_decorator([login_required(login_url='/django-admin/login')], name='dispatch')
class ArtistFormView(FormView):
    form_class = ArtistForm
    template_name = 'admin_side/artist_form.html'

    def get_initial(self):
        initial = super(ArtistFormView, self).get_initial()
        if self.kwargs.get('id'):
            initial['artist'] = get_object_or_404(Artist, id=self.kwargs['id'])
        return initial

    def form_valid(self, form):
        artist = self.get_initial().get('artist')

        if artist:
            # update artist
            form.instance = get_object_or_404(Artist, id=artist.id)
            artist.updated_by = self.request.user
            artist.update(form.data)
        else:
            # create artist
            artist = form.save(commit=True, user=self.request.user)

        print(artist.nick_name, artist.id)
        return redirect(reverse('artists_list'))

    def get_context_data(self, **kwargs):
        if self.kwargs.get('id'):
            kwargs['artist'] = get_object_or_404(Artist, id=self.kwargs['id'])
        return super().get_context_data(**kwargs)


@login_required(login_url='/django-admin/login')
def delete_artist(request, id):
    artist = get_object_or_404(Artist, id=id)
    artist.delete()
    return redirect(reverse('artists_list'))


@method_decorator([login_required(login_url='/django-admin/login')], name='dispatch')
class GenreListView(ListView):
    template_name = 'admin_side/genres_list.html'
    model = Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context


@method_decorator([login_required(login_url='/django-admin/login')], name='dispatch')
class GenreFormView(FormView):
    form_class = GenreForm
    template_name = 'admin_side/genre_form.html'

    def get_initial(self):
        initial = super(GenreFormView, self).get_initial()
        if self.kwargs.get('id'):
            initial['genre'] = get_object_or_404(Genre, id=self.kwargs['id'])
        return initial

    def form_valid(self, form):
        genre = self.get_initial().get('genre')
        if genre:
            # update genre
            form.instance = get_object_or_404(Genre, id=genre.id)
            genre.update(form.data)
        else:
            # create genre
            form.save(commit=True)
        return redirect(reverse('genres_list'))

    def get_context_data(self, **kwargs):
        if self.kwargs.get('id'):
            kwargs['genre'] = get_object_or_404(Genre, id=self.kwargs['id'])
        return super().get_context_data(**kwargs)


@login_required(login_url='/django-admin/login')
def delete_genre(request, id):
    genre = get_object_or_404(Genre, id=id)
    genre.delete()
    return redirect(reverse('genres_list'))


@method_decorator([login_required(login_url='/django-admin/login')], name='dispatch')
class VideoListView(ListView):
    template_name = 'admin_side/video_list.html'
    model = Video

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        return context


@method_decorator([login_required(login_url='/django-admin/login')], name='dispatch')
class VideoFormView(FormView):
    form_class = VideoForm
    template_name = 'admin_side/video_form.html'

    def get_initial(self):
        initial = super(VideoFormView, self).get_initial()
        if self.kwargs.get('id'):
            initial['video'] = get_object_or_404(Video, id=self.kwargs['id'])
        return initial

    def form_valid(self, form):
        video = self.get_initial().get('video')
        if video:
            # update video
            form.instance = get_object_or_404(Video, id=video.id)
            video.update(form.data)
        else:
            # create video
            form.save(commit=True)
        return redirect(reverse('videos_list'))

    def get_context_data(self, **kwargs):
        if self.kwargs.get('id'):
            kwargs['video'] = get_object_or_404(Video, id=self.kwargs['id'])
        return super().get_context_data(**kwargs)


@login_required(login_url='/django-admin/login')
def delete_video(request, id):
    video = get_object_or_404(Video, id=id)
    video.delete()
    return redirect(reverse('videos_list'))


@login_required(login_url='/django-admin/login')
def change_status_video(request, id):
    video = get_object_or_404(Video, id=id)
    video.is_active = not video.is_active
    video.save()
    return redirect(reverse('videos_list'))

