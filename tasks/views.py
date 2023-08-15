from django.shortcuts import render, redirect
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks':tasks})

def task_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        Task.objects.create(name=name)
        return redirect('task_list')
    return render(request, 'task_add.html')

def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('task_list')


