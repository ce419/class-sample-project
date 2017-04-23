from django.http import HttpResponse
from django.shortcuts import render

from ce419a.public.models import Student


def home(request):
    # if request._META['ACCEPT_LANGUAGE'] == 'fa':
    #     return HttpResponse('<h1>CE419</h1><h2>خوش آمدید!</h2>')

    # return HttpResponse('<h1>CE419</h1><h2>Welcome!</h2>')

    students = Student.objects.filter(
        stdid__startswith='92',
    )


    return render(request, 'home.html', {
        'title': 'SALAM',
        'students': students,
        'x': 2,
    })
