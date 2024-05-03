from django.urls import path, include
from .views import LandingPageAPIView,ArtistAPIView,ArtistDetailAPIView,AlbomAPIView,AlbomDetailAPIView,SongAPIViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix="songs", viewset=SongAPIViewSet)

urlpatterns = [
    path("landing/", LandingPageAPIView.as_view(), name="landing"),
    path("artists/", ArtistAPIView.as_view(), name="artists"),
    path("artists/<int:id>/", ArtistDetailAPIView.as_view(), name="artists-detail"),
    path("", include(router.urls), name="songs"),
    path("alboms/", AlbomAPIView.as_view(), name="alboms"),
    path("alboms/<int:id>/", AlbomDetailAPIView.as_view(), name="albom-detail"),
]
