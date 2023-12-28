# Generated by Django 4.2.6 on 2023-12-20 08:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_rename_fontsixeh_advantagestitle_fontsizeh_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogtitle',
            name='fontsizeFilter',
            field=models.IntegerField(default=16, help_text='Размер от 14 до 24', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(24)], verbose_name='Размер подписей фильтров'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalogtitle',
            name='fontsizeH',
            field=models.IntegerField(default=16, help_text='Размер от 16 до 36', validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(36)], verbose_name='Размер заголовка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalogtitle',
            name='fontsizeKitchen',
            field=models.IntegerField(default=16, help_text='Размер от 14 до 24', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(24)], verbose_name='Размер подписей кухонь'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalogtitle',
            name='fontsizeText',
            field=models.IntegerField(default=16, help_text='Размер от 14 до 24', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(24)], verbose_name='Размер текста'),
            preserve_default=False,
        ),
    ]