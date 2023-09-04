from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, filters, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from src.items.filters import ItemFilter
from src.items.models import Item
from src.items.serializers import ListItemSerializer, ItemSerializer


class ItemViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Item.objects.prefetch_related("categories").all()
    serializer_classes = {
        "list": ListItemSerializer,
    }
    default_serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["name", "categories__name"]
    filterset_class = ItemFilter

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def destroy(self, request, *args, **kwargs):
        item: Item = self.get_object()
        Item.objects.filter(pk=item.pk).update(removed=True)
        return Response(status=status.HTTP_204_NO_CONTENT)
