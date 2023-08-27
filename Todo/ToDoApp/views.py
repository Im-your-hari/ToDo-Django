from django.shortcuts import render,redirect
from .models import ToDo

# Create your views here.
def index(request):
    tasks = ToDo.objects.all()
    context = {'tasks' : tasks}
    return render(request, 'index.html',context)

def addtask(request):

    taskname = request.POST['taskname']
    #print(taskname)
    context ={'taskname' : taskname}

    ToDo(name=taskname).save()
    return redirect(request.META['HTTP_REFERER'])

def deletetask(request, taskid):
    task = ToDo.objects.filter(id=taskid)
    task.delete()
    return redirect(request.META['HTTP_REFERER'])

def updatetask(request, taskid):
    pass