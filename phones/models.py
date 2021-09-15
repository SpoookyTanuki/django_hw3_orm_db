from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля - id, name, price, image, release_date, lte_exists и slug
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    lte_exists = models.BooleanField(null=True, blank=True)
    slug = models.TextField(null=True, blank=True)
