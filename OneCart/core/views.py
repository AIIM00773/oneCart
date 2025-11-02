


from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response 


from  .search_engine.parser import parse_query 
from .search_engine.utils import fetch_items



#from .search_engine.main import MAIN

class LndingPage(APIView):
    def get(self,request):
        return render(request, "index.html")
        


class ListingsgPage(APIView):
    def get(self,request):
        return render(request, "islands/onecartlistings.html")


class OnecartaiPage(APIView):
    def get(self,request):
        return render(request, "islands/onecartai.html")

             
class OnecartHome(APIView):
    def get(self, request):
        return render(request, 'islands/onecartnormal.html')
        
class OneCartcartPage(APIView):
    def get(self,request):
        return render(request, "islands/onecart-cart.html")


class OneCartcheckout(APIView):
    def get(self,request):
        return render(request,"islands/onecartcheckout.html" )


class OnecartStores(APIView):
    def get(self, request):
        return render(request, "islands/stores.html")









#-----------------------------------------------------------------------------------------------------------------------------------------------
from rest_framework.response import Response
from .models import Marketplace , GeneralMenuContent  # adjust path if needed
import json 


class ServeStores(APIView):
    def get(self, request):
        stores = Marketplace.objects.all().values() 
        return Response(tuple(stores))  


class ServeMenuItems(APIView):
    def get(self, request):
        stores = GeneralMenuContent.objects.all().values() 
        return Response(tuple(stores))  
