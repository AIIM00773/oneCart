

from django.shortcuts import render, redirect 
import json 
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (Markets, Categories, Brands, Items , Countries) 

# Create your views here.



class GetMarkets(APIView):
    
    def get(self, request):
        return Response({"GetMarketResponse": ["Empty List "]})
