from django.urls import path
from .views import studentListView


urlpattern =[
    path("students/", studentListView.as_view(), name = "student_list_view"),
]