from django.db import models
from django.conf import settings
from mutagen.mp3 import MP3


class Artist(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    nick_name = models.CharField(max_length=255)
    music_count = models.IntegerField(default=0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def update(self, data):
        instance = Artist.objects.get(id=self.id)
        instance.first_name = data.get('first_name')
        instance.last_name = data.get('last_name')
        instance.nick_name = data.get('nick_name')
        instance.save()

    def __str__(self):
        return self.nick_name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def update(self, data):
        instance = Genre.objects.get(id=self.id)
        instance.name = data.get('name')
        instance.save()

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, null=True, blank=True)
    audio = models.FileField(upload_to='audio/')
    audio_len = models.FloatField(default=0)
    word_author = models.CharField(max_length=255, blank=True)
    music_author = models.CharField(max_length=255, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def audio_length(self):
        minute = str(int(self.audio_len / 60))
        second = str(int(self.audio_len % 60))

        if len(minute) == 1:
            minute = '0' + minute

        if len(second) == 1:
            second = '0' + second

        return minute + ':' + second

    def update(self, data):
        instance = Music.objects.get(id=self.id)
        instance.name = data.get('name')
        instance.artist = Artist.objects.get(id=int(data.get('artist')))
        instance.genre = Genre.objects.get(id=int(data.get('genre')))
        instance.save()

    def __str__(self):
        return self.name

