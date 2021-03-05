from django import forms
from django.forms import ModelForm
from .models import *


class HorCapForm(forms.ModelForm):
    class Meta:
        model = HorCap
        fields = '__all__'


class HorCapForm(forms.ModelForm):
    class Meta:
        model = HorCap
        fields = '__all__'


class HorCylForm(forms.ModelForm):
    class Meta:
        model = HorCyl
        fields = '__all__'


class HorDishForm(forms.ModelForm):
    class Meta:
        model = HorDish
        fields = '__all__'


class HorOvalForm(forms.ModelForm):
    class Meta:
        model = HorOval
        fields = '__all__'


class HorEllipForm(forms.ModelForm):
    class Meta:
        model = HorOval
        fields = '__all__'


class RectsForm(forms.ModelForm):
    class Meta:
        model = Rects
        fields = '__all__'


class VerCapForm(forms.ModelForm):
    class Meta:
        model = VerCap
        fields = '__all__'


class VerCylForm(forms.ModelForm):
    class Meta:
        model = VerCyl
        fields = '__all__'


class VerOvalForm(forms.ModelForm):
    class Meta:
        model = VerOval
        fields = '__all__'