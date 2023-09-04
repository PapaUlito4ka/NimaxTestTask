from typing import List

from rest_framework.serializers import ValidationError


def categories_count_validator(categories: List[str]):
    if not (2 <= len(categories) <= 10):
        raise ValidationError("Categories count must be between 2 and 10")
