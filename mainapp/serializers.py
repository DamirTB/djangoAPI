from rest_framework import serializers
from .models import Person, Item

class PersonSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    class Meta:
        model = Person
        fields = ("id", "first_name", "last_name")
    def create(self, validated_data):
        return Person.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.save()
        return instance


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"