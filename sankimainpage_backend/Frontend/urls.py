from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

router.register(r'', HomeViewSet, basename='home')
router.register(r'event',EventDetailFrontEndViewSet , basename='event')
router.register(r'products', ProductsFrontEndViewSet, basename='products')
router.register(r'product-detail', ProductDetailFrontEndViewSet, basename='product-detail')

urlpatterns = [
    path('', include(router.urls))
]
