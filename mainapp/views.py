from django.shortcuts import render
from django.http import HttpRequest
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

class PersonAPIview(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
