

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

# -----------------------
# User Model
# -----------------------
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    wallet_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    # AbstractUser already provides:
    # username, password, first_name, last_name, date_joined, last_login

    def __str__(self):
        return self.username





# -----------------------
# Marketplace Model
# -----------------------
class Marketplace(models.Model):
    name = models.CharField(max_length=100)
    api_base_url = models.URLField()
    api_key = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='marketplace_logos/', blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True)
    product_relation_token = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name





# -----------------------
# Product Model
# -----------------------
class Product(models.Model):
    product_relation_token = models.CharField(max_length=100, blank=True, null=True)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=100)  # ID in external marketplace

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    was_price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10, default='KSH')
    
    image_url = models.URLField(blank=True, null=True)
    image_url1 = models.URLField(blank=True, null=True)
    image_url2 = models.URLField(blank=True, null=True)

    product_external_details_url = models.URLField(null=True)
    category = models.CharField(max_length=100, blank=True)
    brand =  models.CharField(max_length=100, blank=True)

    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.marketplace.name})"






# -----------------------
# Cart Model
# -----------------------
class Cart(models.Model):
    """
    Represents a user's shopping cart.
    Each user has one active cart at a time.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cart_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

    @property
    def total_amount(self):
        # Sum of all items in cart
        return sum(item.total_price for item in self.cartitems.all())

    @property
    def total_items(self):
        return sum(item.quantity for item in self.cartitems.all())




# -----------------------
# Cart Item Model
# -----------------------
class CartItem(models.Model):
    """
    Individual items in the cart.
    Stores product and quantity.
    """
    product_relation_token = models.CharField(max_length=100, blank=True, null=True)
    product_market_of_origin = models.ForeignKey(Marketplace, on_delete = models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey( Cart,on_delete=models.CASCADE,related_name='cartitems' )

    product = models.ForeignKey(Product , on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cart', 'product')  # prevent duplicates in same cart

    def __str__(self):
        return f"{self.product.title} x{self.quantity} in {self.cart.user.username}'s cart"

    @property
    def total_price(self):
        return self.product.price * self.quantity







# -----------------------
# Order Model
# -----------------------
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
        ('terminated', 'Terminated'), 
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    order_authentication_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    order_validation_token = models.CharField(max_length=100, blank=True, null=True)
    order_relation_token = models.CharField(max_length=100, blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Order {self.order_authentication_token} ({self.user.username})"







# -----------------------
# OrderItem Model
# -----------------------
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='Orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2)  # store price at purchase

    def __str__(self):
        return f"{self.product.title} x{self.quantity} (Order {self.order.id})"





# -----------------------
# AI Prompt Model (Optional)
# -----------------------
class AIPrompt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ai_prompts')
    prompt_text = models.TextField()
    response_json = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prompt by {self.user.username} at {self.created_at}"



