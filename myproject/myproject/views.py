from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("This is home")
    return render(request,'home.html')

def about(request):
    #return HttpResponse("This is about")
    return render(request, 'about.html')