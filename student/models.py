from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    contry = models.CharField(max_length= 20)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    student_Gurdian= models.CharField(max_length = 20)
    student_locker_number = models.PositiveSmallIntegerField()
    student_mentor = models.CharField(max_length= 20)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
