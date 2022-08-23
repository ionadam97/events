from django.urls import path
from egm import views

urlpatterns = [
    path('', views.egm, name='egm'),
    path('egm-form', views.createEgm, name='egm-form') ,
    path('cabinet-form', views.createCabinet, name='cabinet-form') ,
    path('platform-form', views.createPlatform, name='platform-form') ,
    path('location-form', views.createLocation, name='location-form') ,
]
