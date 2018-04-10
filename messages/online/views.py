from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
# Create your views here.

def index(request):
    print(models.get_messages())
    context = {'messages':models.get_messages()}
    return render(request,'online/index.html',context)

def create(request):
    return render(request,'online/create.html')

def save(request):
    name = request.GET.get('username','')
    age = request.GET.get('age','')
    tel = request.GET.get('tel','')
    print(name,age,tel)
    models.save_messages(name,age,tel)
    return HttpResponseRedirect('/online/')
