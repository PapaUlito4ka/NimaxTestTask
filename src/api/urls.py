from django.urls import path
from rest_framework import routers

from src.categories.views import CategoryViewSet
from src.items.views import ItemViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.SimpleRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="NimaxTestTask API",
        default_version="v1",
        description="Test description",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router.register(r"categories", CategoryViewSet)
router.register(r"items", ItemViewSet)

urlpatterns = router.urls

urlpatterns += [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
