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
    if request.method == "POST":
        table = Place()
        table.name = request.POST['name']
        table.location = request.POST['location']
        table.description = request.POST['description']
        table.opening_hours = request.POST['opening_hours']
        table.closing_hours = request.POST['closing_hours']
        table.image = request.FILES['image']
        table.save()
        return redirect('/manage')
    return render(request,'add.html') #ชื่อไฟล์ที่จะแสดง

def edit(request,pk): #จัดการข้อมูล
    table = Place.objects.get(place_id=pk)
    context = {"place_data" : table}
    if request.method == "POST":
        table.name = request.POST['name']
        table.location = request.POST['location']
        table.description = request.POST['description']
        table.opening_hours = request.POST['opening_hours']
        table.closing_hours = request.POST['closing_hours']
        table.image = request.FILES['image']
        table.save()
        return redirect('/manage')
    return render(request,'edit.html') #ชื่อไฟล์ที่จะแสดง

def delete_place(request,pk):
    table = Place.objects.get(place_id=pk)
    table.delete()
    return redirect('/manage')


