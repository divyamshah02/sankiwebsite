from django.contrib import admin
from .models import Event, EventBannerImage, HomepageImages, ContactMessage, Products, ProductImage, ProductCategory


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_id')
    search_fields = ('category_name',)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_size', 'product_price', 'category')
    search_fields = ('product_name', 'product_size')
    list_filter = ('product_name', 'category')
    filter_horizontal = ('product_gallery_imgs',)  # For ManyToManyField


class EventAdmin(admin.ModelAdmin):
    # Add ordering to prioritize featured events first and then sort by creation date
    ordering = ['-featured_event']  # Assume you have a `created_at` field for the creation date

    list_display = ('event_name', 'event_date_range', 'event_city', 'event_state', 'ticket_price', 'featured_event')
    search_fields = ('event_name', 'event_city', 'event_state')
    filter_horizontal = ('event_gallery_imgs',)  # For ManyToManyField
    list_filter = ('featured_event',)

    def get_queryset(self, request):
        # Get the default queryset and order by `featured_event` and creation date
        queryset = super().get_queryset(request)
        return queryset.order_by('-featured_event')  # Make sure to use `-created_at` for descending order

    # Optional: If you don't have a `created_at` field, add it
    # created_at = models.DateTimeField(auto_now_add=True)  # Add this field to your Event model if needed

admin.site.register(Event, EventAdmin)
admin.site.register(HomepageImages)
admin.site.register(ContactMessage) 
admin.site.register(EventBannerImage)
admin.site.register(Products, ProductsAdmin)  # Register Products with ProductsAdmin
admin.site.register(ProductImage)  # Register ProductImage
admin.site.register(ProductCategory, ProductCategoryAdmin)  # Register ProductCategory

