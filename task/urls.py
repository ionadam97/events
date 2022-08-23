from django.urls import path

from task import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('task/<str:pk>/', views.task, name='task'),
    path('edith-task/<str:pk>/', views.edithTask, name='edith-task'),
    path('task-form/', views.createTask, name='task-form') ,
    path('componenta-form/', views.createComponenta, name='componenta-form') ,
    path('rezolutie-form/', views.createRezolutie, name='rezolutie-form') ,
    path('label-form/', views.createLabel, name='label-form') ,
    path('dashboard/', views.dashboard, name='dashboard') ,
    path('tasks-filtred/<str:pk>/', views.taskFilter, name='tasks-filtred') ,
   
]
