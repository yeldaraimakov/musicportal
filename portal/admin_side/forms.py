from django import forms

from mutagen.mp3 import MP3

from portal.music_portal.models import Music, Artist, Genre, Video


class MusicForm(forms.ModelForm):
    initial_fields = ['name', 'artist', 'genre', 'audio', 'word_author', 'music_author', ]

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial')
        self.music = kwargs.get('initial').get('music')
        for key in self.initial_fields:
            if hasattr(self.music, key):
                initial[key] = initial.get(key) or getattr(self.music, key)
        kwargs['initial'] = initial
        super(MusicForm, self).__init__(*args, **kwargs)
        if self.music and self.music.id:
            self.fields['audio'].widget.attrs['disabled'] = True

    def save(self, commit=True):
        music = super(MusicForm, self).save(commit=False)

        music.audio_len = MP3(music.audio).info.length

        if commit:
            music.save()

        return music

    class Meta:
        model = Music
        fields = ['name', 'artist', 'genre', 'audio', 'word_author', 'music_author', ]


class ArtistForm(forms.ModelForm):
    initial_fields = ['first_name', 'last_name', 'nick_name', ]

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial')
        self.artist = kwargs.get('initial').get('artist')
        for key in self.initial_fields:
            if hasattr(self.artist, key):
                initial[key] = initial.get(key) or getattr(self.artist, key)
        kwargs['initial'] = initial
        super(ArtistForm, self).__init__(*args, **kwargs)

    def save(self, commit=True, user=None):
        artist = super(ArtistForm, self).save(commit=False)

        if commit:
            artist.updated_by = user
            artist.save()

        return artist

    class Meta:
        model = Artist
        fields = ['first_name', 'last_name', 'nick_name', ]


class GenreForm(forms.ModelForm):
    initial_fields = ['name', ]

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial')
        self.genre = kwargs.get('initial').get('genre')
        for key in self.initial_fields:
            if hasattr(self.genre, key):
                initial[key] = initial.get(key) or getattr(self.genre, key)
        kwargs['initial'] = initial
        super(GenreForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Genre
        fields = ['name', ]


class VideoForm(forms.ModelForm):
    initial_fields = ['title', 'description', 'url']
    description = forms.CharField(label='Түсіндерме', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial')
        self.video = kwargs.get('initial').get('video')
        for key in self.initial_fields:
            if hasattr(self.video, key):
                initial[key] = initial.get(key) or getattr(self.video, key)
        kwargs['initial'] = initial
        super(VideoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Video
        fields = ['title', 'description', 'url']
