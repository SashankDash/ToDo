from django.shortcuts import render,HttpResponse
from .models import Task
# Create your views here.
def home (request):
    context = {'sucess' : False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']

        ins =Task(taskTitle =title, taskDesc = desc)
        ins.save()

        context = {'sucess' : True}
        
    
    return render(request,'todo_app/index.html',context)

def task (request):

    allTasks = Task.objects.all()
    context = {'tasks':allTasks}
    return render(request,'todo_app/task.html',context)
