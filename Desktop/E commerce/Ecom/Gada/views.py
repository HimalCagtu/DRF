from django.shortcuts import render, redirect
from .forms import UserForm,LoginForm
from .models import *
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def signup_form(request):
    if request.user.is_authenticated:
        return redirect('home')
    page = 'signup'
    form = UserForm()
    context = {'form': form}

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            obj =  form.save(commit=False)
            obj.avatar = request.FILES.get('image')
            obj.save()
            return redirect('signup')
        

    return render(request, 'form.html',{'form':form,'page':page})


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email = email)

        except:
            return HttpResponse('User does not exist')

        user = authenticate(email = email, password = password)

        if user:
            login(request, user)
            return redirect('home')


    return render(request, 'form.html')

def logoutpage(request):
 
    logout(request)

    

def homepage(request):

    product = Product.objects.all().order_by('-price')
    context = {'product':product}
    

    return render(request,'home.html',context)