from rest_framework import serializers
from api.models import *


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Song
        fields = '__all__'


class PocastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'


class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = '__all__'