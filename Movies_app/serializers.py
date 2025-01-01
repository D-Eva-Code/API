from rest_framework import serializers
from .models import Movie

class Movieserializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'duration', 'rating', 'typ']
