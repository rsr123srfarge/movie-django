from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Movie


def movies(request):
    
    data = Movie.objects.all()
    return render(request,'movies/movies.html',{'movies':data}) 



def HomePage(request):
    return HttpResponse("Welcome to HomePage")

def index(request):
    datain=Movie()
    
    datain.name='24'
    datain.year=2012
    datain.save()
    return render(request,'movies/index.html')
    