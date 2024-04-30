from django.urls import path
from .views import LandingPageAPIView,ArtistAPIView,AlbomAPIView,SongAPIView

urlpatterns = [
    path("landing/", LandingPageAPIView.as_view(), name="landing"),
    path("artists/", ArtistAPIView.as_view(), name="artists"),
    path("alboms/", AlbomAPIView.as_view(), name="alboms"),
    path("songs/", SongAPIView.as_view(), name="songs"),
]
