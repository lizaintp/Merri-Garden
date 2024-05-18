# Generated by Django 5.0.6 on 2024-05-17 16:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_settings_email_remove_settings_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Почта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='facebook',
            field=models.URLField(default=1, verbose_name='Facebook'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='insta',
            field=models.URLField(default=1, verbose_name='Instagram'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='phone',
            field=models.CharField(default=1, max_length=255, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='pinterest',
            field=models.URLField(default=1, verbose_name='Pinterest'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='subtitle',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Мини описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Название сайта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='twitter',
            field=models.URLField(default=1, verbose_name='Twitter'),
            preserve_default=False,
        ),
    ]