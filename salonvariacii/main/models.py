from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


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
    style = models.ForeignKey(KitchenStyle, on_delete=models.CASCADE, verbose_name="Вид кухни", related_name='kitchens')
    material = models.ForeignKey(KitchenMaterial, on_delete=models.CASCADE, verbose_name="Материал кухни")
    openingMethod = models.ForeignKey(KitchenOpeningMethod, on_delete=models.CASCADE, verbose_name="Метод открытия кухни")
    mainImage = models.ImageField('Главное фото', upload_to='kitchen/')
    images = models.ManyToManyField(KitchenPhoto, blank=True, verbose_name="Дополнительные фотографии кухни")


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
    image = models.ImageField('Фото')
    text = models.TextField('Текст')
    
    class Meta:
        verbose_name = "блок о нас"
        verbose_name_plural = "Блок о нас"

    def __str__(self):
        return self.name  


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

    def __str__(self):
        return self.name   
        