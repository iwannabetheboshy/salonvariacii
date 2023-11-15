from django.contrib import admin
from .models import *


@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    list_display = ("name", "style", "show_number")
    exclude = ['slug']


@admin.register(KitchenOpeningMethod)
class KitchenOpeningMethodAdmin(admin.ModelAdmin):
    pass

@admin.register(KitchenMaterial)
class KitchenMaterialAdmin(admin.ModelAdmin):
    pass

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

@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "message")

@admin.register(LookAt)
class LookAtAdmin(admin.ModelAdmin):
    list_display = ("name", "likes", "show_number")

@admin.register(KitchenFiles)
class KitchenFilesAdmin(admin.ModelAdmin):
    pass

@admin.register(KitchenColors)
class KitchenColorsAdmin(admin.ModelAdmin):
    pass

@admin.register(KitchenFinishing)
class KitchenFinishingAdmin(admin.ModelAdmin):
    pass