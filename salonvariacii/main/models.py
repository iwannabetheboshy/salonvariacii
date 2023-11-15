from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import uuid
import os


class KitchenStyle(models.Model):
    name = models.CharField('Наименование', max_length=50)

    class Meta:
        verbose_name = "стиль кухни"
        verbose_name_plural = "Стили кухни"

    def __str__(self):
        return self.name


class KitchenMaterial(models.Model):
    name = models.CharField('Наименование', max_length=50)

    class Meta:
        verbose_name = "материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return self.name


class KitchenOpeningMethod(models.Model):
    name = models.CharField('Наименование', max_length=50)

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
    name = models.CharField('Наименование цвета', max_length=50)
    image = models.ImageField('Фото цвета', upload_to='kitchen/colors/')


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
    name = models.CharField('Наименование отделки', max_length=50)
    colors = models.ManyToManyField(KitchenColors, blank=True, verbose_name="Цвета кухни")

    class Meta:
        verbose_name = "отделку кухни"
        verbose_name_plural = "Отделки кухонь"   

    def __str__(self):
        return self.name 

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
    name = models.CharField('Наименование', max_length=50)
    desc = models.TextField('Описание для страницы кухни')
    style = models.ForeignKey(KitchenStyle, on_delete=models.CASCADE, verbose_name="Стиль кухни", related_name='kitchens')
    material = models.ManyToManyField(KitchenMaterial, verbose_name="Материал кухни")
    openingMethod = models.ManyToManyField(KitchenOpeningMethod, verbose_name="Метод открытия кухни")
    finishing = models.ManyToManyField(KitchenFinishing, verbose_name="Отделка кухни")
    files = models.ManyToManyField(KitchenFiles, verbose_name="Файлы кухни")
    mainImage = models.ImageField('Главное фото', upload_to='kitchen/')
    catalogVideo = models.FileField('Видео для каталога', upload_to ='kitchen/videos/',
                                    validators=[FileExtensionValidator(allowed_extensions=["webm"])])
    kitchenCardVideo = models.FileField('Видео для страницы кухни', upload_to ='kitchen/videos/',
                                    validators=[FileExtensionValidator(allowed_extensions=["webm"])])
    images = models.ManyToManyField(KitchenPhoto, verbose_name="Дополнительные фотографии кухни")
    show_number = models.IntegerField('Номер показа в карусели каталога', null=True, blank=True)
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
    name = models.CharField('Название кухни', max_length=50)
    image = models.ImageField('Фото кухни',  upload_to='carousel/')
    show_number = models.IntegerField()

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
        verbose_name_plural = "Кухни в карусели на главной странице"

    def __str__(self):
        return self.name

    

class AboutUsDopBlock(models.Model):
    name = models.CharField('Подпись', max_length=50)
    value = models.CharField('Значение', max_length=50)
    
    class Meta:
        verbose_name = "Маленький блок в блоке о нас"
        verbose_name_plural = "Дополнительные значения в блоке о нас"

    def __str__(self):
        return self.name 


class AboutUs(models.Model):
    image = models.ImageField('Фото', upload_to='about/')
    text = models.TextField('Текст')
    
    class Meta:
        verbose_name = "блок о нас"
        verbose_name_plural = "Блок о нас"

    def __str__(self):
        return self.image.url  


class ReviewsAndProject(models.Model):
    image = models.ImageField('Фото', upload_to='review/')
    project_name = models.CharField('Название кухни', max_length=50)
    price = models.IntegerField('Стоимость проекта')
    squeare = models.IntegerField('Площадь кухни')
    review_name = models.CharField('Имя заказчика', max_length=100)
    text = models.TextField('Текст отзыва')
    
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
        verbose_name = "отзыв"
        verbose_name_plural = "Отзывы"


class LookAt(models.Model):
    content = models.FileField('Фото или видео',
                              help_text=("png, jpg, webp, mp4, webm"),
                              upload_to='look_at/')

    name = models.CharField('Название видео', max_length=50)
    likes = models.IntegerField('Количество лайков')
    show_number = models.IntegerField('Номер показа', default=0)

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
 
        