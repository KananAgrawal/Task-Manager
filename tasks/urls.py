from django.urls import path
from .views import task_detail
from tasks import views

urlpatterns= [
    path('v1/tasks/',views.task_detail,name='task-detail'),
]