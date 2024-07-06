from django.shortcuts import render
from task.models import Task
# Create your views here.
def show_task(request):
    tasks = Task.objects.all()
    return render(request, 'ShowTaskManu.html', {'data': tasks})