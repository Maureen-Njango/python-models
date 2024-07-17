from rest_framework import serializers
from classperiod.models import ClassPeriod
from student.models import student
from teacher.models import Teacher
from course.models import Courses


class Studentserielizer(serializers.modelserializer):
    class meta:
        model = Student
        fields = "--all--"

class ClassPeriodserielizer(serializers.modelserializer):
    class meta:
        model = ClassPeriod
        fields = "--all--"

class Coursesserielizer(serializers.modelserializer):
    class meta:
        model = Courses
        fields = "--all--"

class Teacherserielizer(serializers.modelserializer):
    class meta:
        model = Teacher
        fields = "--all--"


