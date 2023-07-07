from django.urls import path
from . import views
app_name = 'tasks'
urlpatterns = [
    path('', views.task, name='index'),
    path('add/', views.add, name='add'),
    
]