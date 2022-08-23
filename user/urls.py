from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),


    path('profiles', views.profiles, name='profiles'),
    path('user_profile/<str:pk>/', views.userProfile, name='user_profile'),
    path('account/', views.userAccount, name='account'),

    path('edith_account/', views.edithAccount, name='edith_account'),


]