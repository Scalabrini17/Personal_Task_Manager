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
            'descricao': 'Descrição',
            'prazo': 'Prazo',
            'prioridade': 'Prioridade',
            'status': 'Status'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.TextInput(attrs={'class':'form-control'}),
            'prazo': forms.DateInput(format= '%d/%m/%Y', attrs={'type': 'date', 'class':'form-control'}),
            'prioridade': forms.Select(attrs={'class':'form-select'}),
            'status': forms.Select(attrs={'class':'form-select'}),

        }