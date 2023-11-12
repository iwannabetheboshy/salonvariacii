# Generated by Django 4.2.6 on 2023-11-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_kitchencolors_kitchenfiles_remove_kitchen_short_desc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitchen',
            name='material',
        ),
        migrations.RemoveField(
            model_name='kitchen',
            name='openingMethod',
        ),
        migrations.AddField(
            model_name='kitchen',
            name='material',
            field=models.ManyToManyField(to='main.kitchenmaterial', verbose_name='Материал кухни'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='openingMethod',
            field=models.ManyToManyField(to='main.kitchenopeningmethod', verbose_name='Метод открытия кухни'),
        ),
    ]