
from django.views import View
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from ..models import Student
from ..serializer import StudentSerializer, StudentModelSerailzier

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name="dispatch")
class StudentAPI(View):

    def get(self, request, *arg, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id", None)

        if id is not None:
            stu_obj = Student.objects.get(id = id)
            stu_seri = StudentModelSerailzier(stu_obj)
            json_data = JSONRenderer().render(stu_seri.data)
            return HttpResponse(json_data, content_type = "application/json")

        stu_obj = Student.objects.all()
        stu_seri = StudentModelSerailzier(stu_obj, many=True)
        json_data = JSONRenderer().render(stu_seri.data)
        return HttpResponse(json_data, content_type="application/json")


    def post(self, request, *arg, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        stu_seri = StudentModelSerailzier(data=pythondata)
        if stu_seri.is_valid():
            stu_seri.save()
            json_data = JSONRenderer().render(stu_seri.data)

        else:
            json_data = JSONRenderer().render(stu_seri.errors)
        return HttpResponse(json_data, content_type="application/json")

    def put(self, request, *arg, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id", None)

        stu_obj = Student.objects.get(id=id)
        stu_seri = StudentModelSerailzier(
            stu_obj, data=pythondata, partial=True)
        if stu_seri.is_valid():
            stu_seri.save()
            json_data = JSONRenderer().render(stu_seri.data)

        else:
            json_data = JSONRenderer().render(stu_seri.errors)
        return HttpResponse(json_data, content_type="application/json")

    def delete(self, request, *arg, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id", None)

        stu_obj = Student.objects.get(id=id)
        stu_obj.delete()

        response = {
            "msg": "your data has beeen deletedddddd...."
        }

        json_data = JSONRenderer().render(response)
        return HttpResponse(json_data, content_type="application/json")

       