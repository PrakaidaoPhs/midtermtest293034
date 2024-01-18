from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request,'base.html')
from .models import *

def list(request):
    show_emp = Place.objects.all()
    context = {'Placedata':show_emp}
    return render(request,'list.html',context)