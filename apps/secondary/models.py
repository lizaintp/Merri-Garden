from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class AboutGallery(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название страницы'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение страницы'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'О Галереи'
        verbose_name_plural = 'О Галереях'

class Gallery(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    date = models.DateField(
        verbose_name='Дата'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Band(models.Model):
    photo = models.ImageField(
        upload_to='photo/',
        verbose_name='Фото сотрудника'
    )
    fullname = models.CharField(
        max_length=255,
        verbose_name='ФИО'
    )
    profession = models.CharField(
        max_length=255,
        verbose_name='Профессия'
    )
    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

class AboutBand(models.Model):
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
        verbose_name = 'О Команде'
        verbose_name_plural = 'О Командах'

class News(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название новости'
    )
    desc = RichTextField(
        verbose_name='Описание',
        blank=True,null=True
    )
    desc2 = RichTextField(
        verbose_name='Описание',
        blank=True,null=True
    )
    comment = RichTextField(
        verbose_name='Комментарии',
        blank=True,null=True
    )
    date = models.DateField(
        verbose_name='Дата'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class AboutNews(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название страницы'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение страницы'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'О Новости'
        verbose_name_plural = 'О Новостях'

