from django.db import models
class Teacher (models.Model):
    first_name = models.CharField(max_length= 40)
    last_name = models.CharField(max_length= 40)
    email = models.CharField(max_length= 20)
    country = models.CharField(max_length= 20)
    date_of_birth = models.EmailField()
    age = models.PositiveSmallIntegerField()
    gender = models.PositiveSmallIntegerField()
    experience = models.PositiveSmallIntegerField()
    unit = models.CharField(max_length= 20)
    level_of_studies = models.CharField(max_length= 20)

    





