from django.db import models
from django.db.models import CharField


class HorizontalCylinder(models.Model):
    length = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()


class VerticalCylinder(models.Model):
    height = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()


class RectangularTank(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    filled = models.IntegerField()


class HorizontalOval(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    filled = models.IntegerField()


class VerticalOval(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    filled = models.IntegerField()


class HorizontalCapsule(models.Model):
    SideLength = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()


class VerticalCapsule(models.Model):
    SideLength = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()


class HorizontalElliptical(models.Model):
    SideLength = models.IntegerField()
    InsideDiameter = models.IntegerField()
    OutsideDiameter = models.IntegerField()
    TankClass = models.CharField(max_length=10)
    thickness = models.IntegerField()
    filled = models.IntegerField()


class Torispherical(models.Model):
    SideLength = models.IntegerField()
    InsideDiameter = models.IntegerField()
    OutsideDiameter = models.IntegerField()
    TankClass = models.CharField(max_length=10)
    thickness = models.IntegerField()
    KnuckleRadius = models.IntegerField()
    filled = models.IntegerField()


class HorizontalDishedEnd(models.Model):
    SideLength = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()


class Elliptical(models.Model):
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    filled = models.IntegerField()
