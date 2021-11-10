from rest_framework import generics
from .serializers import *
from django.shortcuts import render

class SongAPIView(generics.ListCreateAPIView):
     queryset = Song.objects.all()
     serializer_class = SongSerializer


class SongAPIViewID(generics.RetrieveUpdateDestroyAPIView):
          queryset = Song
          serializer_class = SongSerializer



class PodcastAPIView(generics.ListCreateAPIView):
     queryset = Podcast.objects.all()
     serializer_class = PocastSerializer


class PodcastAPIViewID(generics.RetrieveUpdateDestroyAPIView):
     queryset = Podcast
     serializer_class = PocastSerializer



class AudiobookAPIView(generics.ListCreateAPIView):
     queryset = Audiobook.objects.all()
     serializer_class = AudioBookSerializer

class AudiobookAPIViewID(generics.RetrieveUpdateDestroyAPIView):
     queryset = Audiobook
     serializer_class = AudioBookSerializer
