from django.urls import *
from . import views
from .views import ListSongsView

urlpatterns = [
    path('', views.index),
    path('songs/', ListSongsView.as_view(), name="songs-all"),
]
