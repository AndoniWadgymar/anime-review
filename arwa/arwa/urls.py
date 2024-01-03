from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

#DRF SPECTACULAR
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from anime.views import CreatorViewSet

router = DefaultRouter()
router.register(r"creator", CreatorViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]
