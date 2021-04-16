from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HorizontalCylinder, HorizontalCapsule, HorizontalDishedEnd, HorizontalOval, HorizontalElliptical
from .models import RectangularTank, VerticalCapsule, VerticalCylinder, VerticalOval, Torispherical, Elliptical
from .form import VerCapForm, VerCylForm, VerOvalForm, RectsForm
from .form import HorDishForm, HorCylForm, HorOvalForm, HorEllipForm
from .form import HorCapForm, EllipticalForm, TorisphericalForm
import math
import csv

filled_depth = []
filled_volume = []


def index(request):
    return render(request, 'Index/index.html')


def horizontalCapsule(request):
    calcs = HorizontalCapsule.objects.all()
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
                r = d / 2
                e = r - f

                # Calculation for horizontal cylinder
                tank_horvol = math.floor((math.pi * r ** 2 * a) / 1000)
                theta = 2 * math.acos(e / r)
                seg_area = 1 / 2 * r ** 2 * (theta - math.sin(theta)) * a / 1000

                if f <= r:
                    filled_horvol = math.floor(seg_area)

                elif f > r:
                    empty_segment = math.floor(tank_horvol - seg_area)
                    filled_horvol = tank_horvol - empty_segment
                # Calculation for horizontal cylinder

                # Calculation for spherical section
                tank_vol = math.pi * r ** 2 * ((4 / 3) * r + a)
                tank_vol = math.floor(tank_vol / 1000)

                v_sphere = (1 / 3) * math.pi * f ** 2 * (3 * r - f)
                v_sphere = math.floor(v_sphere / 1000)
                # Calculation for spherical section

                # Total Volume
                filled_vol = v_sphere + filled_horvol

                if filled_vol == tank_vol:
                    is_tank_full = "Tank is full"

            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calcs': calcs,
               'tank_vol': tank_vol, 'filled_vol': filled_vol,
               'is_tank_full': is_tank_full, 'out_put': out_put}

    return render(request, 'HorCap/HorCap.html', context)


def horizontalCylinder(request):
    calcs = HorizontalCylinder.objects.all()
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
                r = d / 2
                e = r - f

                tank_vol = math.floor((math.pi * r ** 2 * l) / 1000)
                theta = 2 * math.acos(e / r)
                seg_area = 1 / 2 * r ** 2 * (theta - math.sin(theta)) * l / 1000

                if f <= r:
                    filled_vol = math.floor(seg_area)
                    print(filled_vol)
                elif f > r:
                    empty_segment = math.floor(tank_vol - seg_area)
                    filled_vol = tank_vol - empty_segment

                if filled_vol == tank_vol:
                    is_tank_full = "Tank is full"

            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calcs': calcs,
               'tank_vol': tank_vol,
               'filled_vol': filled_vol, 'is_tank_full': is_tank_full,
               'out_put': out_put}
    return render(request, 'HorCyl/HorCyl.html', context)


def horizontalElliptical(request):
    calc = HorizontalElliptical.objects.all()
    form = HorEllipForm()
    tank_vol = 0.0
    filled_vol = 0.0
    is_tank_full = ""
    out_put = ""

    if request.method == 'POST':
        form = HorEllipForm(request.POST)

        if form.is_valid():
            form.save()

            try:
                l = form.cleaned_data.get("SideLength")
                Di = form.cleaned_data.get("InsideDiameter")
                Do = form.cleaned_data.get("OutsideDiameter")
                Tk = form.cleaned_data.get("TankClass")
                t = form.cleaned_data.get("thickness")
                f = form.cleaned_data.get("filled")
                r = Di / 2
                e = r - f

                if Tk == 'ASME':
                    c = 1/2
                elif Tk == 'DIN 28011':
                    c = 0.49951 + 0.10462 * (t / Do) + 2.3227 * (t / Do)**2

                tank_vol = math.floor((math.pi * r ** 2 * l) / 1000)
                theta = 2 * math.acos(e / r)
                seg_area = 1 / 2 * r ** 2 * (theta - math.sin(theta)) * l / 1000
                Vf = Di**3 * c * math.pi / 12 * (3 * (f / Di)**2 - 2 * (f / Di)**3)

                if f <= r:
                    filled_vol = math.floor(seg_area)
                    filled_vol = filled_vol + (Vf * 2)
                elif f > r:
                    empty_segment = math.floor(tank_vol - seg_area)
                    filled_vol = tank_vol - empty_segment
                    filled_vol = filled_vol + (Vf * 2)

                if filled_vol == tank_vol:
                    is_tank_full = "Tank is full"

            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calc': calc, 'tank_vol': tank_vol,
               'filled_vol': filled_vol, 'is_tank_full': is_tank_full, 'out_put': out_put}

    return render(request, 'HorEllip/HorEllip.html', context)


def horizontalOval(request):
    calcs = HorizontalOval.objects.all()
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
                r = h / 2
                e = r - f

                tank_vol = (math.pi * r ** 2 + 2 * r * a) * l
                tank_vol = math.floor(tank_vol / 1000)

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

            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calcs': calcs, 'tank_vol': tank_vol,
               'filled_vol': filled_vol, 'is_tank_full': is_tank_full,
               'out_put': out_put}
    return render(request, 'HorOval/HorOval.html', context)


def rectangularTank(request):
    calc = RectangularTank.objects.all()
    form = RectsForm()
    tank_vol = 0.0
    filled_vol = 0.0
    is_tank_full = ""
    out_put = ""

    if request.method == 'POST':
        form = RectsForm(request.POST)

        if form.is_valid():
            form.save()

            try:
                h = form.cleaned_data.get("height")
                ln = form.cleaned_data.get("length")
                w = form.cleaned_data.get("width")
                f = form.cleaned_data.get("filled")

                tank_vol = (ln * h * w) / 1000
                filled_vol = (ln * f * w) / 1000

                if filled_vol == tank_vol:
                    is_tank_full = "tank is full"
                elif filled_vol > tank_vol:
                    is_tank_full = "null"
                    filled_vol = None
                else:
                    is_tank_full = ""
            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calcs': calc, 'tank_vol': tank_vol, 'filled_vol': filled_vol,
               'is_tank_full': is_tank_full, 'out_put': out_put}

    return render(request, 'Rect/Rect.html', context)


def verticalCapsule(request):
    calc = VerticalCapsule.objects.all()
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
                r = d / 2
                h = a + d
                f_h = h - f

                tank_vol = math.pi * r ** 2 * ((4 / 3) * r + a)
                tank_vol = math.floor(tank_vol / 1000)
                v_sphere = ((1 / 3) * math.pi * f ** 2 * (3 * r - f)) / 1000
                vs_sphere = ((1 / 3) * math.pi * f_h ** 2 * (3 * r - f_h)) / 1000

                if f <= r:
                    filled_vol = v_sphere
                    filled_vol = math.floor(filled_vol / 1000)

                elif r < f <= (r + a):
                    filled_vol = (0.667 * math.pi * r ** 3) + (math.pi * r ** 2 * (f - d / 2))
                    filled_vol = math.floor(filled_vol / 1000)

                elif f > (r + a) < h:
                    filled_vol = math.floor(tank_vol - vs_sphere)

                if filled_vol == tank_vol:
                    is_tank_full = "Tank is full"

            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calcs': calc, 'tank_vol': tank_vol,
               'filled_vol': filled_vol, 'is_tank_full': is_tank_full,
               'out_put': out_put}
    return render(request, 'VerCap/VerCap.html', context)


def verticalCylinder(request):
    calc = VerticalCylinder.objects.all()
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
                r = d / 2
                f = form.cleaned_data.get("filled")
                tank_volume = (3.14 * r ** 2 * h) / 1000
                filled_vol = (3.14 * r ** 2 * f) / 1000

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


def verticalOval(request):
    calc = VerticalOval.objects.all()
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
                r = w / 2
                a = h - w
                e = r - f
                j = r - f_h
                g = r + a
                i = h - r

                tank_vol = (math.pi * r ** 2 + 2 * r * a) * l
                tank_vol = math.floor(tank_vol / 1000)

                if f < r:
                    theta = 2 * math.acos(e / r)
                    seg_area = 0.5 * r ** 2 * (theta - math.sin(theta)) * l / 1000
                    filled_vol = math.floor(seg_area)

                elif r < f < g:
                    filled_vol = (0.5 * math.pi * r ** 2 * l) + ((f - r) * l * w)
                    filled_vol = math.floor(filled_vol / 1000)

                elif f > (r + a) < h:
                    theta = 2 * math.acos(j / r)
                    seg_area = 0.5 * r ** 2 * (theta - math.sin(theta)) * l / 1000
                    filled_vol = tank_vol - seg_area
                    filled_vol = math.floor(filled_vol)

                if filled_vol == tank_vol:
                    is_tank_full = "Tank is full"

            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calcs': calc,
               'tank_vol': tank_vol, 'filled_vol': filled_vol,
               'out_put': out_put, 'is_tank_full': is_tank_full}
    return render(request, 'VerOval/VerOval.html', context)


def horizontalDishedEnd(request):
    calc = HorizontalDishedEnd.objects.all()
    form = HorDishForm()
    tank_vol = 0.0
    filled_vol = 0.0
    is_tank_full = ""

    if request.method == 'POST':
        form = HorDishForm(request.POST)

        if form.is_valid():
            form.save()
            try:
                sl = form.cleaned_data.get("SideLength")
                d = form.cleaned_data.get("diameter")
                f = form.cleaned_data.get("filled")
                r = d / 2
                e = r - f

                tank_vol = math.floor((math.pi * r ** 2 * sl) / 1000)
                theta = 2 * math.acos(e / r)
                seg_area = 1 / 2 * r ** 2 * (theta - math.sin(theta)) * sl / 1000

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

    context = {'form': form, 'calc': calc}
    return render(request, 'HorDish/HorDish.html', context)


def elliptical(request):
    calc = Elliptical.objects.all()
    form = EllipticalForm()
    tank_vol = 0.0
    filled_vol = 0.0
    is_tank_full = ""
    out_put = ""

    if request.method == 'POST':
        form = EllipticalForm(request.POST)

        if form.is_valid():
            form.save()
            try:
                l = form.cleaned_data.get("length")
                w = form.cleaned_data.get("width")
                h = form.cleaned_data.get("height")
                f = form.cleaned_data.get("filled")

                tank_vol = math.pi * w * l * h/4
                tank_vol = math.floor(tank_vol/1000)
                filled_vol = l * h * w / 4 * (math.acos(1 - (2 * f / h)) - (1 - (2 * f / h)) * math.sqrt(4 * f / h - 4 *
                                                                                                         f**2 / h**2))
                filled_vol = math.floor(filled_vol/1000)

            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calc': calc, 'tank_vol': tank_vol,
               'filled_vol': filled_vol, 'is_tank_full': is_tank_full, 'out_put': out_put}
    return render(request, 'Elliptical/Elliptical.html', context, h)


def torisphere(request):
    calc = Torispherical.objects.all()
    form = TorisphericalForm()
    tank_vol = 0.0
    filled_vol = 0.0
    is_tank_full = ""
    out_put = ""

    if request.method == 'POST':
        form = TorisphericalForm(request.POST)

        if form.is_valid():
            form.save()

            try:
                l = form.cleaned_data.get("SideLength")
                TK = form.cleaned_data.get("TankClass")
                t = form.cleaned_data.get("thickness")
                f = form.cleaned_data.get("filled")
                Do = form.cleaned_data.get("OutsideDiameter")
                Di = form.cleaned_data.get("InsideDiameter")
                Kr = form.cleaned_data.get("KnuckleRadius")
                r = Di / 2
                e = r - f

                if TK == 'ASME':
                    c = 0.30939 + 1.7197 * (Kr - 0.06 * Do) / Di - 0.16116 * t / Do + 0.98997 * (t / Do) ** 2
                elif TK == 'DIN 28011':
                    c = 0.37802 + 0.05073 * t / Do + 1.3762 * (t / Do) ** 2

                Vf = Di ** 3 * c * math.pi / 12 * (3 * (f / Di) ** 2 - 2 * (f / Di) ** 3)

                tank_vol = math.floor((math.pi * r ** 2 * l) / 1000)
                theta = 2 * math.acos(e / r)
                seg_area = 1 / 2 * r ** 2 * (theta - math.sin(theta)) * l / 1000

                if f <= r:
                    filled_vol = math.floor(seg_area)
                    filled_vol = filled_vol + (Vf * 2)
                elif f > r:
                    empty_segment = math.floor(tank_vol - seg_area)
                    filled_vol = tank_vol - empty_segment
                    filled_vol = filled_vol + (Vf * 2)

                if filled_vol == tank_vol:
                    is_tank_full = "Tank is full"
                elif filled_vol > tank_vol:
                    is_tank_full = "Null"
                else:
                    is_tank_full = ""

            except ValueError:
                out_put = "Invalid Input"

    context = {'form': form, 'calc': calc, 'tank_vol': tank_vol,
               'filled_vol': filled_vol, 'is_tank_full': is_tank_full, 'out_put': out_put}
    return render(request, 'Torispherical/Torispherical.html', context)


def generate_csv(request):
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename = chart.csv'

    writer = csv.writer(response)
    writer.writerow([])

    return response


