
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


@api_view(["GET", "POST", "PUT", "DELETE"])
def StudentAPI(request):

    if request.method == "GET":
        pythondata = request.data
        id = pythondata.get("id", None)

        if id is not None:
            stu_obj = Student.objects.get(id = id)
            stu_seri = StudentModelSerailzier(stu_obj)
            return Response(stu_seri.data)

        stu_obj = Student.objects.all()
        stu_seri = StudentModelSerailzier(stu_obj, many=True)
        return Response(stu_seri.data)


    elif request.method == "POST":
        pythondata = request.data
        stu_seri = StudentModelSerailzier(data=pythondata)
        if stu_seri.is_valid():
            stu_seri.save()
            return Response(stu_seri.data)
        else:
            return Response(stu_seri.errors)


    elif request.method == "PUT":
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

    elif request.method == "DELETE":
        pythondata = request.data
        id = pythondata.get("id", None)
        stu_obj = Student.objects.get(id=id)
        stu_obj.delete()
        response = {
            "msg": "your data has beeen deletedddddd...."
        }
        return Response(response)

       