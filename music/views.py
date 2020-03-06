from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer

def index(request):
    x = []
    for i in range(10):
        x.append(i)
    return HttpResponse("<h1>DataFlair Django Tutorials</h1>The Digits are {0}".format(x))

class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
