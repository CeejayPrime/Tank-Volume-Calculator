from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import HorCyl, HorCap, HorDish, HorOval, HorEllip
from . models import Rects, VerCap, VerCyl, VerOval
from . form import VerCapForm, VerCylForm, VerOvalForm, RectsForm
from . form import HorDishForm, HorCylForm, HorOvalForm, HorEllipForm, HorCapForm
import math


def index(request):
    return render(request, 'Index/index.html')


def horCap(request):
    calcs = HorCap.objects.all()
    form = HorCapForm()
    tank_vol = 0.0
    filled_vol = 0.0
    is_tank_full = ""
    out_put = ""

    if request.method == 'POST':
        form = HorCapForm(request.POST)

        if form.is_valid():
            form.save()
            try:
                a = form.cleaned_data.get("SideLength")
                d = form.cleaned_data.get("diameter")
                f = form.cleaned_data.get("filled")
                r = d/2
                e = r - f

                # Calculation for horizontal cylinder
                tank_horvol = math.floor((math.pi * r ** 2 * a) / 1000)
                theta = 2 * math.acos(e / r)
                seg_area = 1 / 2 * r ** 2 * (theta - math.sin(theta)) * a / 1000

                if f <= r:
                    filled_horvol = math.floor(seg_area)
                    # print(filled_vol)
                elif f > r:
                    empty_segment = math.floor(tank_horvol - seg_area)
                    filled_horvol = tank_horvol - empty_segment
                # Calculation for horizontal cylinder

                # Calculation for spherical section
                tank_vol = math.pi * r**2 * ((4/3) * r + a)
                tank_vol = math.floor(tank_vol/1000)

                v_sphere = (1/3) * math.pi * f**2 * (3 * r - f)
                v_sphere = math.floor(v_sphere/1000)
                # Calculation for spherical section

                # Total Volume
                filled_vol = v_sphere + filled_horvol

                if filled_vol == tank_vol:
                    is_tank_full = "Tank is full"
                elif filled_vol > tank_vol:
                    is_tank_full = "Null"
                else:
                    is_tank_full = ""

            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calcs':calcs,
               'tank_vol': tank_vol, 'filled_vol': filled_vol,
               'is_tank_full': is_tank_full, 'out_put': out_put}

    return render(request, 'HorCap/HorCap.html', context)


def horCyl(request):
    calcs = HorCyl.objects.all()
    form = HorCylForm()
    tank_vol = 0.0
    filled_vol = 0.0
    is_tank_full = ""
    out_put = ""

    if request.method == 'POST':
        form = HorCylForm(request.POST)

        if form.is_valid():
            form.save()
            try:
                l = form.cleaned_data.get("length")
                d = form.cleaned_data.get("diameter")
                f = form.cleaned_data.get("filled")
                r = d/2
                e = r - f

                tank_vol = math.floor((math.pi * r ** 2 * l) / 1000)
                theta = 2 * math.acos(e/r)
                seg_area = 1/2 * r**2 * (theta - math.sin(theta)) * l/1000

                if f <= r:
                    filled_vol = math.floor(seg_area)
                    print(filled_vol)
                elif f > r:
                    empty_segment = math.floor(tank_vol - seg_area)
                    filled_vol = tank_vol - empty_segment

                if filled_vol == tank_vol:
                    is_tank_full = "Tank is full"
                elif filled_vol > tank_vol:
                    is_tank_full = "Null"
                else:
                    is_tank_full = ""
            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calcs': calcs,
               'tank_vol': tank_vol,
               'filled_vol': filled_vol, 'is_tank_full': is_tank_full,
               'out_put': out_put}
    return render(request, 'HorCyl/HorCyl.html', context)


def horEllip(request):
    calc = HorEllip.objects.all()
    form = HorEllipForm()
    tank_vol = 0.0
    filled_vol = 0.0
    is_tank_full = ""
    out_put = ""

    if request.method == 'POST':
        form = HorEllipForm(request.POST)

        if form.is_valid():
            form.save()

            a = form.cleaned_data.get("SideLength")
            d = form.cleaned_data.get("diameter")
            f = form.cleaned_data.get("filled")
            r = d/2



    context = {'form': form, 'calc': calc}
    return render(request, 'HorEllip/HorEllip.html', context)


def horOval(request):
    calcs = HorOval.objects.all()
    form = HorOvalForm()
    tank_vol = 0.0
    filled_vol = 0.0
    is_tank_full = ""
    out_put = ""

    if request.method == 'POST':
        form = HorOvalForm(request.POST)

        if form.is_valid():
            form.save()

            try:
                h = form.cleaned_data.get("height")
                w = form.cleaned_data.get("width")
                l = form.cleaned_data.get("length")
                f = form.cleaned_data.get("filled")
                a = w - h
                r = h/2
                e = r - f

                tank_vol = (math.pi * r ** 2 + 2 * r * a) * l
                tank_vol = math.floor(tank_vol/1000)

                # Calculation for horizontal cylinder
                tank_horvol = math.floor((math.pi * r ** 2 * l) / 1000)
                theta = 2 * math.acos(e / r)
                seg_area = 1 / 2 * r ** 2 * (theta - math.sin(theta)) * l / 1000

                if f <= r:
                    filled_horvol = math.floor(seg_area)
                    # print(filled_vol)
                elif f > r:
                    empty_segment = math.floor(tank_horvol - seg_area)
                    filled_horvol = tank_horvol - empty_segment
                # Calculation for horizontal cylinder

                # Calculation for Rectangle
                filled_rectvol = (l * f * a) / 1000
                # Calculation for Rectangle

                filled_vol = filled_horvol + filled_rectvol
                # filled_vol = math.floor(filled_vol/1000)

                if filled_vol == tank_vol:
                    is_tank_full = "Tank is full"
                elif filled_vol > tank_vol:
                    is_tank_full = "Null"
                else:
                    is_tank_full = ""

            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calcs': calcs, 'tank_vol': tank_vol,
               'filled_vol': filled_vol, 'is_tank_full': is_tank_full,
               'out_put': out_put}
    return render(request, 'HorOval/HorOval.html', context)


def rect(request):
    calc = Rects.objects.all()
    form = RectsForm()
    tank_vol = 0.0
    filled_vol = 0.0
    is_tank_full = ""

    if request.method == 'POST':
        form = RectsForm(request.POST)

        if form.is_valid():
            form.save()

            h = form.cleaned_data.get("height")
            ln = form.cleaned_data.get("length")
            w = form.cleaned_data.get("width")
            f = form.cleaned_data.get("filled")

            tank_vol = (ln * h * w)/1000
            filled_vol = (ln * f * w)/1000

            if filled_vol == tank_vol:
                is_tank_full = "tank is full"
            elif filled_vol > tank_vol:
                is_tank_full = "null"
                filled_vol = None
            else:
                is_tank_full = ""

    context = {'form': form, 'calcs': calc, 'tank_vol': tank_vol, 'filled_vol': filled_vol, 'is_tank_full': is_tank_full}
    return render(request, 'Rect/Rect.html', context)


def verCap(request):
    calc = VerCap.objects.all()
    form = VerCapForm()
    tank_vol = 0.0
    filled_vol = 0.0
    is_tank_full = ""
    out_put = ""

    if request.method == 'POST':
        form = VerCapForm(request.POST)

        if form.is_valid():
            form.save()

            try:
                a = form.cleaned_data.get("SideLength")
                d = form.cleaned_data.get("diameter")
                f = form.cleaned_data.get("filled")
                r = d/2
                h = a + d
                f_h = h - f

                tank_vol = math.pi * r**2 * ((4/3) * r + a)
                tank_vol = math.floor(tank_vol/1000)
                v_sphere = ((1 / 3) * math.pi * f ** 2 * (3 * r - f))/1000
                vs_sphere = ((1 / 3) * math.pi * f_h ** 2 * (3 * r - f_h)) / 1000

                if f <= r:
                    filled_vol = v_sphere
                    filled_vol = math.floor(filled_vol/1000)

                elif r < f <= (r + a):
                    filled_vol = (0.667 * math.pi * r ** 3) + (math.pi * r ** 2 * (f - d/2))
                    filled_vol = math.floor(filled_vol / 1000)

                elif f > (r + a) < h:
                    filled_vol = math.floor(tank_vol - vs_sphere)

                if filled_vol == tank_vol:
                    is_tank_full = "Tank is full"
                elif filled_vol > tank_vol:
                    is_tank_full = "Null"
                else:
                    is_tank_full = ""

            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calcs': calc, 'tank_vol': tank_vol,
               'filled_vol': filled_vol, 'is_tank_full': is_tank_full,
               'out_put': out_put}
    return render(request, 'VerCap/VerCap.html', context)


def verCyl(request):
    calc = VerCyl.objects.all()
    form = VerCylForm()
    # the formula is pi * r^2 * h
    tank_volume = 0.0
    filled_vol = 0.0
    is_tank_full = ""
    out_put = ""

    if request.method == 'POST':
        form = VerCylForm(request.POST)

        if form.is_valid():
            form.save()
            try:
                h = form.cleaned_data.get("height")
                d = form.cleaned_data.get("diameter")
                r = d/2
                f = form.cleaned_data.get("filled")
                tank_volume = (3.14 * r**2 * h)/1000
                filled_vol = (3.14 * r**2 * f)/1000

                if filled_vol == tank_volume:
                    is_tank_full = "Tank is full"
                elif filled_vol > tank_volume:
                    is_tank_full = None
                    filled_vol = None
                else:
                    is_tank_full = ""
            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calcs': calc,
               'tank_volume': tank_volume,
               'filled_vol': filled_vol, 'is_tank_full': is_tank_full,
               'out_put': out_put}
    return render(request, 'VerCyl/VerCyl.html', context)


def verOval(request):
    calc = VerOval.objects.all()
    form = VerOvalForm()
    tank_vol = 0.0
    filled_vol = 0.0
    is_tank_full = ""
    out_put = ""

    if request.method == 'POST':
        form = VerOvalForm(request.POST)

        if form.is_valid():
            form.save()

            try:

                h = form.cleaned_data.get("height")
                w = form.cleaned_data.get("width")
                l = form.cleaned_data.get("length")
                f = form.cleaned_data.get("filled")
                f_h = h - f
                r = w/2
                a = h - w
                e = r - f
                j = r - f_h
                g = r + a
                i = h - r

                tank_vol = (math.pi * r**2 + 2 * r * a) * l
                tank_vol = math.floor(tank_vol/1000)

                if f < r:
                    theta = 2 * math.acos(e / r)
                    seg_area = 0.5 * r ** 2 * (theta - math.sin(theta)) * l / 1000
                    filled_vol = math.floor(seg_area)

                elif r < f < g:
                    filled_vol = (0.5 * math.pi * r**2 * l) + ((f - r) * l * w)
                    filled_vol = math.floor(filled_vol/1000)

                elif f > (r + a) < h:
                    theta = 2 * math.acos(j / r)
                    seg_area = 0.5 * r ** 2 * (theta - math.sin(theta)) * l / 1000
                    filled_vol = tank_vol - seg_area
                    filled_vol = math.floor(filled_vol)

                if filled_vol == tank_vol:
                    is_tank_full = "Tank is full"
                elif filled_vol > tank_vol:
                    is_tank_full = "Null"
                else:
                    is_tank_full = ""

            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calcs': calc,
               'tank_vol': tank_vol, 'filled_vol': filled_vol,
               'out_put': out_put, 'is_tank_full': is_tank_full}
    return render(request, 'VerOval/VerOval.html', context)


def horDish(request):
    calc = HorDish.objects.all()
    form = HorDishForm()
    tank_vol = 0.0
    filled_vol = 0.0
    is_tank_full = ""

    if request.method == 'POST':
        form = HorDishForm(request.POST)

        if form.is_valid():
            form.save()
            # try:
            #     sl = form.cleaned_data.get("SideLength")
            #     d = form.cleaned_data.get("diameter")
            #     f = form.cleaned_data.get("filled")
            #     r = d/2



    context = {'form': form, 'calcs': calc}
    return render(request, 'HorDish/HorDish.html', context)