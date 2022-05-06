from ecommerce.viewsets import ProductViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products',ProductViewset)