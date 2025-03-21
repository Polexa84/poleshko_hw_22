from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Creates test products in the database using a fixture'

    def handle(self, *args, **options):
        # Удаляем существующие данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загружаем данные из фикстуры
        call_command('loaddata', 'catalog/fixtures/data.json')

        self.stdout.write(self.style.SUCCESS('Test products created successfully using fixture!'))