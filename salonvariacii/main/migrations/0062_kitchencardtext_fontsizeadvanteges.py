# Generated by Django 4.2.6 on 2023-12-27 08:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0061_kitchen_advantages1_kitchen_advantages2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchencardtext',
            name='fontsizeAdvanteges',
            field=models.IntegerField(default=12, help_text='Размер от 14 до 24', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(24)], verbose_name='Размер подписей приемущества кухни'),
            preserve_default=False,
        ),
    ]