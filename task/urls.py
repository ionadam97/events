from django.urls import path

from task import views

urlpatterns = [
    # view
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.tasks, name='tasks'),
    path('tasks-filtred/<str:pk>/', views.taskFilter, name='tasks-filtred'),
    path('task/<str:pk>/', views.task, name='task'),
    path('selectori/', views.selectori, name='selectori'),
    # create
    path('task-form/', views.createTask, name='task-form'),
    path('componenta-form/', views.createComponenta, name='componenta-form'),
    path('rezolutie-form/', views.createRezolutie, name='rezolutie-form'),
    path('label-form/', views.createLabel, name='label-form'),
    # edith
    path('edith-task/<str:pk>/', views.edithTask, name='edith-task'),
    path('edith-componenta/<str:pk>/',
         views.edithComponenta, name='edith-componenta'),
    path('edith-label/<str:pk>/', views.edithLabel, name='edith-label'),
    path('edith-rezolutie/<str:pk>/',
         views.edithRezolutie, name='edith-rezolutie'),



]
