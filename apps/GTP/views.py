from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForms
from django.contrib import messages


def view_task(request):
    get_task = Task.objects.all()
    context = {
        'get_task': get_task,
    }

    return render(request, 'task/task.html', context)

def add_task(request):
    if request.method == "POST":
        form = TaskForms(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Task salva com sucesso")
            return render(request, 'task/task.html', {'form': form})

    else:
        form = TaskForms()

    return render(request, 'task/addTask.html', {'form': form})

