from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist,Albom,Song
from .serializers import ArtistSerializer,AlbomSerializer,SongSerializer
# Create your views here.

class LandingPageAPIView(APIView):
    def get(self,request):
        return Response(data = {"msg":"you are in langding page"})
    
    def post(self,request):
        return Response(data={"xabar":"this is post method"})


class ArtistAPIView(APIView):
    def get(self,request):
        artists = Artist.objects.all()
        serializers = ArtistSerializer(artists,many=True)
        return Response(data=serializers.data)


class AlbomAPIView(APIView):
    def get(self, request):
        alboms = Albom.objects.all()
        serializers = AlbomSerializer(alboms, many=True)
        return Response(data=serializers.data)


class SongAPIView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializers = SongSerializer(songs, many=True)
        return Response(data=serializers.data)
