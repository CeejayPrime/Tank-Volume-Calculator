from django.urls import path
from . import views


urlpatterns = [
    path("/", views.index, name="index"),
    path('HorCyl/', views.HorCyl, name="HorCyl"),
    path('VerCyl/', views.VerCyl, name="VerCyl"),
    path('Rect/', views.Rect, name="Rect"),
    path('HorOval/', views.HorOval, name="HorOval"),
    path('VerOval/', views.VerOval, name="VerOval"),
    path('HorCap/', views.HorCap, name="HorCap"),
    path('VerCap/', views.VerCap, name="VerCap"),
    path('HorEllip/', views.HorEllip, name="HorEllip"),
    path('HorDish/', views.HorDish, name="HorDish"),
]