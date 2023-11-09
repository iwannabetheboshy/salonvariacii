from django.contrib import admin
from .models import *


@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    list_display = ("name", "style", "material", "openingMethod", "show_number")
    exclude = ['slug']

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


@admin.register(KitchenPhoto)
class KitchenPhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(MainPageCarousel)
class MainPageCarouselAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "show_number")


@admin.register(AboutUsDopBlock)
class AboutUsDopBlocklAdmin(admin.ModelAdmin):
    list_display = ("name", "value")


@admin.register(AboutUs)
class AboutUslAdmin(admin.ModelAdmin):
    pass

@admin.register(ReviewsAndProject)
class ReviewsAndProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "price", "squeare", "review_name", "text", "image")

@admin.register(KitchenFiles)
class KitchenFilesAdmin(admin.ModelAdmin):
    pass

@admin.register(KitchenColors)
class KitchenColorsAdmin(admin.ModelAdmin):
    pass

@admin.register(KitchenFinishing)
class KitchenFinishingAdmin(admin.ModelAdmin):
    pass



