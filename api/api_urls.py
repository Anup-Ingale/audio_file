from django.urls import path,include
from .api_views import *

urlpatterns = [
    path('',SongAPIView.as_view(),name='song'),
    path('song/<int:pk>',SongAPIViewID.as_view(),name='song_id'),

    path('podcast/',PodcastAPIView.as_view(),name='podcast'),
    path('podcast/<int:pk>/',PodcastAPIViewID.as_view(),name='podcast_id'),

    path('audiobook/',AudiobookAPIView.as_view(),name='audiobook'),
    path('audiobook/<int:pk>/',AudiobookAPIViewID.as_view(),name='audiobook_id'),
]