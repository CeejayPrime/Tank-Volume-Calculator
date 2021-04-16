"""tankcalc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gcsv import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calcvol.urls')),
    path('gcsv', views.horizontalCapsuleCsv, name="Gen_Hor_Cap_Csv"),
    # path('calcvol', views.horCap),
    # path('calcvol', views.horCyl),
    # path('calcvol', views.horDish),
    # path('calcvol', views.horEllip),
    # path('calcvol', views.horOval),
    # path('calcvol', views.rect),
    # path('calcvol', views.Torisphere),
    # path('calcvol', views.verCap),
    # path('calcvol', views.verCyl),
    # path('calcvol', views.verOval),
]
