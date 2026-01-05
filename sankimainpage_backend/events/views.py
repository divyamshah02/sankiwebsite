from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Event, HomepageImages, EventBannerImage, ContactMessage, Products, ProductCategory
from rest_framework.decorators import api_view
from .serializers import Eventserializer, Eventdetailserializer, HomepageImageserializer, EventBannerImageserializer, ContactMessageSerializer, Productsserializer, ProductCategorySerializer

# Event List ViewSet
class EventListViewSet(viewsets.ViewSet):
    
    def list(self, request):
        events_list = Event.objects.all()
        serialized_data = Eventserializer(events_list, many=True).data
        homepageimages= HomepageImages.objects.all()
        serialized_data_images = HomepageImageserializer(homepageimages,many=True).data

        return Response(
            {
                "success": True,
                "data": {
                    "events_list": serialized_data,
                    "len_events_data": len(events_list),
                    "homepageimages": serialized_data_images,

                },
                "error": None
            }, status=status.HTTP_200_OK
        )

# Event Detail ViewSet
class EventDetailViewSet(viewsets.ViewSet):
    def list(self, request):
        event_id = request.GET.get('event_id')
        if not event_id:
            return Response(
                {
                    "success": False,
                    "user_not_logged_in": False,
                    "user_unauthorized": False,
                    "data": None,
                    "error": "Event_id not provided."
                }, status=status.HTTP_404_NOT_FOUND)
        
        event_obj = Event.objects.filter(event_id=event_id).first()

        if not event_obj:
            return Response(
                {
                    "success": False,
                    "user_not_logged_in": False,
                    "user_unauthorized": False,
                    "data": None,
                    "error": "Event not found."
                }, status=status.HTTP_404_NOT_FOUND)
        
        event_data =  Eventdetailserializer(event_obj).data
        print(event_data)
        return Response(
            {
                "success": True,
                "user_not_logged_in": False,
                "user_unauthorized": False,
                "data": {
                    "event_data": event_data
                },
                "error": None
            }, status=status.HTTP_200_OK
        )


class ContactMessageViewSet(viewsets.ViewSet):
    def create(self, request):
        # Extract fields from the request data (expecting JSON body)
        name = request.data.get('name')
        email = request.data.get('email')
        subject = request.data.get('subject')
        message = request.data.get('message')

        # Validation for missing fields
        if not all([name, email, subject, message]):
            return Response(
                {
                    "success": False,
                    "user_not_logged_in": False,
                    "user_unauthorized": False,
                    "data": None,
                    "error": "Missing required fields."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create the ContactMessage object
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return Response(
            {
                "success": True,
                "user_not_logged_in": False,
                "user_unauthorized": False,
                "data": None,
                "error": None
            },
            status=status.HTTP_200_OK
        )


class ProductsViewSet(viewsets.ViewSet):
    def list(self, request):
        product_id = request.GET.get('product_id')
        category_id = request.GET.get('category_id')
        
        if product_id:
            # If product_id is provided, filter by product_id
            products_list = Products.objects.filter(product_id=product_id)
        elif category_id:
            # If category_id is provided, filter by category
            products_list = Products.objects.filter(category__category_id=category_id)
        else:
            # Otherwise, get all products
            products_list = Products.objects.all()
            
        serialized_data = Productsserializer(products_list, many=True).data
        return Response(
            {
                "success": True,
                "data": {
                    "products_list": serialized_data,
                    "len_products_data": len(products_list),
                },
                "error": None
            }, status=status.HTTP_200_OK
        )

class ProductCategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        categories = ProductCategory.objects.all()
        serialized_data = ProductCategorySerializer(categories, many=True).data
        
        return Response(
            {
                "success": True,
                "data": {
                    "categories": serialized_data,
                },
                "error": None
            }, status=status.HTTP_200_OK
        )
        
    @action(detail=False, methods=['post'])
    def create_category(self, request):
        category_name = request.data.get('category_name')
        
        if not category_name:
            return Response(
                {
                    "success": False,
                    "error": "Category name is required."
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # Check if category with the same name already exists
        if ProductCategory.objects.filter(category_name__iexact=category_name).exists():
            return Response(
                {
                    "success": False,
                    "error": "A category with this name already exists."
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # Create new category
        category = ProductCategory.objects.create(category_name=category_name)
        serialized_data = ProductCategorySerializer(category).data
        
        return Response(
            {
                "success": True,
                "data": {
                    "category": serialized_data
                },
                "error": None
            }, 
            status=status.HTTP_201_CREATED
        )

# Home View (Template-based View)
def home_view(request):
    return render(request, 'index.html')  # Ensure `index.html` exists in templates
