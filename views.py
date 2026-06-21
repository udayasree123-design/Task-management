from django.shortcuts import render,redirect
from.forms import RegistrationForm,LoginForm

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib .auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from .models import Task,TaskHistory

# Create your views here.
def register(request):
    form=RegistrationForm()
    form1=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        form1=RegistrationForm(request.POST)
        if form.is_valid() and form1.is_valid():
            print("valid")
            form.save()
            return redirect('login')
        else:
            form=RegistrationForm()
            form1=RegistrationForm()
    context={
        'form':form,
        'form1':form1
    } 
    return render(request, 'register.html', {'form': form,'form1':form1})

def log_in(request):
    a=None
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            un=form.cleaned_data['username']
            pswd=form.cleaned_data['password']
            try:
                a=User.objects.get(username=un)
            except:
                messages.error(request,"user not found")
            if a:
                user=authenticate(request,username=un,password=pswd)
                if user:
                    print(user)
                    login(request,user)
                    return redirect("display")
                else:
                    messages.error(request,"password incorrect")
    context={
        'form':form
    }
    return render(request,'login.html',context)



def display(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        Task.objects.create(
            name=name,
            desc=desc
        )
        return redirect('display')
    return render(request,'display.html')


def list_of_tasks(request):
    data=Task.objects.all()
    return render(request,'list_of_tasks.html',{'data':data})


def edit_tasks(request,id):
    task= Task.objects.get(id=id)
    if request.method=="POST":
        task.name=request.POST.get('name')
        task.desc=request.POST.get('desc')
        task.save()
        return redirect('list_of_tasks')
    return render(request,'edit_tasks.html',{'task':task})


def delete_tasks(request,id):
    task=Task.objects.get(id=id)
    TaskHistory.objects.create(
        name=task.name,
        desc=task.desc
    )
    task.delete()
    return redirect('list_of_tasks')

def history(request):
    data=TaskHistory.objects.all().order_by('-deleted_at')
    data.is_history=True
    return render(request,'history.html',{'data':data})

def log_out(request):
    logout(request)
    return redirect("login")
