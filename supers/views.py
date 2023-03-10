from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers

 #This is the file that all the method or actions are in 
@api_view(['GET','POST'])
def supers_list(request):
    
    if request.method == 'GET':

        type = request.query_params.get('type')
        print (type)

        queryset = Supers.objects.all()

        if type:
             queryset = queryset.filter(super_type__type=type)

      
        serializer = SupersSerializer(queryset, many = True)
        return Response(serializer.data)
    elif request.method =='POST':
         serializer = SupersSerializer(data=request.data)
         if serializer.is_valid() == True:
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
        super = get_object_or_404(Supers, pk=pk)
        if request.method == 'GET':   
            serializer =SupersSerializer(super)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer =SupersSerializer(super, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'DELETE':
             super.delete()
             return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
