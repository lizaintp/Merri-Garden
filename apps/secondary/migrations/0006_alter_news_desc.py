# Generated by Django 5.0.6 on 2024-05-23 04:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0005_aboutnews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='desc',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]