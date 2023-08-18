from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/personlist', views.PersonAPIList.as_view()),
    path('api/itemlist', views.ItemAPIview.as_view()),
    path('api/personlist/<int:pk>/', views.PersonAPIUpdate.as_view()),
    path('api/persondetail/<int:pk>', views.PersonAPIDetail.as_view()),
]