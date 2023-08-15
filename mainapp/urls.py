from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/personlist', views.PersonAPIview.as_view()),
    path('api/itemlist', views.ItemAPIview.as_view()),
]