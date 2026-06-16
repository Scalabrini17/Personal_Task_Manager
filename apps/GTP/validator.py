from django.core.exceptions import ValidationError
from .models import Task 

def validacao_nome_duplicado(value):
    
    if Task.objects.filter(nome = value).exists():
        raise ValidationError('O nome da sua task já existe no banco')
   
