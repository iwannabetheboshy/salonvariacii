# Generated by Django 4.2.6 on 2023-12-30 08:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_kitchencardtext_fontsizeadvanteges'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AboutUsDopBlock',
        ),
        migrations.AddField(
            model_name='catalogmainblock',
            name='kitchenTitle',
            field=models.IntegerField(default=12, help_text='Размер от 16 до 36', validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(36)], verbose_name='Размер названия кухни'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalogmainblock',
            name='kitchenTitleTwo',
            field=models.IntegerField(default=12, help_text='Размер от 16 до 36', validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(36)], verbose_name='Размер надписи «Подробнее»'),
            preserve_default=False,
        ),
    ]
