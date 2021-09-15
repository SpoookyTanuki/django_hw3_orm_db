import csv

from django.core.management.base import BaseCommand

from phones.models import Phone

from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader) # пропускаем заголовок
            for line in phone_reader:
                phone = Phone()
                phone.id = line[0]
                phone.name = line[1]
                phone.image = line[2]
                phone.price = line[3]
                phone.release_date = line[4]
                phone.lte_exists = line[5]
                phone.slug = slugify(line[1])

                phone.save() # TODO: Добавьте сохранение модели