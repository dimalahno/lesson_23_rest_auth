from rest_framework.routers import DefaultRouter
from .api_views import ProjectViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls
