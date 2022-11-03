from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(["GET"])
def sendData(request):
    dummy_dict = {
        "id": 1,
        "name": "techsunami"
    }

    return Response(dummy_dict)


