from django.conf import settings
from django.db import models


class Artist(models.Model):
    first_name = models.CharField('Аты', max_length=255, blank=True)
    last_name = models.CharField('Жөні', max_length=255, blank=True)
    nick_name = models.CharField('Лақап аты', max_length=255)

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
    name = models.CharField('Атауы', max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def update(self, data):
        instance = Genre.objects.get(id=self.id)
        instance.name = data.get('name')
        instance.save()

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField('Атауы', max_length=255)
    artist = models.ForeignKey(Artist, verbose_name='Әнші', on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, verbose_name='Жанр', on_delete=models.PROTECT, null=True, blank=True)
    audio = models.FileField()
    audio_len = models.FloatField(default=0)
    word_author = models.CharField('Cөзін жазған', max_length=255, blank=True)
    music_author = models.CharField('Әнін жазған', max_length=255, blank=True)

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
        if data.get('genre') != '':
            instance.genre = Genre.objects.get(id=int(data.get('genre')))
        else:
            instance.genre = None
        instance.word_author = data.get('word_author')
        instance.music_author = data.get('music_author')
        instance.save()

    def __str__(self):
        return self.name


class Video(models.Model):
    YOUTUBE_URL = 'https://www.youtube.com/embed/'

    title = models.CharField('Атауы', max_length=255)
    description = models.CharField('Түсіндірме', max_length=1024, blank=True)
    url = models.CharField('Сілтеме', max_length=255)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def update(self, data):
        instance = Video.objects.get(id=self.id)
        instance.title = data.get('title')
        instance.description = data.get('description')
        instance.url = data.get('url')
        instance.save()

    def __str__(self):
        return self.title + ' ' + self.url

    @property
    def get_url(self):
        splitted_url = self.url.split('=')
        if len(splitted_url) < 2:
            return ''
        return Video.YOUTUBE_URL + splitted_url[1]
