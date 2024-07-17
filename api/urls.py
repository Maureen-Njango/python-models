from django.urls import path
from .views import StudentListView , Course_List_view , TeacherListView


urlpattern =[
    path("students/", StudentListView.as_view(), name = "student_list_view"),
    path('classperiod/', ClassperiodListView.as_view(), name = 'classperiod_list_view'),
    path('courses/', CourseListView.as_view(), name = 'course_List_view'),
    path('teacher/', TeacherListView(), name='teacher_list_view'),
]