


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
        

class ActionOnQuery(APIView):
    def get(self, request):
        return render(request, 'islands/finder-interface.html')
        
    def post(self, request):
        data = request.data
        
        #parser1(data)
        SteP1Returns = list(parse_query(data))
        
        Qobject = SteP1Returns[0]
        tokens = SteP1Returns[-1]
        
        print(f"\n\n{Qobject}\n\n")
       
        print(tokens)
        
        print("\n\n")
        if tokens:
            mchs= fetch_items(tokens)
            #print(mchs)
            
            return Response({"aa":mchs})
