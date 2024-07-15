from root_framework import serializer
from student.models import student
from root_framework.views import APIview
from rest_framework.Response import Response


class studentserielizer(serializers.modelserializer):
    class meta:
        model = student
        fields = "--all--"
class studentListView(APIview):
    def get(self, request):
        students = student.object.all()
        serializer = student.serializer(students, many = True)
        return Response(serializer.data)
