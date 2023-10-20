from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .forms import Studentform
from .models import Student, Cource


# Create your views here.

@login_required
def Register(request):
    if request.method == "POST":
        form = Studentform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration_success.html')

    form = Studentform()
    dict_form = {
        'form': form
    }

    return render(request, 'register.html', dict_form)


@login_required
def view_student(request):
    queryset = Student.objects.all
    dict_form = {
        "queryset": queryset
    }
    return render(request, 'student_details.html', dict_form)


@login_required
def view_course(request):
    set = Cource.objects.all
    dict_form = {
        "set": set
    }
    return render(request, 'student_and_course.html', dict_form)
