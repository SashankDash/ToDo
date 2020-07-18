from django.shortcuts import render,HttpResponse
from .models import Task
# Create your views here.
def home (request):
    sucess = 'False'
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']

        ins =Task(taskTitle =title, taskDesc = desc)
        ins.save()

        sucess = 'True'
        
    
    return render(request,'todo_app/index.html',{'sucess':sucess})

def task (request):
    return render(request,'todo_app/task.html')
