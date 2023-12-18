# Generated by Django 4.2.6 on 2023-12-18 05:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_catalogmain_alter_watchvideomain_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advantagestitle',
            options={'verbose_name': 'приемущества', 'verbose_name_plural': 'Блок «Приемущества»'},
        ),
        migrations.RemoveField(
            model_name='advantagestitle',
            name='titleOne',
        ),
        migrations.RemoveField(
            model_name='advantagestitle',
            name='titleTwo',
        ),
        migrations.AddField(
            model_name='advantagestitle',
            name='fontsixeH',
            field=models.IntegerField(default=123, help_text='Размер от 16 до 36', validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(36)], verbose_name='Размер заголовка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advantagestitle',
            name='fontsixeText',
            field=models.IntegerField(default=123, help_text='Размер от 14 до 22', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(22)], verbose_name='Размер текста абзаца'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advantagestitle',
            name='fontsixeTextH',
            field=models.IntegerField(default=123, help_text='Размер от 14 до 22', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(22)], verbose_name='Размер заголовка абзаца'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advantagestitle',
            name='title',
            field=models.CharField(default=123, help_text='Пример: «Почему нас выбирают»', max_length=50, verbose_name='Заголовок блока'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advantagesblocks',
            name='text',
            field=models.TextField(max_length=500, verbose_name='Текст абзаца'),
        ),
    ]
