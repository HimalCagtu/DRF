from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
@csrf_exempt
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
     
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form.save()
        return redirect ('home')


    return render(request, 'signup.html',{'form':form,})


@csrf_exempt
def loginpage(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('home')
    

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username =username)

        except :
            messages.warning(request,'user or pass invalid')
            return redirect('login')

        user = authenticate(request, username = username , password=password)
    
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'signup.html', {'page':page})


# Create your views here.
@login_required(login_url='login')
def home(request):
    completed = Completed.objects.filter(user =request.user).order_by('-created')[:5]
    form = TaskForm()
    tasks = Task.objects.filter(user = request.user).order_by('due')[:3]

    if request.method =='POST':
        user = request.user
        name = request.POST.get('name')
        due = request.POST.get('due')
        try:
            add =Task.objects.create(user = user , name = name, due =due)
            add.save()
        except:
             if len(name) <3 :
                messages.error(request,'Task name invalid')

             else:
                 messages.error(request,'Please select date')
            
        return redirect('home')
            



    return render(request, 'create.html',{'form':form,'tasks':tasks,'completed':completed})


def logoutpage(request):
    logout(request)
    return redirect('home')

def delete(request, pk):
    task =Task.objects.get(id =pk)

    task.delete()

    return redirect('home')

def edittask(request, pk):
    task = Task.objects.get(id =pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form  = TaskForm(request.POST, instance= task)
        obj = form.save(commit=False)
        obj.user = request.user
        
        obj.save()
        return redirect('home')

        
   
 

    return render(request,'edit.html',{'form':form,'task':task} )

def completed(request , pk):
        # complete = Completed.objects.get(user =request.user)
        task = Task.objects.get(id = pk)
        
        complete = Completed.objects.create(user = request.user , ctask =task)
        
        task.delete()
        
        

        return redirect('home')

def removecompleted(request, pk):

    task = Completed.objects.get(id =pk)

    task.delete()
    return redirect('home')