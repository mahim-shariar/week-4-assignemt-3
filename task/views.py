from django.shortcuts import render, redirect
from . import forms
from .models import Task


def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    else:
        task_form = forms.TaskForm(request.POST)
    return render(request, 'add_task.html', {'form': task_form})


def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    else:
        task_form = forms.TaskForm(instance=task)
    return render(request, 'add_task.html', {'form': task_form})

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('show_task')