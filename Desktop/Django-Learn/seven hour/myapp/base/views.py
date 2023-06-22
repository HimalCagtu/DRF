from django.shortcuts import render,redirect
from .models import Room,Topic,Message
from django.contrib.auth.models import User
from .forms import *
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import  messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# rooms = [

#     {'id':1, 'name':'Let\'s learn python' },
#     {'id':2, 'name':'Design with me' },
#     {'id':3, 'name':'Frontend developers' },
# ]
# Create your views here.



def loginpage(request):
    page='login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method=='POST':
        username = request.POST.get('Username')
        username = username.lower()
        password = request.POST.get("Password")

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, 'User doesnot exist')

        user = authenticate(request, username=username , password=password)

        if user:
            login(request, user)
            return redirect('home')
        
        else:
              messages.error(request, 'Username or pass doesnot exist')


    context={'page':page}
    return render(request, './base/login_register.html', context)

def logoutpage(request):
   
    logout(request)
    return redirect('login')


def signuppage(request):
    form = UserCreationForm()

    if request.method=='POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            obj= form.save(commit=False)
            obj.username=obj.username.lower()
            obj.save()
            login(request , obj)
            return redirect('login')
    else:
        messages.error(request , 'Error occred during registratiom')
    page='signup'

    return render(request, './base/login_register.html',{'form':form})




def home(request):
    q =request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.all()
    room_messages = Message.objects.filter(Q(room__topic__name__contains=q))

    
  
    rooms = Room.objects.filter(Q(topic__name__contains=q) & Q(name__icontains=q))
    total_room = rooms.count()
  
    context = {'rooms':rooms,'topics':topics,'room_count':total_room,'room_messages':room_messages,}
    
    return render(request, './base/home.html',context)

def room(request, pk):
    # room=rooms[1]['id']
    room=Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    comments = Message.objects.all()
    participants = room.participants.all()
    
    
    

    if request.method=='POST':
        
        message = Message.objects.create(user = request.user, room = room , 
                                         body = request.POST.get('comment'))
        room.participants.add(request.user)
        return redirect('room',pk=room.id)

        # if 


    # names=[

    #     {'name':'himal'},
    #     {'name':'suraj'},
    # ]
    context= {
        'room':room,
        'room_messages':room_messages,
        'comments':comments,
        'participants':participants
        
        # 'names':'a'
    }

    return render(request, './base/room.html',context)

def main(request):

    return render(request,'main.html')

@login_required(login_url='/login')
def createroom(request):
    form = RoomForm()
    if request.method=='POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    

    context={'form':form}

    return render (request, './base/room_form.html',context)

@login_required(login_url='login')
def updateroom(request, pk):

    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        # return HttpResponse('Please login as a authorized user')
        messages.error(request,'Not authorized, Please Login as another user')
        return redirect('logout')
        

    if request.method=='POST':
        form= RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, './base/room_form.html',{'room':room,
                                                    'form':form})
@login_required(login_url='login')
def deleteroom(request, pk):
    room= Room.objects.get(id=pk)
    # choice = input("Are you sure?")
    if request.user != room.host:
        messages.error(request, 'Sorry you cannot delete (authorization failed)')
        return redirect('logout')

    form=RoomForm( instance=room)

    if request.method=='POST':
        room.delete()
        return redirect('home')

    

    context={'form':form,
             'room':room}
    
    return render(request, './base/delete.html',context)


@login_required(login_url='login')
def deletecomment(request, pk):
  
    room = Message.objects.get(id=pk)

    if request.user == room.user or request.user.is_superuser:
        if request.method=='POST':
            room.delete()
            return redirect('home')
    
    

    context ={ 'room':room}

    return render(request, './base/delete.html',context)

    pass




@login_required(login_url='login')
def editcomment(request, pk):
    room_message = Message.objects.get(id =pk)
    form = MessageForm(instance=room_message)
    if request.method=='POST':
        form = MessageForm(request.POST , instance=room_message)
        form.save()
        return redirect( 'home')

    
        # body = request.POST.get('body')




    # room_message = Message.objects.get(id = pk)


    return render(request, './base/editcomment.html', {'form':form})




# def addtopic(request):

#     form= TopicForm()

#     if request.method=='POST':
#         form = RoomForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')


#     return render(request, './base/topic.html',{'form':form})

