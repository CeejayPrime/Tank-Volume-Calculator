from django.contrib import admin
from . models import *


class HorizontalCapsuleAdmin(admin.ModelAdmin):
    list_display = ("SideLength", "diameter", "filled")


admin.site.register(HorizontalCylinder)
admin.site.register(VerticalCylinder)
admin.site.register(RectangularTank)
admin.site.register(HorizontalOval)
admin.site.register(VerticalOval)
admin.site.register(HorizontalCapsule, HorizontalCapsuleAdmin)
admin.site.register(VerticalCapsule)
admin.site.register(HorizontalElliptical)
admin.site.register(Torispherical)
admin.site.register(HorizontalDishedEnd)
admin.site.register(Elliptical)
