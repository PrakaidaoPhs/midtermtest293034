from django.shortcuts import render,redirect

# Create your views here.
# def home(request):
#     return render(request,'base.html')
from .models import *

def list(request):
    show_emp = Place.objects.all()
    context = {'Placedata':show_emp}
    return render(request,'list.html',context)

def add(request): #เพิ่มข้อมูล
    return render(request,'add.html') #ชื่อไฟล์ที่จะแสดง

def edit(request): #จัดการข้อมูล
    return render(request,'edit.html') #ชื่อไฟล์ที่จะแสดง

def manage(request): #จัดการข้อมูล
    return render(request,'show.html') #ชื่อไฟล์ที่จะแสดง

def delete_place(request,pk):
    return redirect('/manage_place')


