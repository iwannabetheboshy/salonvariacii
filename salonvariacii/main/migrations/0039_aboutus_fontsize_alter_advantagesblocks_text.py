# Generated by Django 4.2.6 on 2023-12-11 23:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_alter_advantagesblocks_text_alter_catalogtitle_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='fontsize',
            field=models.IntegerField(default=18, help_text='Размер от 14 до 32', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(32)], verbose_name='Размер текста в блоке'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advantagesblocks',
            name='text',
            field=models.TextField(max_length=180, verbose_name='Текст абзаца'),
        ),
    ]
