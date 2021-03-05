from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *


def index(request):
    return render(request)
