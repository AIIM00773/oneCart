



from django.urls import path
from . import views

urlpatterns =[
   path("",views.ActionOnQuery.as_view()),
] 
