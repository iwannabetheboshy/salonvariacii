# Generated by Django 4.2.6 on 2023-12-21 05:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_catalogmainblock'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackblock',
            name='fontsizeInput',
            field=models.IntegerField(default=123, help_text='Размер от 14 до 22', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(22)], verbose_name='Размер подписей в форме'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedbackblock',
            name='inputMassage',
            field=models.IntegerField(default=123, help_text='Размер от 14 до 22', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(22)], verbose_name='Надпись для ввода сообщения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedbackblock',
            name='inputName',
            field=models.IntegerField(default=123, help_text='Размер от 14 до 22', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(22)], verbose_name='Надпись для ввода имени'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedbackblock',
            name='inputPhone',
            field=models.IntegerField(default=123, help_text='Размер от 14 до 22', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(22)], verbose_name='Надпись для ввода телефона'),
            preserve_default=False,
        ),
    ]