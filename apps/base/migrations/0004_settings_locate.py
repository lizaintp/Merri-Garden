# Generated by Django 5.0.6 on 2024-05-18 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_settings_email_settings_facebook_settings_insta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='locate',
            field=models.CharField(default=1, max_length=255, verbose_name='Локация'),
            preserve_default=False,
        ),
    ]