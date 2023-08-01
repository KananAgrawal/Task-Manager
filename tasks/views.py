from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import TaskSerializer
from .models import TaskDetail
from rest_framework.generics import UpdateAPIView
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['POST','GET','DELETE'])
def task_detail(request):
    if request.method == 'POST':
        task_data = request.data.get('tasks',[])
        serializer=TaskSerializer(data=task_data,many=True)
        if serializer.is_valid():
            serializer.save()
            t_id = [{'id':task.id} for task in serializer.instance]
            return Response({'task':t_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'GET':
        tasks = TaskDetail.objects.all().order_by('id')
        serializer = TaskSerializer(tasks,many=True)
        return Response({'tasks': serializer.data},status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        task_data = request.data.get('tasks',[])
        task_ids = [task.get('id') for task in task_data]
        tasks_delete = TaskDetail.objects.filter(id__in=task_ids)
        
        if len(tasks_delete)!=len(task_ids):
            return Response({"Error":"Some tasks IDs do not exist"},status=status.HTTP_400_BAD_REQUEST)
        tasks_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
@api_view(['GET','PUT','DELETE'])
def single_task(request,task_id):

    if request.method == 'GET':
        try:
            task = TaskDetail.objects.get(id=task_id)

        except:
            return Response({"error":"There is no task at that id"},status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        task = TaskDetail.objects.get(id=task_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        try:
            task = TaskDetail.objects.get(id=task_id)
        except:
            return Response({"Error": "There is no task at that id"},status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)


    

        