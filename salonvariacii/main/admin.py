from django.contrib import admin
from .models import *


@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    list_display=('name', 'style', 'get_material', 'get_openingMethod', 'get_finishing', 'show_number')
    filter_horizontal = ('material','openingMethod', 'finishing','files', 'images') 
    fieldsets = (
      ('Основные сведения', {
          'fields': ('name', 'desc', 'style', 'material', 'openingMethod', 'finishing', 'show_number')
      }),
      ('Медиа-файлы кухни', {
          'fields': ('mainImage', 'catalogVideo', 'kitchenCardVideo')
      }),
      ('Карусель фотографий в карточке кухни', {
          'fields': ('images',)
      }),
      ('Сопроводительные PDF-файлы для кухни', {
          'fields': ('files',)
      }),
   )
    exclude = ['slug', 'catalogVideoUrl']

    



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
    list_display = ("name", "show_number")


@admin.register(AboutUsDopBlock)
class AboutUsDopBlocklAdmin(admin.ModelAdmin):
    list_display = ("value", "name", "show_number")


@admin.register(AboutUs)
class AboutUslAdmin(admin.ModelAdmin):
    pass

@admin.register(ReviewsAndProject)
class ReviewsAndProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "price", "squeare", "review_name", "text")

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
    list_display = ("name", "get_colors")
    filter_horizontal = ('colors',) 