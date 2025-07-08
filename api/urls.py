from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('student/<int:pk>/',views.studentDetailView),

    path('employees/', views.Employee.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view())
]