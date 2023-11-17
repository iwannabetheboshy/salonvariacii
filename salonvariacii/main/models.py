from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
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
    name = models.CharField('Имя файла', max_length=50)
    files = models.FileField('Файл', upload_to ='kitchen/files/',
                             validators=[FileExtensionValidator(allowed_extensions=["pdf"])])

    class Meta:
        verbose_name = "файл кухни"
        verbose_name_plural = "Файлы кухонь"   

    def __str__(self):
        return self.name
    

class Kitchen(models.Model):
    name = models.CharField('Название кухни', max_length=50,  
                            help_text=("Пример: «Stosa Young»"),)
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
    catalogVideo = models.FileField('Видео для каталога', 
                                    upload_to ='kitchen/videos/',
                                    validators=[FileExtensionValidator(allowed_extensions=["webm"])],
                                    help_text=("Проигрывается на странице каталога при наведении курсора на изображение кухни. Доступные форматы: mp4, webm"))
    kitchenCardVideo = models.FileField('Видео для карточки кухни', 
                                        upload_to ='kitchen/videos/',
                                        validators=[FileExtensionValidator(allowed_extensions=["webm"])],
                                        help_text=("Отображается в карточке кухни. Доступные форматы: mp4, webm"))
    images = models.ManyToManyField(KitchenPhoto, 
                                    verbose_name="Дополнительные фотографии кухни",
                                    help_text=("Объекты отображаются в порядке их добавления"))
    show_number = models.IntegerField('Номер показа в карусели каталога', 
                                      null=True, 
                                      blank=True,
                                      help_text=("Объекты отображаются в порядке возрастания"))
    slug = models.SlugField(blank=True)
    

    def save(self, *args, **kwargs):
        # Генерируем slug из названия кухни
        self.slug = slugify(self.name)

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

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "кухню"
        verbose_name_plural = "Кухни"

    def __str__(self):
        return self.name



class MainPageCarousel(models.Model):
    name = models.CharField('Название кухни', 
                            max_length=50,
                            help_text=("Пример: «Stosa Young»"))
    image = models.ImageField('Фото кухни',  
                              upload_to='carousel/',
                              help_text=("Доступные форматы: jpg, png, webp"))
    show_number = models.IntegerField('Номер показа в карусели ', 
                                      help_text=("Объекты отображаются в порядке возрастания"))

    def save(self, *args, **kwargs):
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


class AboutUs(models.Model):
    text = models.TextField('Текст',
                            help_text=("Обратите внимание - учитываются отступы и знаки переноса"))
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
                                   help_text=("Пример: «Иванов Иван»"))
    text = models.TextField('Текст отзыва',
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


class LookAt(models.Model):
    content = models.FileField('Фото или видео',
                              help_text=("Доступные форматы: jpg, png, webp, mp4, webm"),
                              upload_to='look_at/')

    name = models.CharField('Название видео', max_length=50,
                            help_text=("Обратите внимание - учитывается регистр введенных символов"))
    likes = models.IntegerField('Количество лайков')
    show_number = models.IntegerField('Номер показа', 
                                      default=0,
                                      help_text=("Объекты отображаются в порядке возрастания"))

    class Meta:
        verbose_name = "взгляни сам"
        verbose_name_plural = "Взгляните сами"

    def save(self, *args, **kwargs):
        if self.content:
            file_name = os.path.basename(self.content.name)
            file_extension = os.path.splitext(file_name)[1][1:].lower()

            if file_extension in ('png', 'jpg'):
                # Проверка наличия файла с таким же именем
                name = str(uuid.uuid1())
                img = Image.open(self.content)
                img_io = BytesIO()
                img.save(img_io, format="WebP")
                img_file = InMemoryUploadedFile(img_io, None, f"{name}.webp", "image/webp", img_io.tell(), None)
                self.content.save(f"{name}.webp", img_file, save=False)

class FeedBack(models.Model):
    name = models.CharField('Имя', max_length=50)
    number = models.CharField('Номер телефона', max_length=20)
    message = models.TextField('Сообщение', blank=True, null=True)
    
    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "Заявки"
 
        