from django.db import models
from django.db.models import CharField


class HorCyl(models.Model):
    length = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()

    def __str__(self):
        return self.filled


class VerCyl(models.Model):
    height = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()

    def __str__(self):
        return self.filled


class Rects(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    filled = models.IntegerField()

    def __str__(self):
        return self.filled


class HorOval(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    filled = models.IntegerField()

    def __str__(self):
        return self.filled


class VerOval(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    filled = models.IntegerField()

    def __str__(self):
        return self.filled


class HorCap(models.Model):
    SideLength = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()

    def __str__(self):
        return self.filled


class VerCap(models.Model):
    SideLength = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()

    def __str__(self):
        return self.filled


class HorEllip(models.Model):
    SideLength = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()

    def __str__(self):
        return self.filled


class HorDish(models.Model):
    SideLength = models.IntegerField()
    diameter = models.IntegerField()
    filled = models.IntegerField()

    def __str__(self):
        return self.filled
