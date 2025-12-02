from django.core.management.base import BaseCommand
from django.core.management import call_command

from user_authentication.models import User


class Command(BaseCommand):
    help = 'Add Ussers!'

    def handle(self, *args, **options):
        # Очищаем базу
        User.objects.all().delete()


        # Заменил на загрузку данных из фикстуры
        call_command('loaddata', 'user_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
