


from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response 




from  .search_engine.parser import parse_query 
from .search_engine.utils import fetch_items


class ActionOnQuery(APIView):
    def get(self, request):
        return render(request, 'islands/finder-interface.html')
        
    def post(self, request):
        data = request.data
        
        #parser1(data)
        dataFetched=parse_query(data)
       
        if dataFetched:
            mchs= fetch_items(dataFetched)
            #print(mchs)
            
            return Response({"aa":mchs})
