import django_filters
from django.db.models import QuerySet
from django_filters import BooleanFilter, Filter

from src.items.models import Item


class ItemFilter(django_filters.FilterSet):
    not_removed = Filter(method="filter_not_removed")

    def filter_not_removed(self, queryset: QuerySet[Item], name, value):
        return queryset.filter(removed=False)

    class Meta:
        model = Item
        fields = {
            "price": ["gte", "lte"],
            "categories__id": ["exact"],
            "published": ["exact"],
        }
