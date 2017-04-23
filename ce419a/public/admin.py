from django.contrib import admin

from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['stdid', 'get_year',
                    'first_name', 'last_name']
    list_filter = ['first_name']


admin.site.register(Student, StudentAdmin)
