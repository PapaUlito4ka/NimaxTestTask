from rest_framework import serializers

from src.categories.models import Category
from src.categories.serializers import CategorySerializer
from src.items.models import Item
from src.items.validators import categories_count_validator


class ItemSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        many=True,
        slug_field="name",
        validators=[categories_count_validator],
    )

    class Meta:
        model = Item
        exclude = ("removed",)


class ListItemSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = "__all__"
