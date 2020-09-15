from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import TaskForm
from .models import Task
# Create your views here.

def home(request):
    task_list = Task.objects.all()
    task_form = TaskForm()
    return render(request, 'home.html', {'task_list': task_list, 'task_form': task_form})
    
def addOne(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        new_task = form.save(commit=False)
        new_task.save()
    return redirect('home')
