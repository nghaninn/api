from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer
from django.http import Http404
from rest_framework.schemas import AutoSchema

def index(request, *args, **kwargs):
    x = []
    for i in range(10):
        x.append(i)
    return HttpResponse("<h1>DataFlair Django Tutorials</h1>The Digits are {0}<br>{1}".format(x, kwargs))


class SongsDetail(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = SongsSerializer

    def get_queryset(self):
        return Songs.objects.all()


class SongsList(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides a get method handler.
    """
    # queryset = Songs.objects.all()
    lookup_field = 'id'
    serializer_class = SongsSerializer

    def get_queryset(self):
        return Songs.objects.all()

    def get_object(self):
        try:
            id = self.kwargs.get("id")
            return Songs.objects.get(id=id)
        except Songs.DoesNotExist:
            raise Http404
