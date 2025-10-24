





from django.urls import path
from . import views

urlpatterns = [
    path("getMarkets/", views.GetMarkets.as_view(), name="get_markets")
]
