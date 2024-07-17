from django.shortcuts import render
from rest_framework import APIview
from classperiod.models import ClassPeriod
from course.models import Courses
from teacher.models import Teacher
from student.models import Student
from .serializers import ClassPeriodserielizer,Studentserielizer,Coursesserielizer
from rest_framework.response import Response

# Create your views here.


class StudentListView(APIview):
    def get(self, request):
        students = Student.object.all()
        serializer = Studentserielizer(students , many = True)
        return Response(serializer.data)

class ClassPeriodListView(APIview):
    def get(self, request):
        classperiod = ClassPeriod.object.all()
        serializer = ClassPerioderielizer(classperiod , many = True)
        return Response(serializer.data)

class CourseListView(APIview):
    def get(self, request):
        course = CoursePeriod.object.all()
        serializer = CoursePerioderielizer(course, many = True)
        return Response(serializer.data)

class TeacherListView(APIview):
    def get(self, request):
        teacher = TeacherPeriod.object.all()
        serializer = TeacherPerioderielizer(teacher, many = True)
        return Response(serializer.data)



