from rest_framework import routers
from .api import CoffeeViewSet

router = routers.DefaultRouter()
router.register('api/coffee', CoffeeViewSet, 'coffee')

urlpatterns = router.urls
