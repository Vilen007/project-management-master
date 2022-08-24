from audioop import reverse
from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from .models import Access, Project, Task, Info, Comment, Commenttask
from django.contrib.auth.models import auth, User
from django.contrib.auth import logout
from django.contrib import messages
from .form import ProjectCreate, TaskCreate, InfoCreate, CommentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .utils import get_missions
import bs4, helium

def login(req):
    if req.method == 'POST':
        username = req.POST['uname']
        password = req.POST['psw']
        u = auth.authenticate(username=username, password=password)
        if u is not None:
            auth.login(req, u)
            return redirect('../projects')
        else:
            messages.info(req, 'كلمة السر غير صحيحة.')
            return redirect('./')
    else:
        return render(req, 'login.html')
    
def logoutt(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return render(request, 'login.html')

def missions(request):
    return render(request, "missions.html", {"missions": get_missions()})


def projects(request):
    if request.user.is_authenticated:
        print(request.user)
        if request.user.id == 1:
            proj = Project.objects.all()
        else:
            proj = Project.objects.filter(userId=request.user.id)

        # form = ProjectCreate()
        context = {
            'proj': proj,
            # 'form': form
        }
        print(context)
        return render(request, 'projects.html', context)
    return redirect('/login')


def upload(request):
    upload = ProjectCreate()
    if request.method == 'POST':
        upload = ProjectCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('projects')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'upload.html', {'upload_form': upload})


def update_project(request, project_id):
    project_id = int(project_id)
    try:
        project_sel = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return redirect('projects')
    project_form = ProjectCreate(request.POST or None, instance=project_sel)
    if project_form.is_valid():
        project_form.save()
        return redirect('projects')
    return render(request, 'upload.html', {'upload_form': project_form})



class ProjectDelete(DeleteView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy(projects)
    template_name = 'Delete_confirm.html'


def project_details(request, pk):
    display_users = Access.objects.all()
    project_id = int(pk)
    try:
        project_sel = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return redirect('index')
    print(display_users)

    #infos = Info.objects.filter(project_Id=int(pk)).first()

    return render(request, 'project-details.html', {"project":project_sel ,"users": display_users })


def tasks(request, pk):
    comments = Comment.objects.all()
    try:
        _tasks = Task.objects.filter(project_Id=int(pk))
    except Task.DoesNotExist:
        return redirect('index')
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.user= request.user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'tasks.html', {'tasks': _tasks, 'project_id': pk, 'comment_form': comment_form, 'comments': comments})

def detail_task(request,pk):
    comments = Commenttask.objects.filter(task_id=pk)
    try:
        task = Task.objects.get(id = int(pk))
    except Task.DoesNotExist:
        return redirect('index')
    return render(request, 'task_details.html', {'task': task, 'project_id': pk  , 'comments': comments})

    # task = Task.objects.filter(id = int(pk))
    # return render(request, 'task_details.html',{'tasks':task})

def taskComment(request,pk):
    comments = Commenttask.objects.filter(task_id=pk)
    try:
        task = Task.objects.get(id = int(pk))
    except Task.DoesNotExist:
        return redirect('index')
    if request.method == 'POST':
        user = request.user
        comment = request.POST['comment']
        id = request.POST['id']
        savecomment = Commenttask(user=user, body=comment, task_id=id)
        savecomment.save()
    return render(request, 'task_details.html', {'task': task, 'comments': comments})


# create task
def uploadtask(request, pk):
    print(request, pk)
    upload = TaskCreate()
    if request.method == 'POST':
        upload = TaskCreate(request.POST, request.FILES)

        if upload.is_valid():
            # upload.project_Id = pk
            form = upload.save(commit=False)
            project = Project.objects.get(id=pk)
            form.project_Id = project
            form.save()
            return redirect('..')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'uploadtask.html', {'uploadtask_form': upload})


def update_task(request, proj,pk):
    task = Task.objects.get(id=pk)

    form = TaskCreate(instance=task)

    if request.method == 'POST':
        form = TaskCreate(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('..')

    return render(request, 'uploadtask.html', {'uploadtask_form': form})


class TaskDelete(DeleteView):
    model = Task
    fields = '__all__'
    success_url = '..'
    template_name = 'Delete_confirm.html'

def getUser(request):
    if request.user.is_superuser:
        display_users = User.objects.all()
        if request.method == 'POST':  # If the form has been submitted...
            userid = request.POST.get('select_user')
            if userid:
                user = User.objects.get(id=userid)

                if request.POST.get('create_project'):
                    user.is_staff = 1
                    user.save()
        return render(request, 'settings.html', {"users": display_users})
    return redirect('projects')

# def infos(request, pk):
#     try:
#         _infos = Info.objects.filter(project_Id=int(pk))
#     except Info.DoesNotExist:
#         return redirect('index')
#
#     return render(request, 'details_info.html', {'infos': _infos, 'project_id': pk})

def info(request, pk):
    # display_infos = Info.objects.filter()
    # print(display_infos)
    # return render(request, 'details_info.html', {"infos": display_infos})
    try:
        _infos = Info.objects.filter(project_Id=int(pk))
    except Info.DoesNotExist:
        return redirect('index')

    return render(request, 'details_info.html', {'infos': _infos, 'project_id': pk})

# create info
def uploadinfo(request, pk):
    print(request, pk)
    upload = InfoCreate()
    if request.method == 'POST':
        upload = InfoCreate(request.POST, request.FILES)

        if upload.is_valid():
            # upload.project_Id = pk
            form = upload.save(commit=False)
            project = Project.objects.get(id=pk)
            form.project_Id = project
            form.save()
            return redirect('..')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'uploadinfo.html', {'uploadinfo_form': upload})

def update_info(request, proj,pk):
    infos = Info.objects.get(id=pk)

    form = InfoCreate(instance=infos)

    if request.method == 'POST':
        form = InfoCreate(request.POST, request.FILES, instance=infos)
        if form.is_valid():
            form.save()
            return redirect('..')

    return render(request, 'uploadinfo.html', {'uploadinfo_form': form})

def gettable(request):
    # user_list = User.objects.all()
    project_list = Project.objects.all()
    task_list = Task.objects.all()

    return render(request, 'table_projet.html', {'project_list': project_list, 'task_list': task_list})

def dashboard(request):
    users = User.objects.all()
    active_users = User.objects.all().filter(is_active=True)
    projects = Project.objects.all()
    tasks = Task.objects.all()
    context = {
        'users' : users,
        'active_users' : active_users,
        'projects' : projects,
        'tasks' : tasks,
    }
    return render(request, 'dashboard.html', context)

def projectView(request):
    projects = Project.objects.all()
    avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    tasks = Task.objects.all()
    overdue_tasks = tasks.filter(type='3')
    context = {
        'projects' : projects,
        'avg_projects' : avg_projects,
        'tasks' : tasks,
        'overdue_tasks' : overdue_tasks,
    }
    return render(request, 'projectsview.html', context)

def userView(request):
    users = User.objects.all()
    context = {
        'users': users,

    }
    return render(request, 'usersviews.html', context)