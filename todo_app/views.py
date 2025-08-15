from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Tasks
from django.contrib import messages

# Create your views here.
def homepage(request):
    all_tasks = Tasks.objects.filter(is_completed=False)
    if not all_tasks:
        messages.info(request,"No Tasks to display")
    if request.method == 'POST':
        list = request.POST.getlist('tasks')
        if list:
            for task_id in list:
                selected = Tasks.objects.get(id=task_id)
                selected.is_completed = True
                selected.save()
        return redirect(reverse('home'))
    return render(request,'todo_app/homepage.html',{
        'tasks': all_tasks,
        })

def addtask(request):
    if request.method == "POST":
        task = request.POST.get('newtask').strip()

        if task == "":
            messages.error(request,"Please enter a valid task!")
            return redirect(reverse('newtask'))
        
        Tasks.objects.create(title = task)
        return redirect(reverse('home'))
    return render(request,'todo_app/add_task.html')

def completedtasks(request):
    all_tasks = Tasks.objects.filter(is_completed=True)
    if not all_tasks:
        messages.info(request,"All Tasks Completed")
    if request.method == "POST":
        tasks = request.POST.getlist('tasks')
        if tasks:
            for task_id in tasks:
                Tasks.objects.get(id=task_id).delete()
        return redirect(reverse('completedtask'))
    return render(request, 'todo_app/completed_tasks.html',{
        'tasks':all_tasks,
    })