from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
import uuid
import os


class KitchenStyle(models.Model):
    name = models.CharField('Введите стиль кухни',
                            help_text=("Пример: «Классический стиль»"),
                            max_length=50)

    class Meta:
        verbose_name = "стиль кухни"
        verbose_name_plural = "Стили кухни"

    def __str__(self):
        return self.name


class KitchenMaterial(models.Model):
    name = models.CharField('Введите материал кухни',
                            help_text=("Пример: «Лакированный»"),
                            max_length=50)

    class Meta:
        verbose_name = "материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return self.name


class KitchenOpeningMethod(models.Model):
    name = models.CharField('Введите способ открытия',
                            help_text=("Пример: «Ручка Pocket»"),
                            max_length=50)

    class Meta:
        verbose_name = "cпособ открытия"
        verbose_name_plural = "Способы открытия"

    def __str__(self):
        return self.name


class KitchenPhoto(models.Model):
    image = models.ImageField('Фото кухни', upload_to='kitchen/')

    def save(self, *args, **kwargs):
        safeImage('image', self.image, KitchenPhoto)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "фотографию кухни"
        verbose_name_plural = "Фотографии кухонь"


class KitchenColors(models.Model):
    name = models.CharField('Наименование цвета',
                            max_length=50,
                            help_text=("Введите наименование цвета"),)
    image = models.ImageField('Фото цвета',
                              help_text=("Фотография плитки цвета. Доступные форматы: jpg, png, webp"),
                              upload_to='kitchen/colors/')


    def save(self, *args, **kwargs):
        if self.image:
            safeImage('image', self.image, KitchenColors)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "цвет кухни"
        verbose_name_plural = "Цвета кухонь"

    def __str__(self):
        return self.name

class KitchenFinishing(models.Model):
    name = models.CharField('Введите наименование отделки',
                            help_text=("Пример: «Дубовая древесина»"),
                            max_length=50)
    colors = models.ManyToManyField(KitchenColors,
                                    help_text=("Выберите один или несколько цветов, которые соответствуют данной отделке"),
                                    blank=True,
                                    verbose_name="Цвета кухни")

    class Meta:
        verbose_name = "отделку кухни"
        verbose_name_plural = "Отделки кухонь"

    def __str__(self):
        return self.name

    def get_colors(self):
        return "; ".join([str(color) for color in self.colors.all()])




class KitchenFiles(models.Model):
    name = models.CharField('Имя файла', max_length=100)
    files = models.FileField('Файл', upload_to ='kitchen/files/',
                             validators=[FileExtensionValidator(allowed_extensions=["pdf"])])

    class Meta:
        verbose_name = "файл кухни"
        verbose_name_plural = "Файлы кухонь"

    def __str__(self):
        return f"{self.name}"

VIDEOPHOTO_CHOICES = (
    ('photo', "Фото"),
    ('video', "Видео")
)

class Kitchen(models.Model):
    name = models.CharField('Название кухни', max_length=50,
                            help_text=("Пример: «Young»"),)
    desc = models.TextField('Описание для страницы кухни',
                            help_text=("Отображается в карточке кухни. Обратите внимание - учитываются отступы и знаки переноса"),)
    style = models.ForeignKey(KitchenStyle,
                              on_delete=models.CASCADE,
                              verbose_name="Стиль кухни",
                              related_name='kitchens',
                              help_text=("«Любой» - означает, что кухня одновременно относится к классическому и современному стилю"),)
    material = models.ManyToManyField(KitchenMaterial,
                                      verbose_name="Материал кухни",
                                      help_text=("Выберите один или несколько материалов"))
    openingMethod = models.ManyToManyField(KitchenOpeningMethod,
                                           verbose_name="Метод открытия кухни",
                                           help_text=("Выберите один или несколько методов открытия кухни"))
    finishing = models.ManyToManyField(KitchenFinishing,
                                       verbose_name="Отделка кухни",
                                       help_text=("Выберите одну или несколько отделок кухни"))
    files = models.ManyToManyField(KitchenFiles,
                                   verbose_name="PDF-файлы",
                                   help_text=("Загрузите не более трех файлов в формате PDF. Присваиваете файлам корректные имена, например, «Техническое описание.pdf»"))
    mainImage = models.ImageField('Главное фото кухни',
                                  upload_to='kitchen/',
                                  help_text=("Отображается: 1) на главное странице в блоке «Каталог»; 2) на странице каталога"))
    catalogVideo = models.CharField('Видео для каталога',
                                    max_length=100,
                                    null=True,
                                    blank=True,
                                    help_text=("Проигрывается на странице каталога при наведении курсора на изображение кухни. Например: https://www.youtube.com/watch?v=z8xoGi5pK70") )
    kitchenCardVideoPhotoChoices = models.CharField('Выбирите видео или фото для карточки кухни', choices=VIDEOPHOTO_CHOICES, max_length=50,
                                                    help_text=("Обязательно выберите фото или введите ссылку на видео в блоке ниже"))
    kitchenCardVideo = models.CharField('Видео для карточки кухни',
                                        null=True,
                                        blank=True,
                                        max_length=100,
                                        help_text=("Отображается в карточке кухни. Например: https://www.youtube.com/watch?v=z8xoGi5pK70"))
    kitchenCardPhoto = models.ImageField('Фото для карточки кухни',
                                         null=True,
                                        blank=True,
                                        upload_to='kitchen/card/',
                                        help_text=("Доступные форматы: jpg, png, webp"))
    images = models.ManyToManyField(KitchenPhoto,
                                    verbose_name="Дополнительные фотографии кухни",
                                    help_text=("Объекты отображаются в порядке их добавления"))
    show_number = models.IntegerField('Номер показа в карусели каталога',
                                      null=True,
                                      blank=True,
                                      help_text=("Объекты отображаются в порядке возрастания"))
    slug = models.SlugField(blank=True)
    hide = models.BooleanField("Скрыть", help_text=("Для скрытия поставьте галочку"), default=False)
    advantages1 = models.CharField('Поле 1',
                                        null=True,
                                        blank=True,
                                        max_length=100)
    advantages2 = models.CharField('Поле 2',
                                        null=True,
                                        blank=True,
                                        max_length=100)
    advantages3 = models.CharField('Поле 3',
                                        null=True,
                                        blank=True,
                                        max_length=100)
    


    def save(self, *args, **kwargs):
        # Генерируем slug из названия кухни
        self.slug = "stosa_" + slugify(self.name).replace('-', '_')
        if self.mainImage:
            safeImage('mainImage', self.mainImage, Kitchen)
        
        if self.kitchenCardPhoto:
            safeImage('kitchenCardPhoto', self.kitchenCardPhoto, Kitchen)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "кухню"
        verbose_name_plural = "Кухни"

    def __str__(self):
        return self.name

    def get_material(self):
        return "; ".join([str(mat) for mat in self.material.all()])

    get_material.short_description = 'Материал кухни'

    def get_openingMethod(self):
        return "; ".join([str(opMed) for opMed in self.openingMethod.all()])

    get_openingMethod.short_description = 'Методы открытия кухни'


    def get_finishing(self):
        return "; ".join([str(fish) for fish in self.finishing.all()])
    
    get_finishing.short_description = 'Отделка кухни'


class MainPageCarousel(models.Model):
    name = models.CharField('Название кухни',
                            max_length=50,
                            help_text=("Пример: «Young»"))
    image = models.ImageField('Фото кухни',
                              upload_to='carousel/',
                              help_text=("Доступные форматы: jpg, png, webp"))
    show_number = models.IntegerField('Номер показа в карусели ',
                                      help_text=("Объекты отображаются в порядке возрастания"))
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = "stosa_" + slugify(self.name).replace('-', '_')
        if self.image:
            safeImage('image', self.image, MainPageCarousel)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "кухню"
        verbose_name_plural = "Карусель кухонь на первом экране"

    def __str__(self):
        return self.name


ALIGMENT_CHOICES = (
    ('center', "По центру"),
    ('left', "По левому краю"),
    ('end', "По правому краю" )
)
class AboutUs(models.Model):
    title = models.CharField('Заголовок',
                              max_length=50,
                              help_text=(
                                  "Пример: «О нас»"))

    fontsizeH=models.IntegerField('Размер заголовка',
                                 validators=[MinValueValidator(16), MaxValueValidator(36)],
                                 help_text=("Размер от 16 до 36"))        
    alignmentH=models.CharField('Выравнивание заголовка', max_length=300, choices = ALIGMENT_CHOICES)                       
    text = models.TextField('Текст',
                            help_text=("Обратите внимание - учитываются отступы и знаки переноса"))
    fontsizeText=models.IntegerField('Размер текста в блоке',
                                 validators=[MinValueValidator(14), MaxValueValidator(24)],
                                 help_text=("Размер от 14 до 24"))
    alignmentText=models.CharField('Выравнивание текста', max_length=300, choices = ALIGMENT_CHOICES)
    image = models.ImageField('Главное фото в блоке «О нас»',
                              upload_to='about/',
                              help_text=("Доступные форматы: jpg, png, webp"))
                              

    class Meta:
        verbose_name = "основную информацию «О нас»"
        verbose_name_plural = "Основная информация «О нас»"

    def __str__(self):
        return self.image.url


class LookAt(models.Model):
    content = models.FileField('Фото или видео',
                               help_text=("Доступные форматы: webp, jpg, png, mp4"),
                               upload_to='look_at/')

    shorts = models.CharField('Ссылка на полное видео',
                              max_length=100,
                              null=True,
                              blank=True,
                              help_text=(
                                  "Например: https://www.youtube.com/watch?v=z8xoGi5pK70"))

    name = models.CharField('Название видео', max_length=50,
                            help_text=("Обратите внимание - учитывается регистр введенных символов"))
    likes = models.IntegerField('Количество лайков')
    show_number = models.IntegerField('Номер показа',
                                      default=0,
                                      help_text=("Объекты отображаются в порядке возрастания"))
    hide = models.BooleanField("Скрыть", help_text=("Для скрытия поставьте галочку"), default=False)

    class Meta:
        verbose_name = "взгляни сам"
        verbose_name_plural = "Взгляните сами"

    def save(self, *args, **kwargs):
        if self.content:
            safeImage('content', self.content, LookAt)

        super().save(*args, **kwargs)

class LookAtTitle(models.Model):
    titleOne = models.CharField('Заголовок 1 уровня',
                              max_length=50,
                              null=True,
                              blank=True,
                              help_text=(
                                  "Пример: «Дизайн и качество»"))
    titleTwo = models.CharField('Заголовок 2 уровня',
                              max_length=50,
                              help_text=(
                                  "Пример: «Взгляните сами»"))

    class Meta:
        verbose_name = "взгляни сам"
        verbose_name_plural = "Заголовки блока «Взгляните сами»"

class FeedBack(models.Model):
    name = models.CharField('Имя', max_length=50)
    number = models.CharField('Номер телефона', max_length=20)
    message = models.TextField('Сообщение', blank=True, null=True)

    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "Заявки"

class FeedbackBlock(models.Model):
    title = models.CharField('Заголовок 1 уровня', max_length=50,
                            null=True,
                            blank=True,
        help_text=("Пример: «Контакты»"))
    fontsize = models.IntegerField('Размер заголовка 1 уровня',
                                 validators=[MinValueValidator(14), MaxValueValidator(22)],
                                 help_text=("Размер от 14 до 22"),
                                 default = 14)
    titleTwo = models.CharField('Заголовок 2 уровня', max_length=50,
        help_text=("Пример: «Контакты»"))
    fontsizeTiteTwo = models.IntegerField('Размер заголовка 2 уровня',
                                 validators=[MinValueValidator(16), MaxValueValidator(36)],
                                 help_text=("Размер от 16 до 36"))
    text = models.TextField('Текст подписи')
    fontsizeText = models.IntegerField('Размер текста подписи',
                                 validators=[MinValueValidator(14), MaxValueValidator(22)],
                                 help_text=("Размер от 14 до 22"))
    image = models.ImageField('Фоновая фотография',
                              upload_to='contact/',
                              help_text=("Доступные форматы: jpg, png, webp"))
    fontsizeBtn = models.IntegerField('Размер подписи кнопки "Оставить заявку"',
                                 validators=[MinValueValidator(14), MaxValueValidator(22)],
                                 help_text=("Размер от 14 до 22"))
    
    inputName = models.CharField('Надпись для ввода имени', max_length=50,
                                 help_text=("Например: «Имя (обязательно)»"))
    inputPhone = models.CharField('Надпись для ввода телефона', max_length=50,
                                 help_text=("Например: «Телефон (обязательно)»"))
    inputMassage = models.CharField('Надпись для ввода сообщения', max_length=50,
                                 help_text=("Например: «Сообщение»"))
    fontsizeInput = models.IntegerField('Размер подписей в форме',
                                 validators=[MinValueValidator(14), MaxValueValidator(22)],
                                 help_text=("Размер от 14 до 22"))
    def save(self, *args, **kwargs):
        if self.image:
             safeImage('image', self.image, FeedbackBlock)

        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "контакты"
        verbose_name_plural = "Блок контакты"

class Politic(models.Model):
    politucFile = models.FileField('Файл', upload_to ='politic/',
                             validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
                             
    class Meta:
        verbose_name = "файл"
        verbose_name_plural = "Файл политики обработки персональных данных"


class AdvantagesTitle(models.Model):
    title = models.CharField('Заголовок блока',
                              max_length=50,
                              help_text=(
                                  "Пример: «Почему нас выбирают»"))
    fontsizeH = models.IntegerField('Размер заголовка',
                                 validators=[MinValueValidator(16), MaxValueValidator(36)],
                                 help_text=("Размер от 16 до 36"))
    fontsizeTextH = models.IntegerField('Размер заголовка абзаца',
                                 validators=[MinValueValidator(14), MaxValueValidator(22)],
                                 help_text=("Размер от 14 до 22"))
    fontsizeText = models.IntegerField('Размер текста абзаца',
                                 validators=[MinValueValidator(14), MaxValueValidator(22)],
                                 help_text=("Размер от 14 до 22"))

    class Meta:
        verbose_name = "приемущества"
        verbose_name_plural = "Блок «Приемущества»"


class AdvantagesBlocks(models.Model):
    name = models.CharField('Наименование абзаца',
                              max_length=50,
                              help_text=(
                                  "Пример: «Компетентность»"))
    text = models.TextField('Текст абзаца',max_length=500)
    show_number = models.IntegerField('Номер показа',
                                      default=0,
                                      help_text=("Объекты отображаются в порядке возрастания"))
    
    class Meta:
        verbose_name = "приемущества"
        verbose_name_plural = "Текст в блоке «Приемущества»"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if AdvantagesBlocks.objects.count() < 4:
            super().save(*args, **kwargs)
        return HttpResponse('Слишком много записей блоков в приемуществах!')


class WatchVideoMain(models.Model):
    url = models.CharField('Ссылка на видео для кнопки «Смотреть видео» на главной странице',
                                null=True,
                                blank=True,
                                max_length=100,
                                help_text=("Например: https://www.youtube.com/watch?v=z8xoGi5pK70"))
    fontsize=models.IntegerField('Размер текста кнопки',
                                 validators=[MinValueValidator(14), MaxValueValidator(24)],
                                 help_text=("Размер от 14 до 24"))
    
    
    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "видео"
        verbose_name_plural = "Кнопка «Смотреть видео» на главной странице"

class CatalogMain(models.Model):
    fontsize=models.IntegerField('Размер текста кнопки',
                                 validators=[MinValueValidator(14), MaxValueValidator(24)],
                                 help_text=("Размер от 14 до 24"))
    
    class Meta:
        verbose_name = "надпись"
        verbose_name_plural = "Кнопка «Смотреть все кухни» на главной странице"




class CatalogTitle(models.Model):
    name = models.CharField('Наименование раздела',
                              max_length=50,
                              help_text=(
                                  "Пример: «Каталог кухонь»"))
    
    fontsizeH = models.IntegerField('Размер заголовка',
                                 validators=[MinValueValidator(16), MaxValueValidator(36)],
                                 help_text=("Размер от 16 до 36"))
    text = models.TextField('Подпись', 
                             help_text=(
                                  "Пример: «Мы делаем не просто кухни, мы создаём стиль»"))
    fontsizeText=models.IntegerField('Размер подписи заголовка',
                                 validators=[MinValueValidator(14), MaxValueValidator(24)],
                                 help_text=("Размер от 14 до 24"))
    fontsizeFilter=models.IntegerField('Размер подписей фильтров',
                                 validators=[MinValueValidator(14), MaxValueValidator(24)],
                                 help_text=("Размер от 14 до 24"))
    fontsizeKitchen=models.IntegerField('Размер подписей кухонь',
                                 validators=[MinValueValidator(14), MaxValueValidator(24)],
                                 help_text=("Размер от 14 до 24"))
    name404 = models.CharField('Надпись черного цвета',
                              max_length=50,
                              help_text=(
                                  "Пример: «К сожалению, ничего не найдено»"))
    fontsize404=models.IntegerField('Размер черной надписи',
                                 validators=[MinValueValidator(14), MaxValueValidator(24)],
                                 help_text=("Размер от 14 до 24"))
    name404Gray = models.CharField('Надпись серого цвета',
                              max_length=50,
                              help_text=(
                                  "Пример: «Попробуйте изменить критерии поиска»"))
    fontsize404Gray=models.IntegerField('Размер серой надписи',
                                 validators=[MinValueValidator(14), MaxValueValidator(24)],
                                 help_text=("Размер от 14 до 24"))
    
    
    class Meta:
        verbose_name = "надпись"
        verbose_name_plural = "Надписи в каталоге"

class Certificate(models.Model):
    name = models.CharField('Наименование сертификата',
                              max_length=50,
                              help_text=(
                                  "Пример: «CERTIFICAZIONE ISO 9001:2015»"))
    image = models.ImageField('Фотограия сертификата',
                              upload_to='certificate/',
                              help_text=("Доступные форматы: jpg, png, webp"))
    
    class Meta:
        verbose_name = "сертификат"
        verbose_name_plural = "Сертификаты в карточке кухни"

    def save(self, *args, **kwargs):
        if self.image:
            safeImage('image', self.image, Certificate)
        super().save(*args, **kwargs)

class KitchenCardText(models.Model):
    fontsizeH = models.IntegerField('Размер надписи кухни',
                                 validators=[MinValueValidator(16), MaxValueValidator(36)],
                                 help_text=("Размер от 16 до 36"))
    fontsizeText=models.IntegerField('Размер текста описания кухни',
                                 validators=[MinValueValidator(14), MaxValueValidator(24)],
                                 help_text=("Размер от 14 до 24"))
    fontsizeFile=models.IntegerField('Размер подписей файлов',
                                 validators=[MinValueValidator(14), MaxValueValidator(24)],
                                 help_text=("Размер от 14 до 24"))
    fontsizeAdvanteges=models.IntegerField('Размер подписей приемущества кухни',
                                 validators=[MinValueValidator(14), MaxValueValidator(24)],
                                 help_text=("Размер от 14 до 24"))
    fontsizeBtn = models.IntegerField('Размер подписи кнопки "Оставить заявку"',
                                 validators=[MinValueValidator(14), MaxValueValidator(22)],
                                 help_text=("Размер от 14 до 22"))
    
    colorMaterialName = models.CharField('Заголовок блока с материалами',
                              max_length=50,
                              help_text=(
                                  "Пример: «Цвет и отделка»"))
    fontsizeColorMaterial=models.IntegerField('Размер заголовка блока с материалами',
                                 validators=[MinValueValidator(16), MaxValueValidator(36)],
                                 help_text=("Размер от 16 до 36"))
    fontsizeNameMaterial=models.IntegerField('Размер подписи материала',
                                 validators=[MinValueValidator(14), MaxValueValidator(24)],
                                 help_text=("Размер от 14 до 24"))
    fontsizeNameColor=models.IntegerField('Размер подписи цвета',
                                 validators=[MinValueValidator(14), MaxValueValidator(24)],
                                 help_text=("Размер от 14 до 24"))
    

    certificateName = models.CharField('Заголовок блока с сертификатами',
                              max_length=50,
                              help_text=(
                                  "Пример: «Сертифицированное качество»"))
    fontsizeCertificateH=models.IntegerField('Размер заголовка блока с сертификатами',
                                 validators=[MinValueValidator(16), MaxValueValidator(36)],
                                 help_text=("Размер от 16 до 36"))
    fontsizeCertificateName=models.IntegerField('Размер подписи сертификатов',
                                 validators=[MinValueValidator(14), MaxValueValidator(24)],
                                 help_text=("Размер от 14 до 24"))
    
    class Meta:
        verbose_name = "надпись"
        verbose_name_plural = "Надписи в карточке кухни"


class CatalogMainBlock(models.Model):
    title = models.CharField('Заголовок 1 уровня', max_length=50,
                              null=True,
                            blank=True,
        help_text=("Пример: «Выберите идеальную кухню для вас»"))
    fontsize = models.IntegerField('Размер заголовка 1 уровня',
                                 validators=[MinValueValidator(14), MaxValueValidator(22)],
                                 help_text=("Размер от 14 до 22"),
                                 default = 14)
    titleTwo = models.CharField('Заголовок 2 уровня', max_length=50,
        help_text=("Пример: «Каталог»"))
    fontsizeTiteTwo = models.IntegerField('Размер заголовка 2 уровня',
                                 validators=[MinValueValidator(16), MaxValueValidator(36)],
                                 help_text=("Размер от 16 до 36"))
    kitchenTitle = models.IntegerField('Размер названия кухни',
                                 validators=[MinValueValidator(16), MaxValueValidator(36)],
                                 help_text=("Размер от 16 до 36"))
    kitchenTitleTwo = models.IntegerField('Размер надписи «Подробнее»',
                                 validators=[MinValueValidator(16), MaxValueValidator(36)],
                                 help_text=("Размер от 16 до 36"))
    
    class Meta:
        verbose_name = "надпись"
        verbose_name_plural = "Надписи в блоке «Каталог»"


class Header(models.Model):
    titleCatalog = models.CharField('Надпись для перехода в каталог', max_length=50,
        help_text=("Пример: «Каталог»"))
    titleLookAt = models.CharField('Надпись для перехода в блок «Взгляните сами»', max_length=50,
        help_text=("Пример: «Взгляните сами»"))
    titleMore = models.CharField('Надпись для перехода в блок «Больше возможностей»', max_length=50,
        help_text=("Пример: «Больше возможностей»"))
    titleContact = models.CharField('Надпись для перехода в блок «Контакты»', max_length=50,
        help_text=("Пример: «Контакты»"))

    fontsize = models.IntegerField('Размер надписей',
                                 validators=[MinValueValidator(14), MaxValueValidator(22)],
                                 help_text=("Размер от 14 до 22"))
    
    class Meta:
        verbose_name = "надписи"
        verbose_name_plural = "Шапка"


class Footer(models.Model):
    titleCatalog = models.CharField('Надпись для перехода в каталог', max_length=50,
        help_text=("Пример: «Каталог»"))
    titleLookAt = models.CharField('Надпись для перехода в блок «Взгляните сами»', max_length=50,
        help_text=("Пример: «Взгляните сами»"))
    titleMore = models.CharField('Надпись для перехода в блок «Больше возможностей»', max_length=50,
        help_text=("Пример: «Больше возможностей»"))
    titleContact = models.CharField('Надпись для перехода в блок «Контакты»', max_length=50,
        help_text=("Пример: «Контакты»"))

    fontsize = models.IntegerField('Размер надписей',
                                 validators=[MinValueValidator(14), MaxValueValidator(22)],
                                 help_text=("Размер от 14 до 22"))
    
    class Meta:
        verbose_name = "надписи"
        verbose_name_plural = "Подвал"


class MoreMainBlock(models.Model):
    title = models.CharField('Заголовок 1 уровня', max_length=50,
                            null=True,
                            blank=True,
        help_text=("Пример: «Дизайн»"))
    fontsize = models.IntegerField('Размер заголовка 1 уровня',
                                validators=[MinValueValidator(14), MaxValueValidator(22)],
                                help_text=("Размер от 14 до 22"),
                                default = 14)
    titleTwo = models.CharField('Заголовок 2 уровня', max_length=50,
        help_text=("Пример: «Больше возможностей»"))
    fontsizeTiteTwo = models.IntegerField('Размер заголовка 2 уровня',
                                 validators=[MinValueValidator(16), MaxValueValidator(36)],
                                 help_text=("Размер от 16 до 36"))
    
    fontsizeTiteText = models.IntegerField('Размер заголовка текста в слайде',
                                 validators=[MinValueValidator(14), MaxValueValidator(22)],
                                 help_text=("Размер от 14 до 22"))
    
    fontsizeText = models.IntegerField('Размер текста в слайде',
                                 validators=[MinValueValidator(14), MaxValueValidator(22)],
                                 help_text=("Размер от 14 до 22"))
    
    class Meta:
        verbose_name = "надпись"
        verbose_name_plural = "Надписи в блоке «Больше возможностей»"


class MoreBlocks(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст',
                            null=True,
                            blank=True,
                            help_text=("Обратите внимание - учитываются отступы и знаки переноса"))
    image1 = models.ImageField('Фотография 1',
                              upload_to='more/',
                              help_text=("Доступные форматы: jpg, png, webp. Отображается в первой строке"))
    image2 = models.ImageField('Фотография 2',
                              upload_to='more/',
                              help_text=("Доступные форматы: jpg, png, webp. Отображается во второй строке слева"))
    image3 = models.ImageField('Фотография 3',
                              upload_to='more/',
                              help_text=("Доступные форматы: jpg, png, webp. Отображается во второй строке справа"))
    showNumber = models.IntegerField('Номер показа в карусели',
                                      null=True,
                                      blank=True,
                                      help_text=("Объекты отображаются в порядке возрастания"))
    
    class Meta:
        verbose_name = "слайд"
        verbose_name_plural = "Слайды в блоке «Больше возможностей»"

    def save(self, *args, **kwargs):
        if self.image1:
            safeImage('image1', self.image1, MoreBlocks)
        if self.image2:
             safeImage('image2',self.image2, MoreBlocks)
        if self.image3:
            safeImage('image3',self.image3, MoreBlocks)
        super().save(*args, **kwargs)



def safeImage(field_name, imageName, imageModel):
    file_name = os.path.basename(imageName.name)
    file_extension = os.path.splitext(file_name)[1][1:].lower()

    if file_extension not in ('webp'):
        # Проверка наличия файла с таким же именем
        existing_file = imageModel.objects.filter(**{f'{field_name}__icontains':file_name}).first()
        if existing_file:
            imageName = existing_file.image
        else:
            name = str(uuid.uuid1())
            img = Image.open(imageName)
            img_io = BytesIO()
            img.save(img_io, format="WebP")
            img_file = InMemoryUploadedFile(img_io, None, f"{name}.webp", "image/webp", img_io.tell(), None)
            imageName.save(f"{name}.webp", img_file, save=False)
