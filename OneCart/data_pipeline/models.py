from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from datetime import timedelta
import uuid


# -----------------------------------------------------------
# MARKETS MODEL
# -----------------------------------------------------------
class Markets(models.Model):
    market_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    # Branding and URLs
    market_logo_link = models.URLField(null=True, blank=True)
    market_website_link = models.URLField(null=True, blank=True)

    # API Endpoints
    api_endpoint_general_search = models.URLField(
        null=True, blank=True, help_text="API endpoint for general product search."
    )
    api_endpoint_categorised_search = models.URLField(
        null=True, blank=True, help_text="API endpoint for category-based search."
    )
    api_endpoint_filtered_search = models.URLField(
        null=True, blank=True, help_text="API endpoint for filtered or advanced search."
    )

    # Business details
    country_of_major = models.CharField(max_length=100, null=True, blank=True)
    category_focus = models.CharField(
        max_length=100, null=True, blank=True,
        help_text="Main product focus, e.g., Electronics, Fashion, etc."
    )

    # Ranking and status
    rank_score = models.DecimalField(
        max_digits=5, decimal_places=2, default=4.0,
        help_text="Dynamic score based on performance or popularity."
    )
    is_active = models.BooleanField(default=True)

    # Authentication
    market_authentication_id_verification = models.CharField(
        max_length=300, null=True, help_text="Used to verify market authenticity."
    )
    market_authentication_id_authentication = models.CharField(
        max_length=300, null=True, help_text="Used to authenticate API requests."
    )
    market_authentication_id_request_verification = models.CharField(
        max_length=300, null=True, help_text="Used to verify inter-system requests."
    )

    created_at = models.DateTimeField(auto_now=True)#auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Market"
        verbose_name_plural = "Markets"
        ordering = ['-rank_score', 'market_name']

    def __str__(self):
        return self.market_name

    def save(self, *args, **kwargs):
        if not self.slug and self.market_name:
            self.slug = slugify(self.market_name)
        super().save(*args, **kwargs)





# -----------------------------------------------------------
# CATEGORIES MODEL
# -----------------------------------------------------------
class Categories(models.Model):
    category_name = models.CharField(
        max_length=100, unique=True,
        help_text="Unique name of the category (e.g., Electronics, Fashion)."
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    category_display_image = models.ImageField(
        upload_to="categories/files/",
        null=True, blank=True,
        help_text="Representative image for this category."
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)




# -----------------------------------------------------------
# BRANDS MODEL
# -----------------------------------------------------------
class Brands(models.Model):
    brand_name = models.CharField(
        max_length=100, unique=True,
        help_text="Unique name of the brand (e.g., Nike, Apple)."
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    brand_display_image = models.ImageField(
        upload_to="brands/files/",
        null=True, blank=True,
        help_text="Representative image for this brand."
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        ordering = ['brand_name']

    def __str__(self):
        return self.brand_name

    def save(self, *args, **kwargs):
        if not self.slug and self.brand_name:
            self.slug = slugify(self.brand_name)
        super().save(*args, **kwargs)







# -----------------------------------------------------------
# ITEMS MODEL
# -----------------------------------------------------------
class Items(models.Model):
    item_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    item_image_link = models.URLField(null=True, blank=True)
    item_brand = models.CharField(max_length=200, null=True, blank=True)
    item_description = models.TextField(null=True, blank=True)
    item_category = models.CharField(max_length=200, null=True, blank=True)

    market_of_origin = models.ForeignKey(
        'Markets', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='items',
        help_text="Market from which this item was fetched."
    )

    item_origin = models.URLField(null=True, blank=True, help_text="Original data source or API endpoint.")
    item_link = models.URLField(null=True, blank=True, help_text="Direct link to item on market site.")

    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    item_to_market_verification_token = models.CharField(max_length=300, null=True)
    item_to_market_authentication_token = models.CharField(max_length=300, null=True)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ['item_name']

    def __str__(self):
        return self.item_name

    def save(self, *args, **kwargs):
        if not self.slug and self.item_name:
            self.slug = slugify(self.item_name)
        super().save(*args, **kwargs)




# -----------------------------------------------------------
# COUNTRIES MODEL
# -----------------------------------------------------------
class Countries(models.Model):
    country_name = models.CharField(max_length=100, null=True)
    country_code = models.CharField(
        max_length=10, null=True,
        help_text="ISO Alpha-2 or Alpha-3 code, e.g. 'KE' or 'KEN'."
    )
    country_short = models.CharField(max_length=20, null=True, blank=True)
    continent = models.CharField(max_length=50, null=True, blank=True)
    flag_link = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ['country_name']

    def __str__(self):
        return f"{self.country_name} ({self.country_code})"




# -----------------------------------------------------------
# FEATURED PRODUCTS MODEL
# -----------------------------------------------------------
class FeaturedProducts(models.Model):
    product = models.ForeignKey(
        'Items', on_delete=models.CASCADE,
        related_name='featured_entries',
        help_text="The product currently being featured."
    )
    market_of_origin = models.ForeignKey(
        'Markets', on_delete=models.CASCADE,
        related_name='featured_products',
        help_text="Market from which this product was fetched."
    )

    is_available = models.BooleanField(default=True)
    expires_in_minutes = models.IntegerField(default=1440, help_text="Default: expires in 1 day.")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Featured Product"
        verbose_name_plural = "Featured Products"
        ordering = ['-created_at']

    def __str__(self):
        return self.product.item_name if self.product else "Unknown Product"

    @property
    def is_expired(self):
        expiration_time = self.created_at + timedelta(minutes=self.expires_in_minutes)
        return timezone.now() > expiration_time




# -----------------------------------------------------------
# FEATURED MARKETS MODEL
# -----------------------------------------------------------
class FeaturedMarkets(models.Model):
    market = models.ForeignKey(
        'Markets', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='featured_entries',
        help_text="The market currently being featured."
    )

    expires_in_minutes = models.IntegerField(default=1440, help_text="Default: expires in 1 day.")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Featured Market"
        verbose_name_plural = "Featured Markets"
        ordering = ['-created_at']

    def __str__(self):
        return self.market.market_name if self.market else "Unknown Market"

    @property
    def is_expired(self):
        expiration_time = self.created_at + timedelta(minutes=self.expires_in_minutes)
        return timezone.now() > expiration_time



