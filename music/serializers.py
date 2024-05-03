from rest_framework import serializers
from .models import Artist,Albom,Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = (
            "id",
            "name",
            "image",
        )


class AlbomSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    class Meta:
        model = Albom
        fields = ("id", "title", "artist", "image")


class SongSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer(read_only=True)
    class Meta:
        model = Song
        fields = ("id","title", "albom", "image")
