from django.shortcuts import render

# Create your views here.

def listview(request):

    return render(request, 'list.html')