from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Status, Localizacao
from .forms import TaskForms
from django.contrib import messages
import requests

def home(request):
    try:
        response = requests.get('https://api.github.com/repos/Scalabrini17/Personal_Task_Manager/commits')

        response.raise_for_status()

        dados = response.json()

        if dados:
            ultimo_commit = (dados[0]["commit"]["message"])
        else:
            ultimo_commit = 'Não existem novas atualizações :('

    except requests.exceptions.RequestException:
        print('Não foi possivel consultar o GitHub')
        ultimo_commit = 'Não foi possível consultar o GitHub.'

    context = {
        'ultimo_commit': ultimo_commit
    }

    return render(request, 'task/home.html', context)

def view_task(request):
    get_task = Task.objects.filter(status__in = [Status.EM_ESPERA, Status.INICIADO], localizacao = Localizacao.ATIVA)
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
    print("ENTROU NA VIEW")
    task = Task.objects.get(id = id)
    form = TaskForms(instance = task)

    if request.method == 'POST':
        print("Recebi um POST")
        form = TaskForms(request.POST, instance = task)
        
        valido = form.is_valid()

        print("É válido?", valido)
        print("Erros:", form.errors)

        if valido:
            print("FORMULÁRIO VÁLIDO")
            form.save()
            messages.success(request, "Task editada com sucesso!")
            return redirect('task:task')
    
    return render(request, 'task/editarTask.html', {'form': form})

def visualizar_task(request, id):
    task = Task.objects.get(id = id)
    return render(request, 'task/visualizarTask.html', {'task': task})

def task_finalizada(request):
    get_task = Task.objects.filter(status = Status.FINALIZADO, localizacao = Localizacao.ATIVA)
    context = {
        'get_task': get_task,
    }

    return render(request, 'task/taskFinalizada.html', context)

def finalizar_task(request, id):
    task = get_object_or_404(Task, id = id)
    task.status = Status.FINALIZADO
    task.save()

    messages.success(request, 'Task finalizada com sucesso!')
    return redirect('task:task')

def mandar_task_lixo(request, id):
    task = get_object_or_404(Task, id = id)
    task.localizacao = Localizacao.LIXEIRA
    task.save()
    messages.success(request, 'Task movida para a lixeira com sucesso!')
    return redirect('task:task')

def lixeira_task(request):
    get_task = Task.objects.filter(localizacao = Localizacao.LIXEIRA)
    context = {
        'get_task': get_task,
    }
    return render(request, 'task/lixeiraTask.html', context)

def restaurar_task(request, id):
    task = get_object_or_404(Task, id = id)

    task.localizacao = Localizacao.ATIVA 
    task.save()
    messages.success(request, 'Task restaurada com sucesso!')
    return redirect('task:lixeiraTask')