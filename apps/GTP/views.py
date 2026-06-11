from django.shortcuts import render
from .models import Task

def view_task(request):
    get_task = Task.objects.all()
    context = {
        'get_task': get_task,
    }

    return render(request, 'task/task.html', context)




