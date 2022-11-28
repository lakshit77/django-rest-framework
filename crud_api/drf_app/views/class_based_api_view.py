
from django.views import View
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from ..models import Student
from ..serializer import StudentModelSerailzier
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

class StudentAPI(APIView):

    def get(self, request):
        pythondata = request.data
        id = pythondata.get("id", None)

        if id is not None:
            stu_obj = Student.objects.get(id = id)
            stu_seri = StudentModelSerailzier(stu_obj)
            return Response(stu_seri.data)

        stu_obj = Student.objects.all()
        stu_seri = StudentModelSerailzier(stu_obj, many=True)
        return Response(stu_seri.data)


    def post(self, request):
        pythondata = request.data
        stu_seri = StudentModelSerailzier(data=pythondata)
        if stu_seri.is_valid():
            stu_seri.save()
            return Response(stu_seri.data)
        else:
            return Response(stu_seri.errors)


    def put(self, request):
        pythondata = request.data
        id = pythondata.get("id", None)
        stu_obj = Student.objects.get(id=id)
        stu_seri = StudentModelSerailzier(
            stu_obj, data=pythondata, partial=True)
        if stu_seri.is_valid():
            stu_seri.save()
            return Response(stu_seri.data)
        else:
            return Response(stu_seri.errors)

    def delete(self, request):
        pythondata = request.data
        id = pythondata.get("id", None)
        try:
            stu_obj = Student.objects.get(id=id)
        except Student.DoesNotExist:
            response = {
                "msg": f"There is no such student model with this id {id}"
            }
            return Response(response)
            
        stu_obj.delete()
        response = {
            "msg": "your data has beeen deletedddddd...."
        }
        return Response(response)

       