from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Movieserializers
from .models import Movie
# Create your views here.

class Movieviewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = Movieserializers