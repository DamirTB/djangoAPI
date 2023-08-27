from django.urls import path, include
from . import views

urlpatterns = [
    path('personlist/', views.PersonAPIList.as_view(), name="personlist"),
    path('itemlist/', views.ItemAPIview.as_view()),
    path('personlist/<int:pk>/', views.PersonAPIDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]