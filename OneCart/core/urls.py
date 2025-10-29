



from django.urls import path
from . import views

urlpatterns =[
   path("",views.LndingPage.as_view()),
   path("ai-interface/",views.ActionOnQuery.as_view()),
   path("shop/",views.ActionOnQuery.as_view()),
] 
