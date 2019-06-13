from rest_framework import generics

from portal.music_portal.api.serializers import MusicListSerializer
from portal.music_portal.models import Music


class MusicList(generics.ListAPIView):
    serializer_class = MusicListSerializer

    def get_queryset(self):
        queryset = Music.objects.all()
        return queryset
