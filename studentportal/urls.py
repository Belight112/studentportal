from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # <--- This is the homepage
    path('register/', views.register_student, name='student_register'),
    path('students/', views.student_list, name='student_list'),
    path('success/', views.success, name='success'),
]
