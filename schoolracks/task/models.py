from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length = 2)

class Racks(models.Model):
    racks_id = models.CharField(max_length = 2)
    students = models.ManyToManyField('Student', related_name = 'racks', blank = True)
