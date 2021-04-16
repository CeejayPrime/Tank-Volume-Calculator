from django import forms
from django.forms import ModelForm
from .models import *


class HorCapForm(forms.ModelForm):
    class Meta:
        model = HorizontalCapsule
        fields = '__all__'

#
# class HorCapForm(forms.ModelForm):
#     class Meta:
#         model = HorCap
#         fields = '__all__'


class HorCylForm(forms.ModelForm):
    class Meta:
        model = HorizontalCylinder
        fields = '__all__'


class HorDishForm(forms.ModelForm):
    class Meta:
        model = HorizontalDishedEnd
        fields = '__all__'


class HorOvalForm(forms.ModelForm):
    class Meta:
        model = HorizontalOval
        fields = '__all__'


class HorEllipForm(forms.ModelForm):
    class Meta:
        model = HorizontalElliptical
        fields = '__all__'


class RectsForm(forms.ModelForm):
    class Meta:
        model = RectangularTank
        fields = '__all__'


class VerCapForm(forms.ModelForm):
    class Meta:
        model = VerticalCapsule
        fields = '__all__'


class VerCylForm(forms.ModelForm):
    class Meta:
        model = VerticalCylinder
        fields = '__all__'


class VerOvalForm(forms.ModelForm):
    class Meta:
        model = VerticalOval
        fields = '__all__'


class EllipticalForm(forms.ModelForm):
    class Meta:
        model = Elliptical
        fields = '__all__'


class TorisphericalForm(forms.ModelForm):
    class Meta:
        model = Torispherical
        fields = '__all__'


