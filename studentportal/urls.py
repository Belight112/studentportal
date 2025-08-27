from django.contrib import admin
from django.urls import path
from students import views  #  Import your views from your app

urlpatterns = [
    path('admin/', admin.site.urls),

    #  Route for student registration form
    path('register/', views.register_student, name='student_register'),

    # Route to show list of registered students
    path('students/', views.student_list, name='student_list'),

    #  Optional: A success page after registration
    path('success/', views.success_view, name='success'),
]
