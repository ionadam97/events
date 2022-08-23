from django.urls import path
from location import views

urlpatterns = [
    path('', views.locations, name='locations'),
    path('location-form', views.createLocation, name='location-form'),
    path('manager-form', views.createManager, name='manager-form'),

]
