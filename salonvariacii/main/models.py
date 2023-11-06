from django.db import models
from django.utils.text import slugify


class KitchenStyle(models.Model):
    name = models.CharField('Наименование', max_length=50)

    class Meta:
        verbose_name = "стиль кухни"
        verbose_name_plural = "Стили кухни"

    def __str__(self):
        return self.name


class KitchenMaterial(models.Model):
    name = models.CharField('Наименование', max_length=50)
    kitchen_styles = models.ForeignKey(KitchenStyle, on_delete=models.CASCADE, verbose_name="Вид кухни")

    class Meta:
        verbose_name = "материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return self.name


class KitchenOpeningMethod(models.Model):
    name = models.CharField('Наименование', max_length=50)
    kitchen_styles = models.ForeignKey(KitchenStyle, on_delete=models.CASCADE, verbose_name="Вид кухни")

    class Meta:
        verbose_name = "cпособ открытия"
        verbose_name_plural = "Способы открытия"

    def __str__(self):
        return self.name


class KitchenPhoto(models.Model):
    image = models.ImageField('Фото кухни', upload_to='kitchen/')

    class Meta:
        verbose_name = "фотографию кухни"
        verbose_name_plural = "Фотографии кухонь"
    

class Kitchen(models.Model):
    name = models.CharField('Наименование', max_length=50)
    short_desc = models.CharField('Краткое описание для карусели каталога', blank=True, max_length=300)
    style = models.ForeignKey(KitchenStyle, on_delete=models.CASCADE, verbose_name="Вид кухни", related_name='kitchens')
    material = models.ForeignKey(KitchenMaterial, on_delete=models.CASCADE, verbose_name="Материал кухни")
    openingMethod = models.ForeignKey(KitchenOpeningMethod, on_delete=models.CASCADE, verbose_name="Метод открытия кухни")
    mainImage = models.ImageField('Главное фото', upload_to='kitchen/')
    images = models.ManyToManyField(KitchenPhoto, blank=True, verbose_name="Дополнительные фотографии кухни")
    show_number = models.IntegerField('Номер показа в карусели каталога', null=True, blank=True)
    slug = models.SlugField(blank=True)
    

    def save(self, *args, **kwargs):
        # Генерируем slug из названия кухни
        self.slug = slugify(self.name)
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
    
    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "Отзывы"

class FeedBack(models.Model):
    name = models.CharField('Имя', max_length=50)
    number = models.CharField('Номер телефона', max_length=20)
    message = models.TextField('Сообщение', blank=True, null=True)
    
    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "Заявки"
 
        