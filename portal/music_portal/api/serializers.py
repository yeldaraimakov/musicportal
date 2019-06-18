from rest_framework import serializers

from portal.music_portal.models import Music


class MusicListSerializer(serializers.ModelSerializer):
    artist = serializers.CharField(source='artist.nick_name')

    class Meta:
        model = Music
        fields = ('id', 'name', 'genre', 'artist', 'audio', 'audio_len', 'word_author', 'music_author')
