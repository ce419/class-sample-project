from django.db import models


class Student(models.Model):
    stdid = models.CharField(max_length=8)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    year = models.IntegerField(default=0)
    courses = models.ManyToManyField('Course')

    def get_color(self):
        import random

        color = '#'
        for i in range(6):
            color += random.choice('0987654321ABCDEF')
        return color

    def get_std_id(self):
        return self.stdid

    def get_year(self):
        return int(self.stdid[:2]) if self.stdid else None

    get_year.short_description = 'سال'

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_courses_count(self):
        return len(self.courses.all())

    def get_assignments_count(self):
        # s = 0
        # for course in self.courses.all():
        #     s += course.get_assignments_count()
        return sum(course.get_assignments_count() for course in
                   self.courses.all())


class Course(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    def get_assignments_count(self):
        return len(self.assignment_set.all())


class Assignment(models.Model):
    name = models.CharField(max_length=1000)
    course = models.ForeignKey(Course)

    url = models.URLField(blank=True)
    content = models.FileField(blank=True)
