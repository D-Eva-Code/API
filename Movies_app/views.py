from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Movieserializers
from .models import Movie
# Create your views here.

class Movieviewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = Movieserializers
    
class Actionviewset(viewsets.ModelViewSet):
    queryset = Movie.objects.filter(typ = "Action")
    serializer_class = Movieserializers
    
class Comedyviewset(viewsets.ModelViewSet):
    queryset = Movie.objects.filter(typ = "Comedy")
    serializer_class = Movieserializers