from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('task', views.view_task, name = 'task'),
    path('addTask', views.add_task, name = 'add_task')
]