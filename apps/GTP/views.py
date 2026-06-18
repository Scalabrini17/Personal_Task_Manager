from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForms
from django.contrib import messages

def home(request):
    return render(request, 'task/home.html')

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
            return redirect('task:task')

    else:
        form = TaskForms()

    return render(request, 'task/addTask.html', {'form': form})

def excluir_task(request, id):
    task = Task.objects.get(id = id)
    task.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('task:task')

def editar_task(request, id):
    task = Task.objects.get(id = id)
    form = TaskForms(instance = task)

    if request.method == 'POST':
        form = TaskForms(request.POST, instance = task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task editada com suceso!")
            return redirect('task:task')
    
    return render(request, 'task/editar_task.html')