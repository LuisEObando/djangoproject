from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Django Course'
    return render(request, 'index.html', 
                  {
                      'title': title
                  })

def about(request):
    username = 'luis'
    return render(request, 'about.html',
                  {
                      'username': username
                  })

def hello(request, username):
    print(username)
    
    return HttpResponse('<h2>Hello %s<h2>' %username)

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',
                  {
                      'projects': projects
                  }
                  )

def tasks(request):
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, title=title)
    #task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html',
                  {
                      'tasks': tasks
                  })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html',
                    {
                        'form': CreateNewProject()
                    })
    else:
        project = Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    task = Task.objects.filter(project_id=id)
    return render (request, 'projects/project_detail.html',
                   {
                       "project": project,
                       "task":task
                   })