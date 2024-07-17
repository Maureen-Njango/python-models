from django.db import models

# Create your models here.
class Courses (models.Model):
    cources_name = models.CharField(max_length=20)
    course_number = models.PositiveSmallIntegerField()
    course_teacher = models.CharField(max_length= 20)
    course_details = models.CharField(max_length= 20)
    course_schedule = models.CharField(max_length= 20)
    course_break = models.CharField(max_length= 20)
    course_intrest = models.CharField(max_length=20)
    course_requirnment = models.CharField(max_length= 20)
    course_id = models.PositiveSmallIntegerField()
    course_points = models.PositiveSmallIntegerField()
