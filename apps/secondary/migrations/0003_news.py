# Generated by Django 5.0.6 on 2024-05-19 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0002_band'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Изображение')),
                ('title', models.CharField(max_length=100, verbose_name='Название новости')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
