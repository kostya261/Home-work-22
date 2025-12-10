from django.db import models

from config import settings


# Create your models here.


class Topic(models.Model):
    """ Описание Категории тем """
    title = models.CharField(max_length=100, verbose_name='наименование', unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'тема'
        verbose_name_plural = 'темы'


class Article(models.Model):
    """Структура статьи"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', verbose_name='Фотография', blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='articles', verbose_name='тема')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='дата обновления')
    views = models.PositiveIntegerField(default=0, verbose_name='просмотры')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_article',
        verbose_name='владелец',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['-created_at', 'title', ]
        permissions = [
            ("can_edit_article", "Can edit article"),
            ("can_unpublish_article", "Can unpublish_article"),
            ("can_description_article", "Can description article"),
            ("can_add_article", "Can add article"),
            ("can_view_article", "Can view article"),
            ("can_delete_article", "Can delete article"),
        ]
