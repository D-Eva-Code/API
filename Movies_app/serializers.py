from rest_framework import serializers
from .models import Movie

class Movieserializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length = None, use_url = True)
    class Meta:
        model = Movie
        fields = ['id', 'name', 'duration', 'rating', 'typ', 'image']
