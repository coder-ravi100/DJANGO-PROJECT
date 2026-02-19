from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .studentSerliazers import StudentSerializer
# Create your views here.

@api_view(['GET'])
def students(request):
    s_all = Student.objects.all()
    serializer = StudentSerializer(s_all,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def studentget(request,pk):
    try:
        s_data = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"error" : "user not found"},status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(s_data)
    return Response(serializer.data)

@api_view(["POST"])
def add_student(request):
    serializer = StudentSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_student(request,pk):
    try:
        s_data = Student.objects.get(id = pk)
    except s_data.DoesNotExist:
        return Response({"error" : "invalid id"},status = status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(s_data,data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_student(request,pk):
    try:
        student = Student.objects.get(id =pk)
    except student.DoesNotExist:
        return Response({"error" : "invalid id"},status = status.HTTP_404_NOT_FOUND) 
    
    student.delete()

    return Response({"messsage" : "Successfully Deleted !"},status = status.HTTP_202_ACCEPTED) 