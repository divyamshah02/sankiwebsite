from rest_framework import serializers
from .models import *

class HomepageImageserializer(serializers.ModelSerializer):
    homepage_image = serializers.ImageField()
    class Meta:
        model = HomepageImages
        fields = '__all__'  # Keeping only the image field

# Add ProductCategory serializer
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['category_id', 'category_name']

class Eventserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
class EventBannerImageserializer(serializers.ModelSerializer):
    banner_image = serializers.ImageField()

    class Meta:
        model = EventBannerImage
        fields = '__all__'


class Eventdetailserializer(serializers.ModelSerializer):
    event_gallery_imgs = EventBannerImageserializer(many=True)
    class Meta:
        model = Event        
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    product_image = serializers.ImageField()

    class Meta:
        model = ProductImage
        fields = '__all__'
     
class Productsserializer(serializers.ModelSerializer):
    product_image = serializers.ImageField()
    product_gallery_imgs = ProductImageSerializer(many=True)
    category = ProductCategorySerializer(read_only=True)

    class Meta:
        model = Products
        fields = '__all__'