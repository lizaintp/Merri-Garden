from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название сайта'
    )
    subtitle = RichTextField(
        verbose_name='Мини описание'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    insta = models.URLField(
        verbose_name='Instagram'
    )
    facebook = models.URLField(
        verbose_name='Facebook'
    )
    twitter = models.URLField(
        verbose_name='Twitter'
    )
    pinterest = models.URLField(
        verbose_name='Pinterest'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Основная настройка'
        verbose_name_plural = 'Основные настройки'
