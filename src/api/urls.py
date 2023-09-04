from rest_framework import routers

from src.categories.views import CategoryViewSet
from src.items.views import ItemViewSet

router = routers.SimpleRouter()

router.register(r"categories", CategoryViewSet)
router.register(r"items", ItemViewSet)

urlpatterns = router.urls
