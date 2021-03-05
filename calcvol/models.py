from django.db import models
from django.db.models import CharField


# class Calculate(models.Model):
#     length = models.IntegerField()
#     width = models.IntegerField()
#     height = models.IntegerField()
#     diameter = models.IntegerField()
#     SideLength = models.IntegerField()
#     filled = models.IntegerField()


class HorCyl(models.Model):
    length = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()


class VerCyl(models.Model):
    height = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()


class Rects(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    filled = models.IntegerField()


class HorOval(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    filled = models.IntegerField()


class VerOval(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    filled = models.IntegerField()


class HorCap(models.Model):
    SideLength = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()


class VerCap(models.Model):
    SideLength = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()


class HorEllip(models.Model):
    SideLength = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()


class HorDish(models.Model):
    SideLength = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()
