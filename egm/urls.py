from django.urls import path
from egm import views

urlpatterns = [
    path('', views.egm, name='egm'),
    path('egm-form/', views.createEgm, name='egm-form') ,
    path('cabinet-form/', views.createCabinet, name='cabinet-form') ,
    path('platform-form/', views.createPlatform, name='platform-form') ,
    path('cabinet/', views.cabinet, name='cabinet') ,
    path('platform/', views.platform, name='platform') ,
    path('egm-edith/<str:pk>/', views.edithEgm, name='egm-edith'),
    path('platform-edith/<str:pk>/', views.edithPlatform, name='platform-edith'),
    path('cabinet-edith/<str:pk>/', views.edithCabinet, name='cabinet-edith'),
]
