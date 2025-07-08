from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employees
from django.http import Http404
from rest_framework import mixins, generics

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
    
    
############################################ Class based ##################################################


# class Employee(APIView):  #here APIView class will decides which request to go to which function no need to write if method == 'GET' like if elif else conditions
#     def get(self, request):       #here self means we are presenting this function as a member function of above class
#         employees = Employees.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = EmployeeSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Employees.objects.get(pk=pk)
#         except Employees.DoesNotExist :
#             raise Http404
        
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer =  EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


######################################### Mixins ###########################################################


# class Employee(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
 
# class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin ,mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)
    
#     def put(self, request, pk):
#         return self.update(request,pk)
    
#     def delete(self, request, pk):
#         return self.destroy(request, pk)



############################################# Generic #########################################################
    
class Employee(generics.ListAPIView, generics.CreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

# class Employee(generics.ListCreateAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'






