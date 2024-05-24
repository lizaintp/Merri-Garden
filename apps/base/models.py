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
        verbose_name='Instagram',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook',
        blank=True, null=True
    )
    twitter = models.URLField(
        verbose_name='Twitter',
        blank=True, null=True
    )
    pinterest = models.URLField(
        verbose_name='Pinterest',
        blank=True, null=True
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

class Images(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение'
    )
    class Meta:
        verbose_name = 'Фотография на главной странице'
        verbose_name_plural = 'Фотографии на главных страницах'

class WhyChooseUs(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Почему выбирает нас'
        verbose_name_plural = 'Почему выбирают нас'

class WhyChooseUsImage(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение'
    )
    class Meta:
        verbose_name = 'Почему выбирает нас, изображение'
        verbose_name_plural = 'Почему выбирает нас, изображения'

class About(models.Model):
    desc = models.TextField(
        verbose_name='Описание'
    )
    subdesc = models.TextField(
        verbose_name='Подописание'
    )
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class AboutAbout(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название страницы'
    )
    desc = RichTextField(
        verbose_name='Описание',
        blank=True,null=True
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение страницы',
        blank=True,null=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Об о нас'
        verbose_name_plural = 'Об о нас'

class WhatDoWeOffer(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Что мы предлагаем'
        verbose_name_plural = 'Что мы предлагаем'

class WhatDoWeOfferImage(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение'
    )
    class Meta:
        verbose_name = 'Что мы предлагаем, изображение'
        verbose_name_plural = 'Что мы предлагаем, изображения'

class Comments(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото'
    )
    comment = models.TextField(
        verbose_name='Комментарий'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Имя'
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

