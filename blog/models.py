from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(default='', max_length=255, verbose_name='Заголовок:')
    message = models.TextField(default='', verbose_name='Текст статьи:')
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Добавляем автора в статью.
    public = models.BooleanField(default=False, verbose_name='Опубликовать:')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания:')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления:')

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
