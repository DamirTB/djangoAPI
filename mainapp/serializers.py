from rest_framework import serializers
from .models import Person, Item

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("first_name", "last_name")

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"