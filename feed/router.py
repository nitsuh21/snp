from feed.viewsets import PostViewset
from rest_framework import routers
from .models import Post

router = routers.DefaultRouter()
router.register('posts',PostViewset)