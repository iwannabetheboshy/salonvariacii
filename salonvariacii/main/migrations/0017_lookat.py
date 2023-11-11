# Generated by Django 4.2.6 on 2023-11-07 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_feedback_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='LookAt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='png, jpg, gif', upload_to='look_at/', verbose_name='Фото или видео')),
                ('is_play', models.BooleanField(default=False, help_text='Только для видео', verbose_name='Воспроизводить?')),
                ('video_name', models.CharField(max_length=50, verbose_name='Название видео')),
                ('video_likes', models.IntegerField(verbose_name='Количество лайков')),
            ],
            options={
                'verbose_name': 'взгляни сам',
                'verbose_name_plural': 'Взгляните сами',
            },
        ),
    ]