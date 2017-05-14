import string

from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form
from django import forms

from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['stdid', 'first_name', 'last_name',
                  'year', 'courses']

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name[0] in string.ascii_letters:
            raise ValidationError('لطفا نام خود را به زبان فارسی وارد نمایید.')
        return first_name.strip()

class Form1(Form):
    username = forms.CharField()
