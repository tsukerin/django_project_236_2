# Generated by Django 4.2.5 on 2023-11-28 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testik', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sertif',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='sertif',
            name='filled_sertif',
            field=models.ImageField(blank=True, upload_to='serif/%Y/%m/%d', verbose_name='Заполненный сертификат'),
        ),
    ]
