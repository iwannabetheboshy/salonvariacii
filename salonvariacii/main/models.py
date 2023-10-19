from django.db import models


class Kitchen(models.Model):
    COLOR_CHOICES = (
        ('black', "black"),
        ('white', "white"),
    )

    STYLE_CHOICES = (
        ('classic', "classic"),
        ('modern', "modern"),
    )

    MATERIAL_CHOICES = (
        ('PVX', "PVX"),
        ('LDSP', "LDSP"),
        ('MDF', "MDF"),
    )

    FORM_CHOICES = (
        ('straight', "straight"),
        ('angular', "angular"),
        ('narrow', "narrow"),
    )
    color = models.CharField('Цвет', choices=COLOR_CHOICES, max_length=50)
    style = models.CharField('Стиль кухни', choices=STYLE_CHOICES, max_length=50)
    material = models.CharField('Материал кухни', choices=MATERIAL_CHOICES, max_length=50)
    form = models.CharField('Форма кухни', choices=FORM_CHOICES, max_length=50)
    width = models.IntegerField('Ширина кухни')

