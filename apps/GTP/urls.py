from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('task', views.view_task, name = 'task'),
    path('addTask', views.add_task, name = 'add_task'),
    path('excluirTask/<int:id>/', views.excluir_task, name = 'excluir_task'),
    path('editarTask/<int:id>/', views.editar_task, name = 'editarTask'),
    path('visualizarTask/<int:id>/', views.visualizar_task, name = 'visualizarTask'),
    path('finalizarTask/<int:id>/', views.finalizar_task, name ='finalizarTask'),
    path('taskFinalizada/', views.task_finalizada, name ='task_finalizada'),
    path('mandarTaskLixo/<int:id>/', views.mandar_task_lixo, name = 'mandarTaskLixo'),
    path('lixeiraTask', views.lixeira_task, name = 'lixeiraTask'),
    path('restaurarTask/<int:id>/', views.restaurar_task, name = 'restaurarTask')
]