from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StudentSerializer
import io
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def student_api(request):
    if request.method == "GET":
        stu_objs = Student.objects.all()
        stu_seris = StudentSerializer(stu_objs, many = True)
        json_data = JSONRenderer().render(stu_seris.data)
        return HttpResponse(json_data, content_type="appliaction/json")

    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)

        if serializer.is_valid():
            serializer.save()
            json_data = JSONRenderer().render(serializer.data)
        else:
            json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data, content_type="appliaction/json")


@csrf_exempt
def student_api_detail(request, id):
    if request.method == "GET":
        stu_obj = Student.objects.get(id = id)
        stu_seris = StudentSerializer(stu_obj)
        json_data = JSONRenderer().render(stu_seris.data)
        return HttpResponse(json_data, content_type="appliaction/json")

    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        stu_obj = Student.objects.get(id=id)
        serializer = StudentSerializer(stu_obj, data=pythondata, partial=True)

        if serializer.is_valid():
            serializer.save()
            json_data = JSONRenderer().render(serializer.data)
        else:
            json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data, content_type="appliaction/json")

    if request.method == "DELETE":
        stu_obj = Student.objects.get(id=id)
        stu_obj.delete()
        res = {
            "msg": "Data deleteddd.."
        }
        # json_data = JSONRenderer().render(res)
        return JsonResponse(res)



    # return Response(dummy_dict)


