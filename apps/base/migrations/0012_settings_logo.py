# Generated by Django 5.0.6 on 2024-05-18 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_remove_settings_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='logo',
            field=models.ImageField(default=1, upload_to='image/', verbose_name='Логотип'),
            preserve_default=False,
        ),
    ]
