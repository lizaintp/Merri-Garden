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