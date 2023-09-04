from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from src.categories.serializers import CategorySerializer
from src.categories.models import Category


class CategoryViewSet(
    mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet
):
    queryset = Category.objects.prefetch_related("items").all()
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        category: Category = self.get_object()
        if category.items.count() > 0:
            raise APIException(
                detail=f'Cannot delete category "{category.name}": has items',
                code=status.HTTP_400_BAD_REQUEST,
            )

        self.perform_destroy(category)
        return Response(status=status.HTTP_204_NO_CONTENT)
