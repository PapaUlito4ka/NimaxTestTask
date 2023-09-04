from django.core.validators import MinValueValidator
from django.db import models

from src.categories.models import Category


class Item(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    price = models.FloatField(
        null=False, blank=False, validators=[MinValueValidator(limit_value=1.0)]
    )
    published = models.BooleanField(default=False)
    removed = models.BooleanField(default=False)
    categories = models.ManyToManyField(to=Category, related_name="items")
