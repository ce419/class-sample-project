from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from ce419a.public.forms import StudentForm
from ce419a.public.models import Student, Course


def home(request):
    # if request._META['ACCEPT_LANGUAGE'] == 'fa':
    #     return HttpResponse('<h1>CE419</h1><h2>خوش آمدید!</h2>')

    # return HttpResponse('<h1>CE419</h1><h2>Welcome!</h2>')

    d = {}

    for student in Student.objects.all():
        if student.year not in d:
            d[student.year] = []
        d[student.year].append(student)

    return render(request, 'home.html', {
        'title': 'CE419',
        'students': d,
        'courses': Course.objects.all(),
    })


@login_required
def student_add(request):
    # request.user.is_authenticated()
    # request.user.is_superuser
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'با موفقیت اضافه شد.')
            return HttpResponseRedirect('/')
    else:
        form = StudentForm()

    return render(request, 'student_add.html', {
        'form': form,
    })


def show_student(request, stdid):
    student = Student.objects.get(stdid=stdid)

    return render(request, 'show_student.html', {
        'student': student,
    })
