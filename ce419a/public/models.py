from django.db import models


class Student(models.Model):
    stdid = models.CharField(max_length=8)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)

    def get_std_id(self):
        return self.stdid

    def get_year(self):
        return int(self.stdid[:2]) if self.stdid else None

    get_year.short_description = 'سال'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
