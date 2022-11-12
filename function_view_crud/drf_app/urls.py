from django.urls import path
from drf_app import function_based_views


urlpatterns = [
    path("student_api", function_based_views.student_api),
    path("student_api/<int:id>", function_based_views.student_api_detail)
]
