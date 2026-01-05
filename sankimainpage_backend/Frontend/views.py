from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
class HomeViewSet(viewsets.ViewSet):
    def list (self, request):
        return render(request, 'index.html')
    
class EventDetailFrontEndViewSet(viewsets.ViewSet):
    def list(self, request):
        return render(request, 'event-detail.html')

class ProductsFrontEndViewSet(viewsets.ViewSet):
    def list(self, request):
        return render(request, 'products_page.html')

class ProductDetailFrontEndViewSet(viewsets.ViewSet):
    def list(self, request):
        return render(request, 'product_detail.html')

