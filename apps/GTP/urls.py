from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.view_task, name = 'task'),
    path('task', views.add_task, name = 'add_task')
]