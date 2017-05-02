from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['stdid', 'first_name', 'last_name',
                  'year', 'courses']
