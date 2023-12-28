# Generated by Django 4.2.6 on 2023-12-21 00:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_catalogtitle_fontsize404_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KitchenCardText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fontsizeH', models.IntegerField(help_text='Размер от 16 до 36', validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(36)], verbose_name='Размер надписи кухни')),
                ('fontsizeText', models.IntegerField(help_text='Размер от 14 до 24', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(24)], verbose_name='Размер текста описания кухни')),
                ('fontsizeFile', models.IntegerField(help_text='Размер от 14 до 24', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(24)], verbose_name='Размер подписей файлов')),
                ('fontsizeColorMaterial', models.IntegerField(help_text='Размер от 16 до 36', validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(36)], verbose_name='Размер заголовка цветов')),
                ('fontsizeNameMaterial', models.IntegerField(help_text='Размер от 14 до 24', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(24)], verbose_name='Размер подписи материала')),
                ('fontsizeNameColor', models.IntegerField(help_text='Размер от 14 до 24', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(24)], verbose_name='Размер подписи цвета')),
                ('certificateName', models.CharField(help_text='Пример: «Сертифицированное качество»', max_length=50, verbose_name='Заголовок блока с сертификатами')),
                ('fontsizeCertificateH', models.IntegerField(help_text='Размер от 16 до 36', validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(36)], verbose_name='Размер заголовка блока с сертификатами')),
                ('fontsizeCertificateName', models.IntegerField(help_text='Размер от 14 до 24', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(24)], verbose_name='Размер подписи сертификатов')),
            ],
            options={
                'verbose_name': 'надпись',
                'verbose_name_plural': 'Надписи в карточке кухни',
            },
        ),
    ]