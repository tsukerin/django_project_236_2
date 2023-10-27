# Generated by Django 4.2.5 on 2023-10-27 22:11

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Название')),
                ('image_full', models.ImageField(blank=True, upload_to='blank/%Y/%m/%d')),
                ('image_one', models.ImageField(blank=True, upload_to='blank/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Бланк',
                'verbose_name_plural': 'Бланки',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('title', models.TextField(max_length=50, verbose_name='Название')),
                ('avatar', models.ImageField(blank=True, upload_to='human/%Y/%m/%d')),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Человечки',
                'ordering': ['-title'],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Название')),
                ('Score', models.PositiveIntegerField()),
                ('Skills', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anketa.skills', verbose_name='Навык')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Model_prof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Название')),
                ('Score', models.PositiveIntegerField()),
                ('Professions', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anketa.professions', verbose_name='Профессия')),
                ('Skills', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anketa.skills', verbose_name='Навык')),
            ],
            options={
                'verbose_name': 'Модельная профессия',
                'verbose_name_plural': 'Модельные профессии',
                'ordering': ['-title'],
            },
        ),
    ]
