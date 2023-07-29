from rest_framework import serializers
from .models import TaskDetail



class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TaskDetail
        fields = ['id','title','is_completed']

