from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.student_register, name='student_register'),
    path('', views.student_list, name='student_list'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('profile/<int:student_id>/', views.student_profile, name='student_profile'),
]
