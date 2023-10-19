from django.db import models


class Kitchen(models.Model):
    COLOR_CHOICES = (
        ('black', "Черный"),
        ('white', "Белый"),
    )

    STYLE_CHOICES = (
        ('classic', "Классический"),
        ('modern', "Модерн"),
    )

    MATERIAL_CHOICES = (
        ('PVX', "ПВХ"),
        ('LDSP', "ЛДСП"),
        ('MDF', "МДФ"),
    )

    FORM_CHOICES = (
        ('straight', "Прямой"),
        ('angular', "Угловой"),
        ('narrow', "Узкий"),
    )
    color = models.CharField('Цвет', choices=COLOR_CHOICES, max_length=50)
    style = models.CharField('Стиль кухни', choices=STYLE_CHOICES, max_length=50)
    material = models.CharField('Материал кухни', choices=MATERIAL_CHOICES, max_length=50)
    form = models.CharField('Форма кухни', choices=FORM_CHOICES, max_length=50)
    width = models.IntegerField('Ширина кухни')

