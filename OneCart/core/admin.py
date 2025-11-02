

from django.contrib import admin
from .models import (User, Marketplace, Product, Cart, CartItem,Order,OrderItem, AIPrompt)

modelsTuple = (User, Marketplace, Product, Cart, CartItem,Order,OrderItem, AIPrompt)

for  model in modelsTuple:
    admin.site.register(model)


