from django.contrib import admin
from .models import *
from django import forms
from django.utils.html import format_html

@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    list_display=('name', 'style', 'get_material', 'get_openingMethod', 'get_finishing', 'show_number')
    filter_horizontal = ('material','openingMethod', 'finishing','files', 'images') 
    fieldsets = (
      ('Основные сведения', {
          'fields': ('name', 'desc', 'style', 'material', 'openingMethod', 'finishing', 'show_number', 'hide')
      }),
      ('Приемущества кухни в карточке', {
          'fields': ('advantages1', 'advantages2', 'advantages3')
      }),
      ('Медиа-файлы кухни', {
          'fields': ('mainImage', 'catalogVideo', 'kitchenCardVideoPhotoChoices', 'kitchenCardVideo', 'kitchenCardPhoto')
      }),
      ('Карусель фотографий в карточке кухни', {
          'fields': ('images',)
      }),
      ('Сопроводительные PDF-файлы для кухни', {
          'fields': ('files',)
      }),
   )
    exclude = ['slug']

    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={'size':'60'})},
    }

    class Media:
        js = ("main/js/custom_admin.js",)


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
    list_display = ("image_title",)
    
    def image_title(self, object):
        return str(object.image).split('/')[-1]


@admin.register(MainPageCarousel)
class MainPageCarouselAdmin(admin.ModelAdmin):
    list_display = ("name", "show_number")
    exclude = ['slug']



@admin.register(AboutUs)
class AboutUslAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "image")


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "message")


@admin.register(LookAt)
class LookAtAdmin(admin.ModelAdmin):
    list_display = ("name", "likes", "show_number", 'hide')


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


@admin.register(Politic)
class PoliticAdmin(admin.ModelAdmin):
    pass


@admin.register(FeedbackBlock)
class FeedbackBlockAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "image")
    fieldsets = (
      ('Основные надписи', {
          'fields': ('title', 'fontsize', 'titleTwo', 'fontsizeTiteTwo', 'text', 'fontsizeText', 'image', 'fontsizeBtn')
      }),
      ('Надписи в форме', {
          'fields': ('inputName', 'inputPhone', 'inputMassage', 'fontsizeInput')
      }),
   )


@admin.register(LookAtTitle)
class LookAtTitleAdmin(admin.ModelAdmin):
    list_display = ("titleOne", "titleTwo")



@admin.register(AdvantagesTitle)
class AdvantagesTitleAdmin(admin.ModelAdmin):
    list_display = ("title", "fontsizeH", "fontsizeTextH", "fontsizeText")


@admin.register(AdvantagesBlocks)
class AdvantagesBlocksAdmin(admin.ModelAdmin):
    list_display = ("name", "text", "show_number")

    def message_user(self, request, message, level='info', extra_tags='', fail_silently=False):
        """
        Override the default message_user method to customize success messages.
        """

        print(message)
        if message == 'приемущества "<a href="/admin/main/advantagesblocks/None/change/">AdvantagesBlocks object (None)</a>" был успешно добавлен.':

            custom_message = 'Превышено максимальное количество записей (4).'
            self.message_user(request, format_html(custom_message), level='error')
        else:
            super().message_user(request, message, level, extra_tags, fail_silently)   

@admin.register(WatchVideoMain)
class WatchVideoMainAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={'size':'60'})},
    }
    
    
@admin.register(CatalogTitle)
class CatalogTitleAdmin(admin.ModelAdmin):
    list_display = ("name", "text")
    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={'size':'60'})},
    }

    fieldsets = (
      ('Основные надписи', {
          'fields': ('name', 'fontsizeH', 'text', 'fontsizeText', 'fontsizeFilter', 'fontsizeKitchen')
      }),
      ('Надписи, когда результаты фильтрации не найдены', {
          'fields': ('name404', 'fontsize404', 'name404Gray', 'fontsize404Gray')
      }),
   )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("name", "image")

@admin.register(KitchenCardText)
class KitchenCardTextAdmin(admin.ModelAdmin):
    list_display = ("fontsizeH", "fontsizeText", "fontsizeFile")
    fieldsets = (
      ('Основаня информация', {
          'fields': ('fontsizeH', 'fontsizeText', 'fontsizeFile', 'fontsizeAdvanteges', 'fontsizeBtn')
      }),
      ('Цвета и материалы', {
          'fields': ('colorMaterialName', 'fontsizeColorMaterial', 'fontsizeNameMaterial', 'fontsizeNameColor')
      }),
      ('Сертификаты качества', {
          'fields': ('certificateName', 'fontsizeCertificateH', 'fontsizeCertificateName')
      }),
   )


@admin.register(CatalogMain)
class CatalogMainAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={'size':'60'})},
    }

@admin.register(CatalogMainBlock)
class CatalogMainBlockAdmin(admin.ModelAdmin):
    list_display = ("title", "titleTwo")


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ("titleCatalog", "titleLookAt", "titleMore", "titleCatalog", "fontsize")


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("titleCatalog", "titleLookAt", "titleMore", "titleCatalog", "fontsize")


@admin.register(MoreMainBlock)
class MoreMainBlockAdmin(admin.ModelAdmin):
    list_display = ("title", "fontsize", "titleTwo", "fontsizeTiteTwo", "fontsizeTiteText", "fontsizeText")

@admin.register(MoreBlocks)
class MoreBlocksAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "image1", "image2", "image3", "showNumber")