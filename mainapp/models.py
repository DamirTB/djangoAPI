from django.db import models
from uuid import uuid4

# Create your models here.

class Person(models.Model):
    UUID = models.UUIDField(editable=False, default=uuid4)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    People = models.ManyToManyField(Person)