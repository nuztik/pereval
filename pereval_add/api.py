from rest_framework.generics import ListAPIView
from . import serializers
from . import models


class SeasonListAPIView(ListAPIView):
    serializer_class = serializers.SeasonSerializer

    def get_queryset(self):
        return models.Season.objects.all()


class UsersListAPIView(ListAPIView):
    serializer_class = serializers.UsersSerializer

    def get_queryset(self):
        return models.Users.objects.all()


class CoordsListAPIView(ListAPIView):
    serializer_class = serializers.CoordsSerializer

    def get_queryset(self):
        return models.Coords.objects.all()


class ImagesListAPIView(ListAPIView):
    serializer_class = serializers.ImagesSerializer

    def get_queryset(self):
        return models.Pereval_image.objects.all()


class PerevalAddedListAPIView(ListAPIView):
    serializer_class = serializers.PerevalAddedSerializer

    def get_queryset(self):
        return models.Pereval_added.objects.all()
