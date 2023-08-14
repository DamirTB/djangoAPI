from django.contrib import admin
from .models import Person, Item
# Register your models here.

admin.site.register(Item)
admin.site.register(Person)