from django.contrib import admin

from .models import Student, Course, Assignment


class StudentAdmin(admin.ModelAdmin):
    list_display = ['stdid', 'year', 'first_name', 'last_name']
    list_filter = ['first_name']


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'course']
    search_fields = ['name', 'course__name']
    list_filter = ['course__name']


admin.site.register(Student, StudentAdmin)
admin.site.register(Course)
admin.site.register(Assignment, AssignmentAdmin)
