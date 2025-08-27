from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import StudentForm
from .models import Student

# ✅ Registration view
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
                        return redirect('student_profile', student_id=student.id)  # redirect to profile
    else:
        form = StudentRegistrationForm()
    return render(request, 'students/register.html', {'form': form})


            # Send email to student or admin
            send_mail(
                subject='New Student Registered',
                message=f"Student {student.first_name} {student.last_name} has registered.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[student.email],  # Or use your admin email
                fail_silently=False,
            )

            return redirect('success')
    else:
        form = StudentForm()

    return render(request, 'students/register.html', {'form': form})

# ✅ List view
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# ✅ Success page view
def success_view(request):
    return render(request, 'students/success.html')

from django.shortcuts import render, get_object_or_404
from .models import Student

def student_profile(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/profile.html', {'student': student})
