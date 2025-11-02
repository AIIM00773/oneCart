

from django.contrib import admin
from .models import (User, Marketplace, Product, Cart, CartItem,Order,OrderItem, AIPrompt,GeneralMenuContent)

modelsTuple = (User, Marketplace, Product, Cart, CartItem,Order,OrderItem, AIPrompt,GeneralMenuContent)

for  model in modelsTuple:
    admin.site.register(model)


