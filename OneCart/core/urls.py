



from django.urls import path
from . import views

urlpatterns =[
   path("",views.LndingPage.as_view()),
   path("onecart-listings/", views.ListingsgPage.as_view()),
   path("onecart-ai/", views.OnecartaiPage.as_view()), 
   path("home/",views.OnecartHome.as_view()),
   path("shop/",views.OnecartHome.as_view()),
] 
