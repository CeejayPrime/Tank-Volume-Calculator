from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('HorCyl/', views.horizontalCylinder, name="HorCyl"),
    path('VerCyl/', views.verticalCylinder, name="VerCyl"),
    path('Rect/', views.rectangularTank, name="Rects"),
    path('HorOval/', views.horizontalOval, name="HorOval"),
    path('VerOval/', views.verticalOval, name="VerOval"),
    path('HorCap/', views.horizontalCapsule, name="HorCap"),
    path('VerCap/', views.verticalCapsule, name="VerCap"),
    path('HorEllip/', views.horizontalElliptical, name="HorEllip"),
    path('HorDish/', views.horizontalDishedEnd, name="HorDish"),
    path('Ellip/', views.elliptical, name="Elliptical"),
    path('Torisphere/', views.torisphere, name="Torispherical"),
]
