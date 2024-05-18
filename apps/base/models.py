from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to='image/',
        verbose_name='Логотип'
    )
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
    locate = models.CharField(
        max_length=255,
        verbose_name='Локация'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Основная настройка'
        verbose_name_plural = 'Основные настройки'

class Instagram(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение'
    )
    image2 = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение 2'
    )
    image3 = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение 3'
    )
    image4 = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение 4'
    )
    image5 = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение 5'
    )
    image6 = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение 6'
    )
    image7 = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение 7'
    )
    image8 = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение 8'
    )
    image9 = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение 9'
    )
    
    class Meta:
        verbose_name = 'Фотография с инстаграмма'
        verbose_name_plural = 'Фотографии с инстаграмма'