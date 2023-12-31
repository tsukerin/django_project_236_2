# Generated by Django 4.2.5 on 2023-11-10 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anketa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Название')),
                ('avatar', models.ImageField(blank=True, upload_to='human/%Y/%m/%d', verbose_name='Аватар')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Человечки',
                'ordering': ['-title'],
            },
        ),
        migrations.AlterField(
            model_name='blank',
            name='image_full',
            field=models.ImageField(blank=True, upload_to='blank/%Y/%m/%d', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='blank',
            name='image_one',
            field=models.ImageField(blank=True, upload_to='blank/%Y/%m/%d', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='model_prof',
            name='score',
            field=models.PositiveIntegerField(verbose_name='Очки'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='score',
            field=models.PositiveIntegerField(verbose_name='Очки'),
        ),
    ]
