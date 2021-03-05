from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . formula import *
from . form import *


def index(request):
    return render(request, 'Index/index.html')


def horCap(request):
    calc = HorCap.objects.all()
    form = HorCapForm()

    return render(request, 'HorCap/HorCap.html')


def horCyl(request):
    calc = HorCyl.objects.all()
    form = HorCylForm()
    return render(request, 'HorCyl/HorCyl.html')


def horEllip(request):
    calc = HorEllip.objects.all()
    form = HorEllipForm()
    return render(request, 'HorEllip/HorEllip.html')


def horOval(request):
    calc = HorOval.objects.all()
    form = HorOvalForm()
    return render(request, 'HorOval/HorOval.html')


def rects(request):
    calc = Rects.objects.all()
    form = RectsForm()
    return render(request, 'Rect/Rect.html')


def verCap(request):
    calc = VerCap.objects.all()
    form = VerCapForm()
    return render(request, 'VerCap/VerCap.html')


def verCyl(request):
    calc = VerCyl.objects.all()
    form = VerCylForm()
    return render(request, 'VerCyl/VerCyl.html')


def verOval(request):
    calc = VerOval.objects.all()
    form = VerOvalForm()
    return render(request, 'VerOval/VerOval.html')


def horDish(request):
    calc = HorDish.objects.all()
    form = HorDishForm()
    return render(request, 'HorDish/HorDish.html')