from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
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


class ArtistDetailAPIView(APIView):
    def get(self, request, id):
        try:
            artist = Artist.objects.get(id=id)
            serializer = ArtistSerializer(artist)
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        artist = Artist.objects.get(id=id)
        artist.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbomAPIView(APIView):
    def get(self,request):
        albums = Albom.objects.all()
        serializer = AlbomSerializer(albums, many=True)
        return Response(data=serializer.data)


class AlbomDetailAPIView(APIView):
    def get(self, request, id):
        try:
            album = Albom.objects.get(id=id)
            serializer = AlbomSerializer(album)
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        album = Albom.objects.get(id=id)
        serializer = AlbomSerializer(instance=album, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        album = Albom.objects.get(id=id)
        serializer = AlbomSerializer(instance=album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        album = Albom.objects.get(id=id)
        album.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class SongAPIViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
