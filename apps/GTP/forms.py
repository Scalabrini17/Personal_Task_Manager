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
            'descricao': forms.Textarea(attrs={'class': 'form-control','rows': 5}),
            'prazo': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'prioridade': forms.Select(attrs={'class':'form-select'}),
            'status': forms.Select(attrs={'class':'form-select'}),

        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['prazo'].input_formats = ('%Y-%m-%d',)