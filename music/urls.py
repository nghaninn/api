from django.urls import path, re_path, include
from . import views
from .views import SongsList, SongsDetail

urlpatterns = [
    # path('',  views.index, name='index'),
    path('', SongsDetail.as_view(), name="songs-create"),
    re_path(r'^((?P<id>\d+)/)$', SongsList.as_view(), name="songs-all"),
    # 'api/(?P<version>(v1|v2))/'
    # path('songs/', ListSongsView.as_view(), name="songs-all"),
]
