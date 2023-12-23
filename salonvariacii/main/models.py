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
        file_name = os.path.basename(self.image.name)
        file_extension = os.path.splitext(file_name)[1][1:].lower()

        if file_extension not in ('webp'):
            # Проверка наличия файла с таким же именем
            existing_file = KitchenPhoto.objects.filter(image__icontains=self.image).first()
            if existing_file:
                self.image = existing_file.image
            else:
                name = str(uuid.uuid1())
                img = Image.open(self.image)
                img_io = BytesIO()
                img.save(img_io, format="WebP")
                img_file = InMemoryUploadedFile(img_io, None, f"{name}.webp", "image/webp", img_io.tell(), None)
                self.image.save(f"{name}.webp", img_file, save=False)
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
            file_name = os.path.basename(self.image.name)
            file_extension = os.path.splitext(file_name)[1][1:].lower()

            if file_extension not in ('webp'):
                # Проверка наличия файла с таким же именем
                existing_file = KitchenColors.objects.filter(image__icontains=self.image).first()
                if existing_file:
                    self.image = existing_file.image
                else:
                    name = str(uuid.uuid1())
                    img = Image.open(self.image)
                    img_io = BytesIO()
                    img.save(img_io, format="WebP")
                    img_file = InMemoryUploadedFile(img_io, None, f"{name}.webp", "image/webp", img_io.tell(), None)
                    self.image.save(f"{name}.webp", img_file, save=False)
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


    def save(self, *args, **kwargs):
        # Генерируем slug из названия кухни
        self.slug = "stosa_" + slugify(self.name).replace('-', '_')
        if self.mainImage:
            file_name = os.path.basename(self.mainImage.name)
            file_extension = os.path.splitext(file_name)[1][1:].lower()

            if file_extension not in ('webp'):
                # Проверка наличия файла с таким же именем
                existing_file = Kitchen.objects.filter(mainImage__icontains=self.mainImage).first()
                if existing_file:
                    self.mainImage = existing_file.mainImage
                else:
                    name = str(uuid.uuid1())
                    img = Image.open(self.mainImage)
                    img_io = BytesIO()
                    img.save(img_io, format="WebP")
                    img_file = InMemoryUploadedFile(img_io, None, f"{name}.webp", "image/webp", img_io.tell(), None)
                    self.mainImage.save(f"{name}.webp", img_file, save=False)
        
        if self.kitchenCardPhoto:
            file_name = os.path.basename(self.kitchenCardPhoto.name)
            file_extension = os.path.splitext(file_name)[1][1:].lower()
            print(file_extension)
            if file_extension not in ('webp'):
                
                # Проверка наличия файла с таким же именем
                existing_file = Kitchen.objects.filter(kitchenCardPhoto__icontains=self.kitchenCardPhoto).first()
                if existing_file:
                    self.kitchenCardPhoto = existing_file.kitchenCardPhoto
                else:
                    name = str(uuid.uuid1())
                    img = Image.open(self.kitchenCardPhoto)
                    img_io = BytesIO()
                    img.save(img_io, format="WebP")
                    img_file = InMemoryUploadedFile(img_io, None, f"{name}.webp", "image/webp", img_io.tell(), None)
                    self.kitchenCardPhoto.save(f"{name}.webp", img_file, save=False)

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
            file_name = os.path.basename(self.image.name)
            file_extension = os.path.splitext(file_name)[1][1:].lower()

            if file_extension not in ('webp'):
                # Проверка наличия файла с таким же именем
                existing_file = MainPageCarousel.objects.filter(image__icontains=self.image).first()
                if existing_file:
                    self.image = existing_file.image
                else:
                    name = str(uuid.uuid1())
                    img = Image.open(self.image)
                    img_io = BytesIO()
                    img.save(img_io, format="WebP")
                    img_file = InMemoryUploadedFile(img_io, None, f"{name}.webp", "image/webp", img_io.tell(), None)
                    self.image.save(f"{name}.webp", img_file, save=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "кухню"
        verbose_name_plural = "Карусель кухонь на первом экране"

    def __str__(self):
        return self.name



class AboutUsDopBlock(models.Model):
    value = models.CharField('Значение',
                             max_length=50,
                             help_text=("Укажите число, включая единицы измерения. Например, 100%"))
    name = models.CharField('Подпись',
                            max_length=50,
                            help_text=("Пример: «сделано в Италии»"))
    show_number = models.IntegerField('Номер показа ',
                                      help_text=("Объекты отображаются в порядке возрастания (слева направо)"))

    class Meta:
        verbose_name = "О нас в цифрах"
        verbose_name_plural = "О нас в цифрах "

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


class ReviewsAndProject(models.Model):
    image = models.ImageField('Главная фотография проекта',
                              upload_to='review/',
                              help_text=("Доступные форматы: jpg, png, webp"))
    project_name = models.CharField('Название кухни',
                                    max_length=50,
                                    help_text=("Пример: «Stosa Young»"))
    price = models.IntegerField('Стоимость проекта',
                                help_text=("Введите стоимость проекта в евро"))
    squeare = models.IntegerField('Площадь проекта',
                                  help_text=("Введите площадь проекта в квадратных метрах"))
    review_name = models.CharField('Фамилия и имя заказчика',
                                   max_length=100,
                                   null=True,
                                   blank=True,
                                   help_text=("Пример: «Иванов Иван»"))
    text = models.TextField('Текст отзыва',
                            null=True,
                            blank=True,
                            help_text=("Обратите внимание - учитываются отступы и знаки переноса"))

    def save(self, *args, **kwargs):
        if self.image:
            file_name = os.path.basename(self.image.name)
            file_extension = os.path.splitext(file_name)[1][1:].lower()

            if file_extension not in ('webp'):
                # Проверка наличия файла с таким же именем
                existing_file = ReviewsAndProject.objects.filter(image__icontains=self.image).first()
                if existing_file:
                    self.image = existing_file.image
                else:
                    name = str(uuid.uuid1())
                    img = Image.open(self.image)
                    img_io = BytesIO()
                    img.save(img_io, format="WebP")
                    img_file = InMemoryUploadedFile(img_io, None, f"{name}.webp", "image/webp", img_io.tell(), None)
                    self.image.save(f"{name}.webp", img_file, save=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "наш проект"
        verbose_name_plural = "Наши проекты"

class ReviewsAndProjectTitle(models.Model):
    title = models.CharField('Заголовок',
                              max_length=50,
                              help_text=(
                                  "Пример: «Наши проекты и отзывы»"))

    class Meta:
        verbose_name = "наш проект"
        verbose_name_plural = "Заголовки блока «Наши проекты»"

    def __str__(self):
        return self.title

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
            file_name = os.path.basename(self.content.name)
            file_extension = os.path.splitext(file_name)[1][1:].lower()

            if file_extension not in ('mp4', 'webp'):
                # Проверка наличия файла с таким же именем
                existing_file = LookAt.objects.filter(content__icontains=self.content).first()
                if existing_file:
                    self.content = existing_file.content
                else:
                    name = str(uuid.uuid1())
                    img = Image.open(self.content)
                    img_io = BytesIO()
                    img.save(img_io, format="WebP")
                    img_file = InMemoryUploadedFile(img_io, None, f"{name}.webp", "image/webp", img_io.tell(), None)
                    self.content.save(f"{name}.webp", img_file, save=False)
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
        help_text=("Пример: «Контакты»"))
    fontsize = models.IntegerField('Размер заголовка 1 уровня',
                                 validators=[MinValueValidator(14), MaxValueValidator(22)],
                                 help_text=("Размер от 14 до 22"))
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
            file_name = os.path.basename(self.image.name)
            file_extension = os.path.splitext(file_name)[1][1:].lower()

            if file_extension not in ('mp4', 'webp'):
                # Проверка наличия файла с таким же именем
                existing_file = LookAt.objects.filter(content__icontains=self.image).first()
                if existing_file:
                    self.image = existing_file.image
                else:
                    name = str(uuid.uuid1())
                    img = Image.open(self.image)
                    img_io = BytesIO()
                    img.save(img_io, format="WebP")
                    img_file = InMemoryUploadedFile(img_io, None, f"{name}.webp", "image/webp", img_io.tell(), None)
                    self.image.save(f"{name}.webp", img_file, save=False)
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
    text = models.CharField('Подпись', 
                             max_length=100,
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
            file_name = os.path.basename(self.image.name)
            file_extension = os.path.splitext(file_name)[1][1:].lower()

            if file_extension not in ('mp4', 'webp'):
                # Проверка наличия файла с таким же именем
                existing_file = LookAt.objects.filter(content__icontains=self.image).first()
                if existing_file:
                    self.image = existing_file.image
                else:
                    name = str(uuid.uuid1())
                    img = Image.open(self.image)
                    img_io = BytesIO()
                    img.save(img_io, format="WebP")
                    img_file = InMemoryUploadedFile(img_io, None, f"{name}.webp", "image/webp", img_io.tell(), None)
                    self.image.save(f"{name}.webp", img_file, save=False)
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
        help_text=("Пример: «Выберите идеальную кухню для вас»"))
    fontsize = models.IntegerField('Размер заголовка 1 уровня',
                                 validators=[MinValueValidator(14), MaxValueValidator(22)],
                                 help_text=("Размер от 14 до 22"))
    titleTwo = models.CharField('Заголовок 2 уровня', max_length=50,
        help_text=("Пример: «Каталог»"))
    fontsizeTiteTwo = models.IntegerField('Размер заголовка 2 уровня',
                                 validators=[MinValueValidator(16), MaxValueValidator(36)],
                                 help_text=("Размер от 16 до 36"))
    
    class Meta:
        verbose_name = "надпись"
        verbose_name_plural = "Надписи в блоке 'Каталог'"


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