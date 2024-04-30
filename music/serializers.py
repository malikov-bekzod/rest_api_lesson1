from rest_framework import serializers
from .models import Artist,Albom,Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("name","image",)


class AlbomSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Albom
        fields = ("title","artist","image")


class SongSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer()
    class Meta:
        model = Song
        fields = ("title", "albom", "image")
