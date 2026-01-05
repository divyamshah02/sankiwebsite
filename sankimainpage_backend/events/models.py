from django.db import models
import uuid

class Event(models.Model):
    event_id = models.CharField(max_length=10, unique=True, editable=False, primary_key=True, default='')
    featured_event = models.BooleanField(default=False)
    event_name = models.CharField(max_length=255)
    event_details = models.TextField()
    event_venue = models.CharField(max_length=255)
    event_date_range = models.CharField(max_length=255)
    event_address = models.TextField()
    event_city = models.CharField(max_length=255)
    event_state = models.CharField(max_length=255)
    event_time = models.CharField(max_length=255)
    location_link = models.CharField(max_length=255, default='')
    event_title_img = models.ImageField(upload_to='event_title_images/')
    ticket_price = models.CharField(max_length=255)
    ticket_name = models.CharField(max_length=255, default='')
    digital_pass = models.BooleanField(default=False)
    artist_name = models.CharField(max_length=255, default='')
    artist_description = models.CharField(max_length=255, default='')
    artist_image = models.ImageField(upload_to='event_artist_images/', null=True, blank=True)
    event_gallery_imgs = models.ManyToManyField('EventBannerImage', blank=True)  # Many to Many for multiple images
    whatsapp_number  = models.CharField(max_length=255, default='')
    whatsapp_message = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.event_name

    def save(self, *args, **kwargs):
        if not self.event_id:
            self.event_id = self.generate_unique_event_id()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_event_id():
        while True:
            event_id = str(uuid.uuid4().int)[:10]  # Generate 10-digit number from UUID
            if not Event.objects.filter(event_id=event_id).exists():
                return event_id



class ProductCategory(models.Model):
    category_id = models.CharField(max_length=10, unique=True, editable=False, primary_key=True, default='')
    category_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category_name
        
    def save(self, *args, **kwargs):
        if not self.category_id:
            self.category_id = self.generate_unique_category_id()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_category_id():
        while True:
            category_id = str(uuid.uuid4().int)[:10]  # Generate 10-digit number from UUID
            if not ProductCategory.objects.filter(category_id=category_id).exists():
                return category_id
    
    class Meta:
        verbose_name_plural = "Product Categories"

class HomepageImages(models.Model):
    homepage_image = models.ImageField(upload_to='homepage_images/')
    image_description = models.CharField(max_length=255, default='')
    def __str__(self):
        return f"{self.homepage_image}"
   
    # other fields

class EventBannerImage(models.Model):
    banner_image = models.FileField(upload_to='event_banner_images/')

    def __str__(self):
        return f"{self.banner_image}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically stores submission time

    def __str__(self):
        return f"{self.name}"
    
class ProductImage(models.Model):
    product_image = models.FileField(upload_to='product_images/')
    
    def __str__(self):
        return f"{self.product_image}"

class Products(models.Model):
    product_id = models.CharField(max_length=10, unique=True, editable=False, primary_key=True, default='')
    product_name = models.CharField(max_length=255)
    product_size = models.CharField(max_length=255, default='')
    product_description = models.TextField()
    product_price = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='productsimages/')  # Main product image
    product_gallery_imgs = models.ManyToManyField('ProductImage', blank=True)  # Multiple product images
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    whatsapp_number = models.CharField(max_length=255, default='')
    whatsapp_message = models.CharField(max_length=255, default='')

    def __str__(self):
        return f"{self.product_name}"
        
    def save(self, *args, **kwargs):
        if not self.product_id:
            self.product_id = self.generate_unique_product_id()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_product_id():
        while True:
            product_id = str(uuid.uuid4().int)[:10]  # Generate 10-digit number from UUID
            if not Products.objects.filter(product_id=product_id).exists():
                return product_id
