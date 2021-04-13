from django.shortcuts import render
from calcvol.views import *


# Create your views here.
def hCap(request):
    tk_dia = horCap(request, horCap.d)
    return tk_dia

