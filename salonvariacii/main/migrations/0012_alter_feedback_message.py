# Generated by Django 4.2.6 on 2023-11-06 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_feedback_alter_kitchen_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Сообщение'),
        ),
    ]
