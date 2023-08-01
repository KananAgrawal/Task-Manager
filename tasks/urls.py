from django.urls import path
from .views import task_detail,single_task
from tasks import views

urlpatterns= [
    path('v1/tasks/',views.task_detail,name='task-detail'),
    path('v1/tasks/<int:task_id>/',views.single_task,name='single-task')
]