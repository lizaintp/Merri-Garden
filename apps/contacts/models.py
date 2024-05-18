from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    subject = models.CharField(
        max_length=100,
        verbose_name='Тема'
    )
    message = models.TextField(
        verbose_name='Комментарий'
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class Quetions(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название вопроса'
    )
    desc = models.TextField(
        verbose_name='Ответ на вопрос'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'