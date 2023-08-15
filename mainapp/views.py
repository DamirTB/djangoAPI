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

class PersonAPIview(APIView):
    def get(self, request):
        lst = Person.objects.all().values()
        return Response({'post': list(lst)})
    def post(self, request):
        post_new = Person.objects.create(
            first_name=request.data['first_name'],
            last_name=request.data['sur_name']
        )
        return Response({'post' : model_to_dict(post_new)})

#class PersonAPIview(generics.ListAPIView):
#    queryset = Person.objects.all()
#    serializer_class = PersonSerializer

class ItemAPIview(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
