from rest_framework.response import Response
from rest_framework import viewsets

from ..models import Student
from ..serializer import StudentModelSerailzier, DeleteSerialzier, DeleteResponseSerialzier
from drf_yasg.utils import swagger_auto_schema


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerailzier
