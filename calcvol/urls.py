from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('HorCyl/', views.horCyl, name="HorCyl"),
    path('VerCyl/', views.verCyl, name="VerCyl"),
    path('Rect/', views.rect, name="Rects"),
    path('HorOval/', views.horOval, name="HorOval"),
    path('VerOval/', views.verOval, name="VerOval"),
    path('HorCap/', views.horCap, name="HorCap"),
    path('VerCap/', views.verCap, name="VerCap"),
    path('HorEllip/', views.horEllip, name="HorEllip"),
    path('HorDish/', views.horDish, name="HorDish"),
    path('Ellip', views.Ellip, name="Elliptical"),
    path('Torisphere/', views.Torisphere, name="Torispherical"),
]
