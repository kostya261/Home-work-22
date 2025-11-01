from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add Products to the database!'

    def handle(self, *args, **options):
        # Очищаем базу
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем категории (БЕЗ распаковки!)
        processors = Category.objects.create(title='Процессоры', description='Процессор различных фирм')
        monitors = Category.objects.create(title='Мониторы', description='Мониторы различных фирм')
        memorys = Category.objects.create(title='Память', description='Память различных фирм')  # Исправил название!

        products = [
            {'title': 'Intel Core i7',
             'description': 'Процессор фирмы Intel, 4 ядра, 8 потоков, частота процессора 3ГГц',
             'category': processors, 'price': 25000},  # Добавил цену
            {'title': 'AMD Rayzen',
             'description': 'Процессор фирмы AMD, 4 ядра, 8 потоков, частота процессора 3.2ГГц',
             'category': processors, 'price': 22000},  # Добавил цену

            {'title': 'Monitor Acer',
             'description': 'Монитор фирмы Acer', 'price': 5000, 'category': monitors},
            {'title': 'Monitor Benq',
             'description': 'Монитор фирмы Benq', 'price': 6000, 'category': monitors},
            {'title': 'Monitor Samsung',
             'description': 'Монитор фирмы Samsung', 'price': 9000, 'category': monitors},

            {'title': 'Memory Kingston',
             'description': 'Память Kingston', 'price': 800, 'category': memorys},
            {'title': 'Memory Hynix',
             'description': 'Память Hynix', 'price': 900, 'category': memorys},
        ]

        for product_data in products:  # Переименовал переменную
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added product: {product.title}'))  # Исправил SUCCES на SUCCESS
            else:
                self.stdout.write(self.style.WARNING(f'Product: {product.title} already exist!'))