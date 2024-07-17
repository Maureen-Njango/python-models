from django.db import models

# Create your models here.
class ClassPeriod(models.model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField()
    classroom = models.CharField(max_length= 20)
    day_of_the_week = models.CharField(max_length= 20)
    def__str__(self):
        return self.classroom

