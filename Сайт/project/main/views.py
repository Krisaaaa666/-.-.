from django.shortcuts import render
from .models import Post


def index(request):
    '''
    students = Student.objects.all() #строка которая определяет какие именно объекты мне нужно вывести из бд
    data ={
        'title': 'Главная страница'
    }'''
    return render(request,'main/index.html', #data,
                   # {'title':'Главная страница','students': students}  
                 ) #все что в фигурных скобках тоже относится к бд

def about(request):
    return render(request, 'main/about.html')

def postypauchim(request):
    return render(request, 'main/postypauchim.html')

def roditeli(request):
    return render(request, 'main/roditeli.html')

def registr(request):
    return render(request, 'main/registr.html')

def vxod(request):
    return render(request, 'main/vxod.html')

def contakt(request):
    return render(request, 'main/contakt.html')

def ychiteluam(request):
    return render(request, 'main/ychiteluam.html')


