from django.urls import path
from gcsv import views


urlpatterns = [
    path('', views.horizontalCapsuleCsv, name="getcsv")
]