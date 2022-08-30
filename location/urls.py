from django.urls import path
from location import views

urlpatterns = [
    path('', views.locations, name='locations'),
    path('location-form', views.createLocation, name='location-form'),
    path('manager-form', views.createManager, name='manager-form'),
    path('managers', views.managers, name='managers'),
    path('location-edith/<str:pk>/', views.edithLocation, name='location-edith'),
    path('manager-edith/<str:pk>/', views.edithManager, name='manager-edith'),
    path('manager-delete/<str:pk>/', views.deleteManager, name='manager-delete'),

]
