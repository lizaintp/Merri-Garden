# Generated by Django 5.0.6 on 2024-05-24 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_settings_email_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='email_link',
        ),
    ]
