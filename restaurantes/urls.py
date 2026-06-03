from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TipoComidaViewSet, RestauranteViewSet

router = DefaultRouter()
router.register(r'tipos-comida', TipoComidaViewSet)
router.register(r'restaurantes', RestauranteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]