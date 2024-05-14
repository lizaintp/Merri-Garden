from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Имя'
    )
    lastname = models.CharField(
        max_length=100,
        verbose_name='Фамилия'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    subject = models.CharField(
        max_length=100,
        verbose_name='Тема'
    )
    comment = models.TextField(
        verbose_name='Комментарий'
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'