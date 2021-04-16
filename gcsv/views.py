from django.shortcuts import render
from calcvol.views import *
from calcvol.form import *
from calcvol.models import *


def horizontalCapsuleCsv(request, pk):
    g_csv = HorizontalCapsule.objects.get(id=pk)
    # form = HorCapForm(instance=g_csv)
    d = g_csv.diameter
    l = g_csv.SideLength
    r = d/2
    tank_horvol = math.floor((math.pi * r ** 2 * l) / 1000)
    vol = []
    fill_d = []
    for b in range(10, d):
        e = r - b
        theta = 2 * math.acos(e / r)
        seg_area = 1 / 2 * r ** 2 * (theta - math.sin(theta)) * l / 1000

        if b <= r:
            filled_horvol = math.floor(seg_area)
        elif b > r:
            empty_segment = math.floor(tank_horvol - seg_area)
            filled_horvol = tank_horvol - empty_segment

        v_sphere = (1 / 3) * math.pi * b ** 2 * (3 * r - b)

        fill_csv_v = math.floor((v_sphere + filled_horvol)/1000)

        fill_d.append(b)
        vol.append(fill_csv_v)

    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment: filename = Horizontal Capsule.csv'
    writer = csv.writer(response)
    writer.writerow(fill_d)
    writer.writerow(vol)

    return response

