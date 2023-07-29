from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import TaskSerializer
from .models import TaskDetail
from rest_framework.generics import UpdateAPIView
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['POST','GET'])
def task_detail(request):
    if request.method == 'POST':
        task_data = request.data.get('tasks',[])
        serializer=TaskSerializer(data=task_data,many=True)
        if serializer.is_valid():
            serializer.save()
            t_id = [{'id':task.id} for task in serializer.instance]
            return Response({'task':t_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
       
    