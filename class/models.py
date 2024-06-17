from django.db import models
class Classroom(models.Model):
    class_name = models.CharField(max_length = 20)
    class_number = models.PositiveSmallIntegerField()
    teacher_incharge = models.CharField(max_length = 15)
    number_of_students = models.PositiveSmallIntegerField()
    number_of_sits = models.PositiveSmallIntegerField()
    number_of_tables = models.PositiveSmallIntegerField()
    number_of_boards = models.PositiveSmallIntegerField()
    numbers_of_doors= models.PositiveSmallIntegerField()
    class_color = models.CharField(max_length = 20)
    number_of_art = models.PositiveSmallIntegerField()

    

    



