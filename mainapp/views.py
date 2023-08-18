from django.shortcuts import render
from django.http import HttpRequest
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Item
from .serializers import PersonSerializer, ItemSerializer

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

class PersonAPIList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonAPIUpdate(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 

class PersonAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 

class ItemAPIview(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
