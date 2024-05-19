from django.db import models

# Create your models here.

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

class News(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название новости'
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
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'