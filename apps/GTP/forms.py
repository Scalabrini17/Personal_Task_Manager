from django import forms
from .models import Task

class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'nome', 'descricao', 'prazo', 'prioridade', 'status',
        ]
        labels = {
            'nome': 'Nome',
            'descicao': 'Descrição',
            'prazo': 'Prazo',
            'prioridade': 'Prioridade',
            'status': 'Status'
        }