from django.urls import path, include
from tasklist_app.views import TaskListCreate, TaskListDetail

urlpatterns = [
    path('tasklist',TaskListCreate.as_view()),
    path('tasklist/<int:pk>',TaskListDetail.as_view())
]