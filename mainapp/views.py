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
        lst = Person.objects.all()
        return Response({'post': PersonSerializer(lst, many=True).data})
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post' : serializer.data})
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"Error" : "Method PUT not allowed"})
        try:
            instance = Person.objects.get(pk=pk)
        except:
            return Response({"Error" : "Method PUT not allowed"})
        serializer = PersonSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post' : serializer.data})


#class PersonAPIview(generics.ListAPIView):
#    queryset = Person.objects.all()
#    serializer_class = PersonSerializer    

class ItemAPIview(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
