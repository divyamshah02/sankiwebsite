from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Define router for viewsets
router = DefaultRouter()
router.register(r'all-events-api', EventListViewSet, basename='all-events-api')
router.register(r'event-detail-api', EventDetailViewSet, basename='event-detail-api')
router.register(r'contact-us-api', ContactMessageViewSet, basename='contact-us-api')
router.register(r'products-api', ProductsViewSet, basename='products-api')
router.register(r'product-categories-api', ProductCategoryViewSet, basename='product-categories-api')

urlpatterns = [
  # Home page using function-based view
    path('', include(router.urls)),  # Include router endpoints
]
