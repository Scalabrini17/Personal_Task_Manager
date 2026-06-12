from django.shortcuts import render
from .models import Task
from .forms import TaskForms

def view_task(request):
    get_task = Task.objects.all()
    context = {
        'get_task': get_task,
    }

    return render(request, 'task/task.html', context)

def add_task(request):
    form = TaskForms
    if request.method == "POST":
        form = TaskForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    return render(request, 'task/addTask.html', {'form': form})




