from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetsViewSet, basename='snippets')
router.register(r'tags', views.TagsViewSet, basename='tags')
router.register(r'dashboard', views.DashBoardViewSet, basename='dashboard')
urlpatterns = router.urls
