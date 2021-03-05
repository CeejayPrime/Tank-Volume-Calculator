from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('HorCyl/', views.horCyl, name="HorCyl"),
    path('VerCyl/', views.verCyl, name="VerCyl"),
    path('Rect/', views.Rects, name="Rect"),
    path('HorOval/', views.horOval, name="HorOval"),
    path('VerOval/', views.verOval, name="VerOval"),
    path('HorCap/', views.horCap, name="HorCap"),
    path('VerCap/', views.verCap, name="VerCap"),
    path('HorEllip/', views.horEllip, name="HorEllip"),
    path('HorDish/', views.horDish, name="HorDish"),
]