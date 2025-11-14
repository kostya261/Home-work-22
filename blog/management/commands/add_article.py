from django.core.management.base import BaseCommand
from django.core.management import call_command

from blog.models import Article, Topic
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add Products to the database!'

    def handle(self, *args, **options):
        # Очищаем базу
        Article.objects.all().delete()
        Topic.objects.all().delete()

        # Заменил на загрузку данных из фикстуры
        call_command('loaddata', 'blog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))