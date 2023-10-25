from django.contrib import admin
from .models import *


@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    list_display = ("name", "style", "material", "openingMethod")

    class Media:
        js = ("main/js/custom_admin.js",)


@admin.register(KitchenOpeningMethod)
class KitchenOpeningMethodAdmin(admin.ModelAdmin):
    list_display = ("name", "kitchen_styles")


@admin.register(KitchenMaterial)
class KitchenMaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "kitchen_styles")


@admin.register(KitchenStyle)
class KitchenStyleAdmin(admin.ModelAdmin):
    pass




