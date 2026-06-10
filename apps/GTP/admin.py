from django.contrib import admin
from .models import Task

@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('nome', 'prioridade' ,'prazo', 'status')

    
# Register your models here.
