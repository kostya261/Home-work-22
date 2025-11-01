from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование', unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.description)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование', unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/', verbose_name='Фотография')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='категория')
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.description)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['title', ]
