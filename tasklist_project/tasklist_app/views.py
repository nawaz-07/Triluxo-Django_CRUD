from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from . models import Task
from . serializers import TaskSerializer
from rest_framework import status
from rest_framework.exceptions import NotFound, ValidationError

# Create your views here.

class TaskListCreate(APIView):
    def get(self,request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many = True)
        return Response({"Success":serializer.data})

    def post(self,request):
        if not request.data:
            raise ValidationError("Request data is empty. Please provide task data.")

        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Successfully Created":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskListDetail(APIView):

    def get_object(self,pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return NotFound(detail="Task Not Exist")


    def get(self,request,pk):
        try:
            task = self.get_object(pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except:
            return Response({"msg": "Id not Exist Enter Valid Id"}, status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk):
        try:
            task = self.get_object(pk)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Data Updated Successfully":serializer.data})
        except:
            return Response({"msg": "Id not Exist Enter valid Id"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            task = self.get_object(pk)
            task.delete()
            return Response({"msg":"Record Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"msg": "Id not Exist Enter valid Id"}, status=status.HTTP_404_NOT_FOUND)
