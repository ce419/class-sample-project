from django.contrib import messages
from django.http import HttpResponse
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

    print(d)
    return render(request, 'home.html', {
        'title': 'CE419',
        'students': d,
        'courses': Course.objects.all(),
    })


def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            # messages.add_message(request, messages.SUCCESS, '')
    else:
        form = StudentForm()

    return render(request, 'student_add.html', {
        'form': form,
    })
