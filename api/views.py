from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

# def studentsView(request):
#     students = {
#         'id': 1,
#         'name': 'Harsh',
#         'class': "Computer Science"
#     }
#     return JsonResponse(students)


#Mannual way of serializing data (serialization see its defination in copy)
# def studentsView(request):
#     students = Student.objects.all()  #this will bring all the students in the DB
#     print(students)
#     student_list = list(students.values())  #as we are getting students as QuerySet so converting it into list so it can be easily convert into JSON 
#     return JsonResponse(student_list , safe=False)  #here as we using JsonResponse and getting students as QuerySet and JsonResponse expects as we sending dictioinary so it gives error thats why we use safe=False


@api_view(['GET', 'POST'])
def studentsView(request):
    print('request----', request.data)
    if request.method == 'GET':
        #get all the data from students table
        students = Student.objects.all()
        serializer =  StudentSerializer(students, many=True) #many=True coz we can have multiple students list
        # print('serializer----', serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print('errors----', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT' , 'DELETE'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer =  StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE' :
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        




