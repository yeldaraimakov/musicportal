from django import forms

from mutagen.mp3 import MP3

from portal.music_portal.models import Music, Artist, Genre


class MusicForm(forms.ModelForm):
    initial_fields = ['name', 'artist', 'genre', 'audio', ]

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

        if commit:
            music.save()
            print(music.audio.url)
            music.audio_len = MP3(music.audio.url).info.length
            music.save()

            music.artist.music_count += 1
            music.artist.save()

        return music

    class Meta:
        model = Music
        fields = ['name', 'artist', 'genre', 'audio', ]


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
