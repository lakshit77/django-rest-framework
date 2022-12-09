from rest_framework.response import Response
from rest_framework import viewsets

from ..models import Student
from ..serializer import StudentModelSerailzier, DeleteSerialzier, DeleteResponseSerialzier
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    # methods=["POST", "PUT"],
    request_body = StudentModelSerailzier,
    responses={"200": StudentModelSerailzier,},
    operation_id="Techsunami POST and PUT",
)
class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentModelSerailzier(stu, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if pk is not None:
            stu = Student.objects.get(id = pk)
            serializer = StudentModelSerailzier(stu)
            return Response(serializer.data)

    @swagger_auto_schema(
        request_body = StudentModelSerailzier,
        responses={"200": StudentModelSerailzier,},
        operation_id="Techsunami POST",
    )
    def create(self, request, pk=None):
        serializer = StudentModelSerailzier(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @swagger_auto_schema(
        request_body = StudentModelSerailzier,
        responses={"200": StudentModelSerailzier,},
        operation_id="Techsunami Patch",
    )
    def partial_update(self, request, pk=None):
        stu = Student.objects.get(id = pk)
        serializer = StudentModelSerailzier(stu, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @swagger_auto_schema(
        responses={"200": DeleteResponseSerialzier,},
        operation_id="Techsunami Delete API",
    )
    def destroy(self, request, pk):
        stu = Student.objects.get(id = pk)
        stu.delete()
        response = {
            "msg": "your data has beeen deletedddddd...."
        }
        return Response(response)

    