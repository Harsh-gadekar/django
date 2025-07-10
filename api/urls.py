from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('students/', views.studentsView),
    path('student/<int:pk>/',views.studentDetailView),

    # path('employees/', views.Employee.as_view()),
    # path('employee/<int:pk>/', views.EmployeeDetail.as_view())

    path('', include(router.urls)),

    path('blogs/', views.BlogView.as_view()),
    path('comments/', views.CommentView.as_view()),

    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]